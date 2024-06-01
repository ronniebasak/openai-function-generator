import inspect
from typing import Any, get_type_hints, List, Union, Optional

def generate_tool_definition(func: Any, ignore_params: List[str] = []) -> dict:
    docstring = inspect.getdoc(func)    
    func_name = func.__name__
    
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)
    
    parameters = {
        "type": "object",
        "properties": {},
        "required": []
    }
    
    def get_json_type(py_type: Any) -> str:
        """Map Python type to JSON Schema type."""
        type_mapping = {
            int: "integer",
            str: "string",
            float: "number",
            bool: "boolean",
            list: "array",
            dict: "object",
            Any: "string"  # Default to string if type is Any
        }
        return type_mapping.get(py_type, "string")
    
    def handle_complex_type(py_type: Any) -> dict:
        """Handle complex types like Union, Optional, List, and Dict."""
        if hasattr(py_type, '__origin__'):
            origin = py_type.__origin__
            args = py_type.__args__
            
            if origin is Union:
                types = [get_json_type(arg) for arg in args]
                if len(types) == 2 and type(None) in args:
                    # Handle Optional
                    return {"type": types[0], "optional": True}
                return {"type": types}
            
            elif origin is list:
                return {"type": "array", "items": {"type": get_json_type(args[0])}}
            
            elif origin is dict:
                return {"type": "object", "additionalProperties": {"type": get_json_type(args[1])}}
        
        return {"type": get_json_type(py_type)}
    
    for param_name, param in sig.parameters.items():
        # Determine if the parameter is optional
        if param_name in ignore_params:
            continue
        if param.default is param.empty:
            optional = False
        else:
            optional = True
        
        # Get the type hint
        param_type = type_hints.get(param_name, Any)
        
        # Create the parameter definition
        param_def = handle_complex_type(param_type)
        param_def["description"] = f"Description for {param_name}"  # Placeholder description
        
        parameters["properties"][param_name] = param_def
        
        if not optional:
            parameters["required"].append(param_name)
    
    # Generate the tool definition
    tool_definition = {
        "type": "function",
        "function": {
            "name": func_name,
            "description": docstring,
            "parameters": parameters
        }
    }
    
    return tool_definition

if __name__ == "__main__":
    # Example usage
    def get_current_weather(self, location: str, unit: Optional[int] = "celsius", forecast_days: List[int] = [1, 2, 3]) -> None:
        """
        Get the current weather in a given location
        """
        pass

    print(generate_tool_definition(get_current_weather, ["self"]))