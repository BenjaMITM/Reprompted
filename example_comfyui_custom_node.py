# Example ComfyUI Custom Node Extension

class Example:
    """
    Example node for ComfyUI custom extension.
    This node demonstrates input handling, lazy evaluation, and basic image processing.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
        Define input fields for the node.
        """
        return {
            "required": {
                "image": ("IMAGE",),
                "int_field": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 4096,
                    "step": 64,
                    "display": "number",
                    "lazy": True
                }),
                "float_field": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001,
                    "display": "number",
                    "lazy": True
                }),
                "print_to_screen": (["enable", "disable"],),
                "string_field": ("STRING", {
                    "multiline": False,
                    "default": "Hello World!",
                    "lazy": True
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "test"
    CATEGORY = "Example"

    def check_lazy_status(self, image, string_field, int_field, float_field, print_to_screen):
        """
        Specify which lazy fields need evaluation based on current input values.
        """
        if print_to_screen == "enable":
            return ["int_field", "float_field", "string_field"]
        else:
            return []

    def test(self, image, string_field, int_field, float_field, print_to_screen):
        if print_to_screen == "enable":
            print(f"""Your input contains:\n    string_field: {string_field}\n    int_field: {int_field}\n    float_field: {float_field}\n""")
        # Example processing: invert image
        image = 1.0 - image
        return (image,)

# --- Additional Node Example: Generation Control Node ---
class GenerationControl:
    """
    Node to demonstrate controlling generation process parameters.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "steps": ("INT", {"default": 20, "min": 1, "max": 150, "step": 1, "display": "number"}),
                "guidance": ("FLOAT", {"default": 7.5, "min": 1.0, "max": 20.0, "step": 0.1, "display": "number"}),
            },
        }

    RETURN_TYPES = ("INT", "FLOAT")
    FUNCTION = "set_params"
    CATEGORY = "Generation Control"

    def set_params(self, steps, guidance):
        # This node outputs generation parameters for downstream nodes
        return (steps, guidance)

# --- API Route Example ---
from aiohttp import web
from server import PromptServer

@PromptServer.instance.routes.get("/hello")
async def get_hello(request):
    return web.json_response({"message": "hello"})

# Node registration
NODE_CLASS_MAPPINGS = {
    "Example": Example,
    "GenerationControl": GenerationControl
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Example": "Example Node",
    "GenerationControl": "Generation Control Node"
}