# Fine-Tuning with LoRA or QLoRA

We'll use the `mlx-lm` package to fine-tune an LLM with low rank adaptation (LoRA) for a target task. The example also supports quantized LoRA fine-tuning and works with the following model families:

- Mistral
- Llama
- Phi2
- Mixtral
- Qwen2
- Gemma
- OLMo
- MiniCPM
- InternLM2

**Access our Fine-Tuned GitAI Model at [Hugging Face](https://huggingface.co/collections/YashJain/gitai-66716f5414a2d8e2b6d93bd9)**

## Data

For fine-tuning (`--train`), the data loader expects a `train.jsonl` and a `valid.jsonl` to be in the data directory. For evaluation (`--test`), the data loader expects a `test.jsonl` in the data directory.

Currently, `*.jsonl` files support three data formats: `chat`, `completions`, and `text`. Here are three examples of these formats:

`chat`:

```jsonl
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Hello."
    },
    {
      "role": "assistant",
      "content": "How can I assist you today."
    }
  ]
}
```

`completions`:

```jsonl
{
  "prompt": "What is the capital of France?",
  "completion": "Paris."
}
```

`text`:

```jsonl
{
  "text": "This is an example for the model."
}
```

Note, the format is automatically determined by the dataset. Keys in each line not expected by the loader will be ignored.

For the `chat` and `completions` formats, Hugging Face [chat templates](https://huggingface.co/blog/chat-templates) are used. This applies the model's chat template by default. If the model does not have a chat template, then Hugging Face will use a default.

If you are unsure of the format to use, the `chat` or `completions` are good to start with. For custom requirements on the format of the dataset, use the `text` format to assemble the content yourself.

## Fine-tune

To fine-tune a model use:

```shell
mlx_lm.lora \
    --model <path_to_model> \
    --train \
    --data <path_to_data> \
    --iters 600
```

The `--data` argument must specify a path to a `train.jsonl`, `valid.jsonl` when using `--train` and a path to a `test.jsonl` when using `--test`. (Default folder name 'data')

For example, to fine-tune a Qwen2 0.5B Instruct you can use `--model Qwen/Qwen2-0.5B-Instruct-MLX`.

Try using a smaller batch size with `--batch-size`. `2` or `1` will reduce memory consumption. This may slow things down a little, but will also reduce the memory use.

Reduce the number of layers to fine-tune with `--lora-layers` to `8` or `4`. This reduces the amount of memory needed for back propagation. It may also reduce the quality of the fine-tuned model if you are fine-tuning with a lot of data.

By default, the adapter config and weights are saved in `adapters/`. You can specify the output location with `--adapter-path`.

You can resume fine-tuning with an existing adapter with `--resume-adapter-file <path_to_adapters.safetensors>`.

## Evaluate

To compute test set perplexity use:

```shell
mlx_lm.lora \
    --model <path_to_model> \
    --adapter-path <path_to_adapters> \
    --data <path_to_data> \
    --test
```

## Generate

For generation use `mlx_lm.generate`:

```shell
mlx_lm.generate \
    --model <path_to_model> \
    --adapter-path <path_to_adapters> \
    --prompt "<your_model_prompt>"
```

## Fuse

To generate the fused model run:

```shell
mlx_lm.fuse --model <path_to_model>
```

This will by default load the adapters from `adapters/`, and save the fused model in the path `lora_fused_model/`. All of these are configurable.

To upload a fused model, supply the `--upload-repo` and `--hf-path` arguments to `mlx_lm.fuse`. The latter is the repo name of the original model, which is useful for the sake of attribution and model versioning.

For example, to fuse and upload a model derived from Qwen2-0.5B-Instruct-MLX, run:

```shell
mlx_lm.fuse \
    --model Qwen/Qwen2-0.5B-Instruct-MLX \
    --upload-repo YashJain/GitAI-Qwen2-0.5B-Instruct-MLX-v1 \
    --hf-path Qwen/Qwen2-0.5B-Instruct-MLX
```

## Contributing

We welcome contributions to improve and expand the Fine-Tuning with LoRA or QLoRA project. Here are some ways you can contribute:

### Implementing PyTorch and TensorFlow Versions

One of the key areas for contribution is implementing PyTorch and TensorFlow versions of the fine-tuning process. This will allow users to choose their preferred deep learning framework. Here are some steps to get started:

1. Create a new directory for each framework (e.g., `pytorch_implementation/` and `tensorflow_implementation/`).
2. Implement the core LoRA and QLoRA algorithms in each framework.
3. Adapt the data loading and processing steps to work with PyTorch and TensorFlow.
4. Implement the training, evaluation, and generation scripts for each framework.
5. Ensure compatibility with the same model families supported by the MLX version.
6. Write documentation and usage examples for each implementation.

### Other Contribution Areas

- Enhancing the existing MLX implementation with new features or optimizations.
- Adding support for more model families.
- Improving documentation and adding more detailed tutorials.
- Implementing additional fine-tuning techniques beyond LoRA and QLoRA.
- Creating benchmarks to compare performance across different frameworks.
- Adding more sophisticated evaluation metrics.
- Developing tools for easier model deployment and serving.

### Contributing Guidelines

1. Fork the repository and create a new branch for your feature or bug fix.
2. Follow the coding style and conventions used in the existing codebase.
3. Write clear, concise commit messages.
4. Add or update tests as necessary to cover your changes.
5. Update the documentation to reflect any changes in functionality or usage.
6. Submit a pull request with a clear description of your changes and their benefits.

