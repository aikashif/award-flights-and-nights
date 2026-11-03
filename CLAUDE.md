# Project instructions

## Video and animation requests

When the user asks for a video, animation, film, short, promo, explainer or any animated clip, use the video skills in `.claude/skills/` directly. Do not ask whether to use them.

- **lemo-opuscar** (Lemo-Opuscar): use for a styled short film, or when the user names an art style (oil painting, watercolor, ukiyo-e, satellite briefing, and so on). Also use when the user has no style yet: it helps them choose one.
- **hyperframes** (HyperFrames): use for motion graphics, UI or product promos, title cards, charts and data animations, captions, overlays, slideshows and vertical social clips. Read `hyperframes` first. It sends you to `hyperframes-cli`, `hyperframes-registry` and `media-use` when needed.
- If the request fits both, use lemo-opuscar for an artistic film and hyperframes for a clean, designed video.

Requirements: Node 20+, ffmpeg 7+ (Lemo-Opuscar needs 7+), Python 3.11+.

Sources (to update, copy the folders again):
- Lemo-Opuscar: https://github.com/lemomo-ai/lemo-opuscar, folder `plugin/skills/lemo-opuscar` (MIT)
- HyperFrames: https://github.com/heygen-com/hyperframes, folders `skills/hyperframes`, `skills/hyperframes-cli`, `skills/hyperframes-registry`, `skills/media-use` (Apache-2.0)
