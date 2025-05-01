# ComfyUI Node for the 'eval' shortcode
from reprompted.lib.shared import Reprompted

class RepromptedEvalNode:
    """
    Node for the 'eval' shortcode: Evaluates a Python expression from the content string.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "expression": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "evaluate"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()

    def evaluate(self, expression):
        try:
            result = str(eval(expression))
        except Exception as e:
            result = f"Eval error: {e}"
        return (result,)