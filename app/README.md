# Optional thin app layer

The core deliverable for this entry is the ComfyUI workflow under `../workflows/`.

If you add a UI later:

- Call ComfyUI via its HTTP API (`/prompt`, `/history`, `/view`)
- Expose: upload ref → run lock workflow → show up to 2 outputs
- Keep model weights local; do not hard-code closed partner APIs if targeting **Open Weights Only**

For tonight's deadline, a clear workflow + README + demo video is enough to submit; this folder can stay documentation-only.
