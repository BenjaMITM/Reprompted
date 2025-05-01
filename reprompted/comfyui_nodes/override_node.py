# ComfyUI Node for the 'override' shortcode
from reprompted.lib.shared import Reprompted

class RepromptedOverrideNode:
    """
    Node for the 'override' shortcode: Force variable(s) to hold a pre-determined value the rest of the run.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "var_name": ("STRING", {"multiline": False, "default": ""}),
                "value": ("STRING", {"multiline": False, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "override_var"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()
        self.shortcode_overrides = {}

    def override_var(self, var_name, value):
        self.shortcode_overrides[var_name] = value
        return ("")

    def cleanup(self):
        self.shortcode_overrides.clear()