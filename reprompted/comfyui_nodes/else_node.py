# ComfyUI Node for the 'else' shortcode
from reprompted.lib.shared import Reprompted

class RepromptedElseNode:
    """
    Node for the 'else' shortcode: Executes content if previous condition failed.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "content": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_else"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()
        self.do_else = False

    def do_else(self, content):
        if self.do_else:
            self.do_else = False
            return (self.reprompted.parse_alt_tags(content, None),)
        else:
            return ("",)

    def cleanup(self):
        self.do_else = False