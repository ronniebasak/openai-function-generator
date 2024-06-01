from typing import List, Optional
import unittest
from openai_tool_generator.generate_tool_definition import generate_tool_definition

class TestGenerateToolDefinition(unittest.TestCase):
    def test_generate_tool_definition(self):
        def sample_func(a: int, b: Optional[str] = "default", c: List[float] = [1.0, 2.0]) -> None:
            """
            Sample function for testing
            """
            pass
        
        expected_output = {
            "type": "function",
            "function": {
                "name": "sample_func",
                "description": "Sample function for testing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "integer",
                            "description": "Description for a"
                        },
                        "b": {
                            "type": "string",
                            "description": "Description for b"
                        },
                        "c": {
                            "type": "array",
                            "items": {
                                "type": "number"
                            },
                            "description": "Description for c"
                        }
                    },
                    "required": ["a"]
                }
            }
        }
        
        self.assertEqual(generate_tool_definition(sample_func), expected_output)

if __name__ == '__main__':
    unittest.main()