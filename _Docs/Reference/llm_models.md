# Available LLM Models (Artemis Endpoint)

The following models are available via the `https://llm.artemis-ai.ca/v1` endpoint.

## Recommended Models
- **deepseek-v3.1-671b-cloud**: Best all-rounder for reasoning and coding.
- **kimi-k2-thinking-cloud**: Specialized for complex thinking tasks.
- **groq-llama-3.3**: Ultra-fast responses (<1s).
- **qwen3-coder-480b-cloud**: Optimized for code generation.

## Full Model List
| Model ID | Provider | Notes |
| :--- | :--- | :--- |
| `deepseek-v3.1-671b-cloud` | OpenAI | Created: 1677610602 |
| `cogito-2.1-671b-cloud` | OpenAI | Created: 1677610602 |
| `gpt-oss-120b-cloud` | OpenAI | Created: 1677610602 |
| `qwen3-coder-480b-cloud` | OpenAI | Created: 1677610602 |
| `qwen3-vl-235b-cloud` | OpenAI | Created: 1677610602 |
| `glm-4.6-cloud` | OpenAI | Created: 1677610602 |
| `minimax-m2-cloud` | OpenAI | Created: 1677610602 |
| `kimi-k2-thinking-cloud` | OpenAI | Created: 1677610602 |
| `gemini-3-pro-preview` | OpenAI | Created: 1677610602 |
| `mistral-large-3-675b-cloud` | OpenAI | Created: 1677610602 |
| `nomic-embed-text` | OpenAI | Embedding Model |
| `deepseek-v3.1` | OpenAI | Alias |
| `kimi-k2-thinking` | OpenAI | Alias |
| `gpt-oss` | OpenAI | Alias |
| `qwen3-coder` | OpenAI | Alias |
| `qwen3-vl` | OpenAI | Alias |
| `glm-4.6` | OpenAI | Alias |
| `minimax-m2` | OpenAI | Alias |
| `cogito-2.1` | OpenAI | Alias |
| `mxbai-embed-large` | OpenAI | Embedding Model |

## Configuration
Ensure your `.env` file is set correctly:
```bash
LLM_API_BASE=https://llm.artemis-ai.ca/v1
LLM_API_KEY=sk-qTxNno4ic0_f18M6ZsYKxg
```
