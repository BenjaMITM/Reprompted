# ComfyUI Node for the 'random' shortcode
from reprompted.lib.shared import Reprompted
import random

class RepromptedRandomNode:
    """
    Node for the 'random' shortcode: Generates a random integer or float between min and max.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "min_value": ("FLOAT", {"default": 0.0}),
                "max_value": ("FLOAT", {"default": 100.0}),
                "as_float": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "random_value"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()

    def random_value(self, min_value, max_value, as_float):
        if as_float:
            return (random.uniform(float(min_value), float(max_value)),)
        else:
            return (float(random.randint(int(min_value), int(max_value))),)