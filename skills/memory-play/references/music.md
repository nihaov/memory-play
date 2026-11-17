# My Theme Music

Pick two or three remembered details that can be heard in the music. For example, a running habit could become a steady pulse, and a repeatedly tinkered-with object could become a short motif that returns with a changed note. Choose a direction based on the available memories and the user's preferences. Give the cue an opening, a variation, and a clear ending, usually in 20–35 seconds.

1. Use an available music generation tool if it can deliver an original instrumental cue. Describe the musical features and the sound you want it to make.
2. With a local Python 3 tool, compose the notes and render a simple WAV with [the bundled renderer](../scripts/render_music.py). Use a new output path in the host's artifact directory. Return the WAV using the host's audio player or a file link.
3. In a text-only host, provide a playable-by-hand sketch with tempo, instruments, and at least four measures of note names and durations.

For the WAV option, write a JSON score with the tempo in `bpm` and an array of `notes`. Each note has a zero-based starting `beat`, a `length` in beats, a MIDI `pitch` (60 is middle C), a `voice` (`keys`, `pluck`, or `bass`), and optional `velocity` greater than 0 and up to 1. Overlapping notes form chords or layers. Use silence between phrases and vary note lengths and velocities.

```json
{
  "bpm": 96,
  "notes": [
    {"beat": 0, "length": 0.75, "pitch": 64, "voice": "pluck"},
    {"beat": 0, "length": 2, "pitch": 45, "voice": "bass", "velocity": 0.55},
    {"beat": 1, "length": 0.75, "pitch": 67, "voice": "pluck"}
  ]
}
```

Run this command from the Skill's folder, using the actual score and output paths.

```sh
python3 scripts/render_music.py score.json theme.wav
```

Give the cue a title and briefly point out where the remembered details can be heard.
