# ComfyUI Node for the 'set' shortcode
from reprompted.lib.shared import Reprompted

class RepromptedSetNode:
    """
    Node for the 'set' shortcode: Sets a variable to a value, with options to append, prepend, or output.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "var_name": ("STRING", {"multiline": False, "default": ""}),
                "value": ("STRING", {"multiline": True, "default": ""}),
                "append": ("BOOLEAN", {"default": False}),
                "prepend": ("BOOLEAN", {"default": False}),
                "output": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "set_var"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()

    def set_var(self, var_name, value, append, prepend, output):
        user_vars = getattr(self.reprompted, "shortcode_user_vars", {})
        overrides = getattr(self.reprompted, "shortcode_objects", {}).get("override", None)
        # Check for override
        if overrides and hasattr(overrides, "shortcode_overrides") and var_name in overrides.shortcode_overrides:
            value = overrides.shortcode_overrides[var_name]
        # Type conversion
        try:
            if self.reprompted.is_float(value):
                value = float(value)
            elif self.reprompted.is_int(value):
                value = int(value)
        except Exception:
            pass
        # Set variable
        if append:
            user_vars[var_name] = str(user_vars.get(var_name, "")) + str(value)
        elif prepend:
            user_vars[var_name] = str(value) + str(user_vars.get(var_name, ""))
        else:
            user_vars[var_name] = value
        self.reprompted.log(f"Setting {var_name} to {value}")
        if output:
            return (str(value),)
        else:
            return ("",)