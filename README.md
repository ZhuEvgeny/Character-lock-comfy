# Character Lock

One reference image in. Up to two locked lookdev directions out.

Open-source entry for [Open Source Higgsfield](https://comfy.org/open-source-higgsfield/).

**Author:** Evgeny ([@xx0618](https://x.com/xx0618)) · Fiverr: `xx0618`  
**License:** [MIT](LICENSE)  
**Repo:** https://github.com/ZhuEvgeny/Character-lock-comfy

Character Lock is a local ComfyUI workflow for freelance lookdev. You give it one clear face. [PuLID for Flux](https://github.com/lldacing/ComfyUI_PuLID_Flux_ll) holds that identity on open-weight Flux.1 Schnell while you change the scene. Each queue returns one image. You keep at most two directions so a client can choose quickly.

## Lookdev boards

<table>
  <tr>
    <td align="center"><strong>Reference</strong><br><img src="examples/input_ref.png" alt="Reference board: frontal face, gray t-shirt, plain wall" width="220"></td>
    <td align="center"><strong>Direction A</strong><br><img src="examples/output_dir_a.png" alt="Direction A board: same character against a brick wall" width="220"></td>
    <td align="center"><strong>Direction B</strong><br><img src="examples/output_dir_b.png" alt="Direction B board: same character in a kitchen, navy hoodie" width="220"></td>
  </tr>
</table>

[`demo/demo.mp4`](demo/demo.mp4) is a 31-second slideshow of these three boards. Captions and matching prompts are in [`examples/README.md`](examples/README.md). How the files were made is in [How the examples were produced](#how-the-examples-were-produced).

## Load the workflow in ComfyUI

1. Install [ComfyUI](https://github.com/comfyanonymous/ComfyUI) **0.3.7 or newer**.
2. Install the two custom-node packs in [Custom nodes](#custom-nodes) and restart ComfyUI.
3. Download the models into the folders in [Models](#models).
4. Copy the reference into ComfyUI's input folder:

   ```bash
   cp examples/input_ref.png /path/to/ComfyUI/input/input_ref.png
   ```

5. In ComfyUI choose **Load** and open [`workflows/character_lock_v1.json`](workflows/character_lock_v1.json).
6. On the **Reference face** node, select `input_ref.png`, or drop in your own clear front-facing face.
7. **Queue Prompt**. One run saves one image. The filename prefix is `character_lock`.
8. For a second direction, edit **Positive prompt**, change the seed on **Sample**, and queue again. Keep two. The graph starts at seed `42` with the seed control set to `randomize` (the seed changes after every queue). Set that control to `fixed` when you want the same image again.

PuLID is already set to weight `0.85`, start `0.0`, end `0.75`. The sampler is Euler / simple, 4 steps, CFG `1`, 640×640, which is the Flux Schnell setting.

Tested on an RTX 3060 Laptop (6GB) at 640×640 with ComfyUI started as:

```bash
python main.py --lowvram
```

If the GPU runs out of memory: 512×512, PuLID weight `0.7`, end `0.6`, FaceNet provider **CPU**.

### Custom nodes

This graph loads `UnetLoaderGGUF` from [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) and the PuLID nodes from [ComfyUI_PuLID_Flux_ll](https://github.com/lldacing/ComfyUI_PuLID_Flux_ll).

If another pack also registers `ApplyPulidFlux`, disable it before installing this one. The usual conflict is [ComfyUI-PuLID-Flux](https://github.com/balazik/ComfyUI-PuLID-Flux). This workflow uses **PulidFluxFaceNetLoader** from `ComfyUI_PuLID_Flux_ll`.

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/city96/ComfyUI-GGUF.git
git clone https://github.com/lldacing/ComfyUI_PuLID_Flux_ll.git
cd ComfyUI_PuLID_Flux_ll
pip install -r requirements.txt
pip install facenet-pytorch --no-deps
```

Restart ComfyUI after the clones. On a portable Windows install, run the `pip` commands with that install's Python.

## Models

Weights stay on your machine. Place each file in the ComfyUI folder below.

| File | Folder | Download |
| --- | --- | --- |
| `flux1-schnell-Q4_K_S.gguf` | `models/unet/` | [city96/FLUX.1-schnell-gguf](https://huggingface.co/city96/FLUX.1-schnell-gguf/blob/main/flux1-schnell-Q4_K_S.gguf) |
| `clip_l.safetensors` | `models/clip/` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors) |
| `t5xxl_fp8_e4m3fn.safetensors` | `models/clip/` | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/t5xxl_fp8_e4m3fn.safetensors) |
| `ae.safetensors` | `models/vae/` | [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) — file `ae.safetensors`. Accept the license on that page first; the weight stays gated until you do. |
| `pulid_flux_v0.9.1.safetensors` | `models/pulid/` | [guozinan/PuLID](https://huggingface.co/guozinan/PuLID/blob/main/pulid_flux_v0.9.1.safetensors) |
| `EVA02_CLIP_L_336_psz14_s6B.pt` | `models/clip/` | [QuanSun/EVA-CLIP](https://huggingface.co/QuanSun/EVA-CLIP/blob/main/EVA02_CLIP_L_336_psz14_s6B.pt). The PuLID pack can also fetch this on first run. |

FaceNet weights download into the PyTorch cache the first time the **FaceNet (CPU)** node runs.

The positive prompt already on the graph is:

> portrait of an East Asian woman, soft studio light, clean background, sharp detail

## How the examples were produced

`examples/input_ref.png`, `examples/output_dir_a.png`, and `examples/output_dir_b.png` are an original fictional character: a short black bob, a brick-wall direction, and a kitchen direction. They were generated with Grok Image as lookdev boards for this entry.

[`demo/demo.mp4`](demo/demo.mp4) is a 31-second, 1280×720 slideshow of those same boards: title, reference, direction A, direction B, repository URL. The picture frames are the PNGs in `examples/`.

Images you generate yourself come from [`workflows/character_lock_v1.json`](workflows/character_lock_v1.json). [`scripts/gen.py`](scripts/gen.py) queues that same graph on a ComfyUI that is already running. A two-direction sample is [`scripts/jobs.example.json`](scripts/jobs.example.json). Copy `examples/input_ref.png` into ComfyUI's `input/` folder first:

```bash
python scripts/gen.py scripts/jobs.example.json
```

`COMFYUI_URL` overrides the default `http://127.0.0.1:8188`. `COMFYUI_OUTPUT` is your ComfyUI `output` folder, and the script uses it only when printing the saved path. The helper talks to that local ComfyUI server.

## Repo layout

```text
Character-lock-comfy/
├── LICENSE
├── README.md
├── SUBMISSION.md                 # pitch and judge map
├── workflows/
│   └── character_lock_v1.json    # the graph to load
├── examples/                     # reference + two direction boards
├── demo/
│   └── demo.mp4                  # 31s slideshow
├── scripts/
│   ├── gen.py                    # local ComfyUI queue helper
│   └── jobs.example.json
└── app/README.md                 # notes for a future local UI
```

## Contest

`#OpenSourceHiggsfield` · `#ComfyUI`

**Open Weights Only.** The core model is open-weight Flux.1 Schnell (`flux1-schnell-Q4_K_S.gguf`). Identity is PuLID with FaceNet. The queue runs on the machine where ComfyUI is installed.

The contest's **Built with FLUX** bonus is for a workflow whose core model is FLUX 3. This workflow's core model is Flux.1 Schnell.

The window on the [contest page](https://comfy.org/open-source-higgsfield/) closes **November 3, 2026, 9:00am PT**. Paste-ready wording for the entry lives in [`SUBMISSION.md`](SUBMISSION.md).

## Likeness

Use an original character, or a likeness you have rights to use. The boards in this repo are a fictional character made for the entry.

Weight files keep their own licenses. Flux.1 Schnell is Apache-2.0. The workflow and scripts in this repository are [MIT](LICENSE).
