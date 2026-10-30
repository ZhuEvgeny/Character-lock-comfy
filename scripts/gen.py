import json, sys, time, urllib.request, uuid, os, shutil
API = "http://127.0.0.1:8188"
OUT = r"D:\AI\ComfyUI\output"

CHAR = ("Mira, an original fictional young woman, late 20s, East Asian features, short asymmetric silver-white bob haircut with a single teal streak, "
        "thin straight eyebrows, small beauty mark under her left eye, wearing a mustard-yellow utility jacket over a black turtleneck, small silver hoop earrings")

def build(prompt, seed, w, h, prefix, ref=None, weight=0.9, end_at=1.0, steps=4):
    g = {
      "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": "flux1-schnell-Q4_K_S.gguf"}},
      "2": {"class_type": "DualCLIPLoader", "inputs": {"clip_name1": "clip_l.safetensors", "clip_name2": "t5xxl_fp8_e4m3fn.safetensors", "type": "flux", "device": "default"}},
      "3": {"class_type": "VAELoader", "inputs": {"vae_name": "ae.safetensors"}},
      "4": {"class_type": "EmptyLatentImage", "inputs": {"width": w, "height": h, "batch_size": 1}},
      "5": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["2", 0]}},
      "6": {"class_type": "CLIPTextEncode", "inputs": {"text": "", "clip": ["2", 0]}},
      "7": {"class_type": "FluxGuidance", "inputs": {"guidance": 3.5, "conditioning": ["5", 0]}},
      "8": {"class_type": "KSampler", "inputs": {"seed": seed, "steps": steps, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0,
             "model": ["17", 0] if ref else ["1", 0], "positive": ["7", 0], "negative": ["6", 0], "latent_image": ["4", 0]}},
      "9": {"class_type": "VAEDecode", "inputs": {"samples": ["8", 0], "vae": ["3", 0]}},
      "10": {"class_type": "SaveImage", "inputs": {"filename_prefix": prefix, "images": ["9", 0]}},
    }
    if ref:
        g.update({
          "13": {"class_type": "PulidFluxModelLoader", "inputs": {"pulid_file": "pulid_flux_v0.9.1.safetensors"}},
          "14": {"class_type": "PulidFluxEvaClipLoader", "inputs": {}},
          "15": {"class_type": "PulidFluxFaceNetLoader", "inputs": {"provider": "CPU"}},
          "16": {"class_type": "LoadImage", "inputs": {"image": ref}},
          "17": {"class_type": "ApplyPulidFlux", "inputs": {"weight": weight, "start_at": 0.0, "end_at": end_at, "model": ["1", 0],
                 "pulid_flux": ["13", 0], "eva_clip": ["14", 0], "face_analysis": ["15", 0], "image": ["16", 0]}},
        })
    return g

def queue(g):
    req = urllib.request.Request(API + "/prompt", data=json.dumps({"prompt": g, "client_id": str(uuid.uuid4())}).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))["prompt_id"]

def wait(pid, timeout=1800):
    t0 = time.time()
    while time.time() - t0 < timeout:
        h = json.load(urllib.request.urlopen(f"{API}/history/{pid}"))
        if pid in h:
            st = h[pid].get("status", {})
            if st.get("status_str") == "error":
                print("ERROR", json.dumps(st)[:3000]); return None
            for n in h[pid]["outputs"].values():
                for im in n.get("images", []):
                    return os.path.join(OUT, im.get("subfolder", ""), im["filename"])
        time.sleep(3)
    return None

if __name__ == "__main__":
    jobs = json.load(open(sys.argv[1], encoding="utf-8-sig"))
    for j in jobs:
        prompt = j["prompt"].replace("{CHAR}", CHAR)
        g = build(prompt, j["seed"], j["w"], j["h"], j["prefix"], j.get("ref"), j.get("weight", 0.9), j.get("end_at", 1.0))
        if j.get("save_graph"):
            json.dump(g, open(j["save_graph"], "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        t = time.time(); pid = queue(g); f = wait(pid)
        print(j["prefix"], j["seed"], "->", f, f"{time.time()-t:.0f}s", flush=True)

