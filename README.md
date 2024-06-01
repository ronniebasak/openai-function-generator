# OpenAI Function Generator

This project provides a tool to generate JSON schema definitions for OpenAI functions.

## Installation

```bash
pip install openai-tool-generator
```

## Usage

```python
from openai_tool_generator.generate_tool_definition import generate_tool_definition

def sample_func(a: int, b: Optional[str] = "default", c: List[float] = [1.0, 2.0]) -> None:
    """
    Sample function for testing
    """
    pass

definition = generate_tool_definition(sample_func)
print(definition)
```