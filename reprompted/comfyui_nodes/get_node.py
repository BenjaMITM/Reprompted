# ComfyUI Node for the 'get' shortcode
from reprompted.lib.shared import Reprompted

class RepromptedGetNode:
    """
    Node for the 'get' shortcode: Retrieves a variable value, optionally appending a string after.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "var_name": ("STRING", {"multiline": False, "default": ""}),
                "after": ("STRING", {"multiline": False, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_var"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()

    def get_var(self, var_name, after):
        # Mimic the shortcode logic
        parg = var_name
        if hasattr(self.reprompted, "parse_alt_tags"):
            parg = self.reprompted.parse_alt_tags(var_name, None)
        val = self.reprompted.shortcode_user_vars.get(parg, "")
        if after:
            val = str(val) + after
            self.reprompted.shortcode_user_vars[parg] = val
        return (str(val),)