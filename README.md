[简体中文](README.zh-CN.md)

# Memory Play

Turn what your agent remembers about you into something only you would get.

Memory Play is an agent skill for a creative break. Pick an activity or ask for a surprise. Your agent draws on its memories of you to make a portrait, a short film trailer, or something else with details you recognize.

## Install

Run the command and select Codex or Claude Code in the installer. The `-g` flag makes the skill available across your projects.

```sh
npx skills add nihaov/memory-play --skill memory-play -g
```

## Play

Try `memory-play list` to see every activity or `memory-play random` to draw one. You can also invoke `memory-play` and name the activity you want.

| Activity | What your agent creates |
| --- | --- |
| Ten Notes for Your Future | Ten pieces of life advice grounded in things you care about. |
| Your Inner World | An imagined scene that brings together a few things you've shared. |
| Your Week, the Documentary | A dryly funny trailer that finds a thread through your recent conversations. |
| My Portrait | A portrait that captures your habits and interests through pose, lighting, and personal details. |
| Give Me an Award | A deadpan ceremony for one real incident, complete with a darkly funny award citation. |
| My Theme Music | An original instrumental cue that turns remembered details into rhythm, melody, and sound. Hosts with Python can render a simple WAV when a music tool is unavailable. |
| A Parallel-Universe Side Quest | A fictional dispatch from the world where you followed through on an idea you once discussed. |

Your agent shows the chosen activity's prompt before it starts. For example, **Your Inner World** opens with this line.

> **Based on what you know about me, paint a picture of the world inside my head.**

Every activity starts from the agent's available memories of you. The current conversation can fill in details. If there is too little to work with, your agent can ask for a cue or two. In a text-only host, image activities return a ready-to-use image prompt.

## Update the activities

The public catalog lives in [`docs/catalog.json`](docs/catalog.json) and is [served by GitHub Pages](https://nihaov.github.io/memory-play/catalog.json). The skill fetches it when you open Memory Play and uses the bundled catalog if the online version is unavailable. The catalog contains public activity descriptions. Your own agent supplies the personal context.

To add an activity, give it a unique `id`, a bilingual `title` and `user_prompt`, and a `prompt` with creative direction. Catalog changes are available after Pages deploys. When the skill itself changes, run `npx skills update memory-play`.
