from mlx_lm import load, generate

model, tokenizer = load("YashJain/GitAI-gemma-2b")

prompt = "How git commit hash are generated"

response = generate(model, tokenizer, prompt=prompt, verbose=True, max_tokens=100)
