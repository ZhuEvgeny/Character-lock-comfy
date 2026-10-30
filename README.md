# Character Lock (ComfyUI)

One reference image in → locked lookdev out (max 2 directions).
Open-source entry for [Open Source Higgsfield](https://comfy.org/open-source-higgsfield/).

**Author:** Evgeny ([@xx0618](https://x.com/xx0618)) · Fiverr: `xx0618`  
**License:** MIT  
**Repo:** https://github.com/ZhuEvgeny/Character-lock-comfy

## What it does

- Lock a character look from a single reference image (PuLID for Flux)
- Seed sweep → keep up to **2** creative directions
- Runs locally in ComfyUI on open weights (no closed API)

Public simplified workflow. Production / client settings stay private.

## Requirements

- Recent [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- GPU: works on **6GB** laptop at 640×640 with `--lowvram` (RTX 3060 Laptop tested)
- Custom nodes:
  - [ComfyUI_PuLID_Flux_ll](https://github.com/lldacing/ComfyUI_PuLID_Flux_ll)
  - Optional: ZhEnPromptTranslate (Chinese→English prompt). If missing, replace that node with plain English `CLIPTextEncode`.
- Models:
  - UNet (GGUF): `models/unet/flux1-schnell-Q4_K_S.gguf` via **UnetLoaderGGUF**
  - Dual CLIP: `clip_l.safetensors` + `t5xxl_fp8_e4m3fn.safetensors` (type `flux`)
  - VAE: `ae.safetensors`
  - PuLID: `models/pulid/pulid_flux_v0.9.1.safetensors`
  - EVA-CLIP: `models/clip/EVA02_CLIP_L_336_psz14_s6B.pt`

**Not used:** InstantID / IP-Adapter FaceID (not Flux-compatible here). **No ControlNet** in this public graph.

## Repo layout

```text
Character-lock-comfy/
├── LICENSE
├── README.md
├── workflows/
│   └── character_lock_v1.json
├── examples/          # add input_ref.png + output_dir_a.png (+ optional _b)
├── demo/              # add demo.mp4 ≤ 2 minutes
└── app/README.md
```

## Quick start

1. `git clone https://github.com/ZhuEvgeny/Character-lock-comfy.git`
2. Install `ComfyUI_PuLID_Flux_ll` into `custom_nodes`, restart ComfyUI
3. Place the models listed above in the usual folders
4. ComfyUI → **Load** → `workflows/character_lock_v1.json`
5. Drop a clear frontal face into **Load Image** → Queue Prompt
6. Seed sweep; keep **at most 2** directions

Suggested PuLID: weight `0.85`, start `0.0`, end `0.75`. If OOM: 512², weight `0.7`, end_at `0.6`, FaceNet device **CPU**.

## Demo & examples

- Stills: [`examples/`](examples/) (add your own licensed refs/outputs)
- Screen recording: [`demo/demo.mp4`](demo/demo.mp4) ≤ 2 min — reference → lock → two directions

## Challenge tags

`#OpenSourceHiggsfield` · `#ComfyUI`  
Categories: **Open Weights Only** · **Built with FLUX** (Flux Schnell core)

## Disclaimer

Ship only original or properly licensed likenesses. Do not use unlicensed celebrity / IP faces.
