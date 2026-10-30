# Submission notes — Open Source Higgsfield

**Deadline:** October 30 · 9am PT (Shanghai 10/31 00:00)  
**Form:** https://comfy.org/open-source-higgsfield/  
**Repo:** https://github.com/ZhuEvgeny/Character-lock-comfy

## Paste-ready fields

**One-line pitch**  
Character Lock: one reference face → PuLID+Flux Schnell lookdev, seed-sweep to at most two client-ready directions — fully open weights in ComfyUI.

**Longer description**  
Freelance lookdev needs a locked character, not prompt roulette. This public ComfyUI workflow takes a single reference image, applies PuLID for Flux on a GGUF Flux Schnell UNet, and keeps creative variation to ≤2 directions so clients decide fast. No InstantID/IP-Adapter FaceID (Flux path), no ControlNet, no closed APIs. Includes workflow JSON, example stills of an original fictional character, and a local generation helper script.

**Categories to tick**  
- Open Weights Only  
- Built with FLUX (Flux Schnell core)

**What judges should open**  
1. `README.md` + `workflows/character_lock_v1.json`  
2. `examples/input_ref.png` → `output_dir_a.png` / `output_dir_b.png`  
3. `demo/demo.mp4` once recorded

## Still todo before submit

- [ ] Record and commit `demo/demo.mp4` (≤2 min)
- [ ] Fill the official submission form with this repo URL


