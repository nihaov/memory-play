#!/usr/bin/env python3
"""Render an original note sequence to a small, dependency-free WAV."""

import argparse
import json
import math
import struct
import wave
from pathlib import Path

SAMPLE_RATE = 22050
MAX_SECONDS = 45
VOICES = {
    "keys": (0.022, 0.13, 1.4, 0.27, 0.13),
    "pluck": (0.004, 0.085, 3.8, 0.36, 0.18),
    "bass": (0.017, 0.15, 0.7, 0.18, 0.04),
}


def render_score(score):
    bpm = float(score["bpm"])
    if not 40 <= bpm <= 220:
        raise ValueError("BPM must be between 40 and 220.")
    seconds_per_beat = 60 / bpm
    events = score["notes"]
    if not isinstance(events, list) or not 1 <= len(events) <= 300:
        raise ValueError("Provide 1 to 300 notes.")

    notes = []
    for note in events:
        start = float(note["beat"]) * seconds_per_beat
        duration = float(note["length"]) * seconds_per_beat
        pitch = note["pitch"]
        voice = note["voice"]
        velocity = float(note.get("velocity", 0.7))
        if not (0 <= start < start + duration <= MAX_SECONDS):
            raise ValueError("Every note must have a positive length and end within 45 seconds.")
        if type(pitch) is not int or not 24 <= pitch <= 96 or voice not in VOICES:
            raise ValueError("Use a MIDI pitch from 24 to 96 and a voice of keys, pluck, or bass.")
        if not 0 < velocity <= 1:
            raise ValueError("Velocity must be greater than zero and at most one.")
        notes.append((start, duration, pitch, voice, velocity))

    sample_count = math.ceil((max(start + duration for start, duration, *_ in notes) + 0.2) * SAMPLE_RATE)
    samples = [0.0] * sample_count
    for start, duration, pitch, voice, velocity in notes:
        mix_note(samples, start, duration, pitch, voice, velocity)

    peak = max(map(abs, samples))
    if not peak:
        raise ValueError("The score produced no audible samples.")
    level = 26000 / peak
    return b"".join(struct.pack("<h", round(sample * level)) for sample in samples)


def mix_note(samples, start, duration, pitch, voice, velocity):
    attack, release, decay, overtone, third_harmonic = VOICES[voice]
    first_sample = round(start * SAMPLE_RATE)
    frequency = 440 * 2 ** ((pitch - 69) / 12)
    for index in range(math.ceil(duration * SAMPLE_RATE)):
        elapsed = index / SAMPLE_RATE
        envelope = min(1, elapsed / attack, (duration - elapsed) / release)
        phase = math.tau * frequency * elapsed
        tone = math.sin(phase) + overtone * math.sin(2 * phase) + third_harmonic * math.sin(3 * phase)
        samples[first_sample + index] += tone * velocity * envelope * math.exp(-decay * elapsed)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("score", type=Path, help="JSON score")
    parser.add_argument("output", type=Path, help="New WAV file")
    args = parser.parse_args()
    try:
        score = json.loads(args.score.read_text(encoding="utf-8"))
        frames = render_score(score)
        with args.output.open("xb") as output, wave.open(output, "wb") as wav:
            wav.setparams((1, 2, SAMPLE_RATE, 0, "NONE", "not compressed"))
            wav.writeframes(frames)
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
