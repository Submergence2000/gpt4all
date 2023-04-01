from datasets import load_dataset
dataset = load_dataset("nomic-ai/gpt4all_prompt_generations")
for split, dataset in dataset.items():
    dataset.to_json(f"data/squad-{split}.jsonl")