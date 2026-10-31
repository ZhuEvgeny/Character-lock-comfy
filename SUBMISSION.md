# Submission notes — Open Source Higgsfield

**Window:** closes November 3, 2026, 9:00am PT  
**Contest page:** https://comfy.org/open-source-higgsfield/  
**Repo:** https://github.com/ZhuEvgeny/Character-lock-comfy  
**Form:** submitted with this repository URL

## Paste-ready fields

**One-line pitch**  
Character Lock: one reference face, PuLID on Flux.1 Schnell, one image per queue, keep at most two lookdev directions. Open weights in ComfyUI.

**Longer description**  
Freelance lookdev needs a locked character. This ComfyUI workflow takes a single reference image, holds identity with PuLID for Flux (FaceNet loader) on a GGUF Flux.1 Schnell UNet, and asks you to keep at most two directions so a client can decide. Each queue saves one image. The repo includes the workflow, a local queue helper, lookdev boards of an original fictional character (Grok Image), and a 31-second slideshow of those boards.

**Category**  
Open Weights Only. Core model: Flux.1 Schnell Q4_K_S GGUF. The contest's Built with FLUX bonus asks for FLUX 3 as the core model; this graph uses Flux.1 Schnell.

## What to open

1. [`README.md`](README.md) — what it is, how to load the graph, models, how the boards were made
2. [`workflows/character_lock_v1.json`](workflows/character_lock_v1.json) — ComfyUI → Load
3. [`examples/input_ref.png`](examples/input_ref.png), [`output_dir_a.png`](examples/output_dir_a.png), [`output_dir_b.png`](examples/output_dir_b.png)
4. [`demo/demo.mp4`](demo/demo.mp4) — 31s, 1280×720

## Shipped

- [x] Public workflow, MIT license, setup steps in the README
- [x] `demo/demo.mp4` (31 seconds, under the 2-minute limit)
- [x] Example boards in `examples/`
- [x] Entry form submitted with this repo URL
