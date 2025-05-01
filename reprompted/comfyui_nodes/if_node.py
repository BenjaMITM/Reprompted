# ComfyUI Node for the 'if' shortcode
from reprompted.lib.shared import Reprompted

class RepromptedIfNode:
    """
    Node for the 'if' shortcode: Conditional logic based on variable values.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "var_name": ("STRING", {"multiline": False, "default": ""}),
                "expected_value": ("STRING", {"multiline": False, "default": ""}),
                "not_flag": ("BOOLEAN", {"default": False}),
                "content": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "if_condition"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()

    def if_condition(self, var_name, expected_value, not_flag, content):
        is_true = True
        user_vars = getattr(self.reprompted, "shortcode_user_vars", {})
        val = user_vars.get(var_name, "")
        if str(val) != str(expected_value):
            is_true = False
        if ((is_true and not not_flag) or (not_flag and not is_true)):
            if "else" in getattr(self.reprompted, "shortcode_objects", {}):
                self.reprompted.shortcode_objects["else"].do_else = False
            return (self.reprompted.parse_alt_tags(content, None),)
        else:
            if "else" in getattr(self.reprompted, "shortcode_objects", {}):
                self.reprompted.shortcode_objects["else"].do_else = True
            return ("",)