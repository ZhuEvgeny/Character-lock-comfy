# Character Lock (ComfyUI)

One reference image in → locked lookdev out (max 2 directions).  
Open-source entry for [Open Source Higgsfield](https://comfy.org/open-source-higgsfield/).

**Author:** Evgeny ([@xx0618](https://x.com/xx0618)) · Fiverr: `xx0618`  
**License:** MIT  
**Repo:** https://github.com/ZhuEvgeny/Character-lock-comfy

## What it does

- Lock a character look from a single reference image
- Seed sweep → keep up to **2** creative directions
- Runs locally in ComfyUI (open-weights friendly path)

This is a **simplified public** workflow. Production / client settings stay private.

## Requirements

- Recent [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- GPU VRAM: document yours after first successful run (e.g. 12GB+)
- Models (fill in exact names you ship with the workflow):
  - Base checkpoint: `<!-- e.g. flux1-dev / your pick -->`
  - Optional LoRAs / IP-Adapter / face lock nodes: `<!-- list -->`
- Custom nodes (if any): `<!-- list GitHub links -->`

## Repo layout

```text
Character-lock-comfy/
├── LICENSE
├── README.md
├── workflows/
│   └── character_lock_v1.json
├── examples/
│   ├── input_ref.png
│   ├── output_dir_a.png
│   └── output_dir_b.png
├── demo/
│   └── demo.mp4          # ≤ 2 minutes
└── app/
    └── README.md         # optional: Comfy API / thin UI notes
```

## Quick start

1. Clone this repo  
   `git clone https://github.com/ZhuEvgeny/Character-lock-comfy.git`
2. Open ComfyUI → **Load** → `workflows/character_lock_v1.json`
3. Install any missing custom nodes listed above, restart ComfyUI
4. Place required models in the usual ComfyUI folders
5. Drop your reference into the **Load Image** node → **Queue Prompt**
6. Compare seed variants → keep at most **2** directions

Suggested starting values (tune per model): seed sweep range, CFG, steps — fill after your first export.

## Demo

See [`demo/demo.mp4`](demo/demo.mp4): reference → lock → two directions.  
Still examples: [`examples/`](examples/).

## Design notes

- One locked lookdev path beats prompt roulette for recurring characters
- Cap at 2 directions so clients decide faster (same idea as my public notes on X)

## Challenge tags

`#OpenSourceHiggsfield` · `#ComfyUI`  
Categories to consider: **Open Weights Only** (if no closed APIs) and/or **Built with FLUX** (if FLUX is the core model).

## Disclaimer

Example images must be original or properly licensed. Do not ship unlicensed likenesses or IP.
