# ComfyUI Node for the 'choose' shortcode
from reprompted.lib.shared import Reprompted
import random

class RepromptedChooseNode:
    """
    Node for the 'choose' shortcode: Returns one of multiple options, delimited by newline or vertical pipe.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "options": ("STRING", {"multiline": True, "default": "Option 1|Option 2|Option 3"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "choose"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()

    def choose(self, options):
        # Split options by pipe or newline, remove empty entries
        parts = [part for part in options.replace("\n", "|").split("|") if part.strip()]
        if not parts:
            return ("",)
        choice = random.choice(parts)
        return (self.reprompted.parse_alt_tags(choice, None),)