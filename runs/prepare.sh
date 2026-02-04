
export NANOCHAT_BASE_DIR="./.cache/nanochat"

uv run prepare_dataset.py

python -m scripts.base_eval --eval "core,sample" --hf-path openai-community/gpt2
python -m tasks.spellingbee