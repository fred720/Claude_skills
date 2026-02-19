# Purpose

Create a new Ollama CLI agent to execute the command.

## Variables

DEFAULT_MODEL: gpt-oss
HEAVY_MODEL: deepseek-v3.2:cloud
BASE_MODEL: gpt-oss
FAST_MODEL: deepseek-v3.2:cloud

## Instructions

- Before executing the command, run `ollama --help` to understand the command and its options.
- Always use interactive mode (so leave off -p and use positional prompt if needed)
- For the -m (model) argument, use the DEFAULT_MODEL if not specified. If 'fast' is requested, use the FAST_MODEL. If 'heavy' is requested, use the HEAVY_MODEL.
- Always run with `--dangerously-bypass-approvals-and-sandbox`