from datasets import load_dataset

load_dataset("openai/gsm8k", "main")
load_dataset("HuggingFaceTB/smol-smoltalk")
load_dataset("openai/openai_humaneval", split="test")
load_dataset("cais/mmlu", "all")
load_dataset("cais/mmlu", "auxiliary_train")
load_dataset("openai/gsm8k", "main")
load_dataset("openai/gsm8k", "socratic")
load_dataset("allenai/ai2_arc", "ARC-Easy")
load_dataset("allenai/ai2_arc", "ARC-Challenge")