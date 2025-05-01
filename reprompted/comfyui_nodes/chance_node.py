# ComfyUI Node for the 'chance' shortcode
from reprompted.lib.shared import Reprompted

class RepromptedChanceNode:
    """
    Node for the 'chance' shortcode: Returns the content if the number you passed is greater than or equal to a random number between 1 and 100.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "probability": ("FLOAT", {"default": 50.0, "min": 0, "max": 100}),
                "content": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "chance"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()

    def chance(self, probability, content):
        # Mimic the shortcode logic
        import random
        if int(float(probability)) >= random.randint(1, 100):
            # Reset 'else' state if needed
            if "else" in getattr(self.reprompted, "shortcode_objects", {}):
                self.reprompted.shortcode_objects["else"].do_else = False
            return (self.reprompted.parse_alt_tags(content, None),)
        else:
            if "else" in getattr(self.reprompted, "shortcode_objects", {}):
                self.reprompted.shortcode_objects["else"].do_else = True
            return ("",)