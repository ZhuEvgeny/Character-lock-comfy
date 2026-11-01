# App

Character Lock ships as the ComfyUI workflow in [`../workflows/character_lock_v1.json`](../workflows/character_lock_v1.json). This folder is a note for a later interface. There is no UI code here yet.

A local UI can call ComfyUI's HTTP API:

- `POST /prompt` queues the graph
- `GET /history/{prompt_id}` waits for the image
- `GET /view` returns the saved file

Three actions are enough: upload a reference, run the lock, show up to two saved directions. Keep the model weights on the machine that runs ComfyUI so the entry stays **Open Weights Only**.

[`../scripts/gen.py`](../scripts/gen.py) is the command-line way to queue the graph today. Setup steps are in the [README](../README.md).
