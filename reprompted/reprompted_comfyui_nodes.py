# Reprompted ComfyUI Custom Nodes

from reprompted.lib.shared import Reprompted
from aiohttp import web
from server import PromptServer

class RepromptedProcessString:
    """
    Node for processing a string using Reprompted's shortcode parser.
    """
    def __init__(self):
        self.reprompted = Reprompted()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_string": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "Reprompted"

    def process(self, input_string):
        output = self.reprompted.process_string(input_string)
        return (output,)

class RepromptedParseAltTags:
    """
    Node for parsing alt tags in a string using Reprompted.
    """
    def __init__(self):
        self.reprompted = Reprompted()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_string": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "parse"
    CATEGORY = "Reprompted"

    def parse(self, input_string):
        output = self.reprompted.parse_altt_tags(input_string)
        return (output,)

class RepromptedRegisterShortcode:
    """
    Node for registering a custom shortcode with Reprompted.
    """
    def __init__(self):
        self.reprompted = Reprompted()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "shortcode_name": ("STRING", {"multiline": False, "default": "custom"}),
                "handler_code": ("STRING", {"multiline": True, "default": "def handler(pargs, kwargs, context, content):\n    return content"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "register"
    CATEGORY = "Reprompted"

    def register(self, shortcode_name, handler_code):
        # Dynamically register a shortcode handler (for demonstration, eval is used; in production, use safer alternatives)
        local_vars = {}
        exec(handler_code, {}, local_vars)
        handler = local_vars.get("handler")
        if handler:
            self.reprompted.shortcode_parser.register(handler, shortcode_name)
            return (f"Registered shortcode: {shortcode_name}",)
        return ("Failed to register shortcode.",)

class RepromptedValidatePrompt:
    """
    Node for validating a prompt string using Reprompted utilities.
    """
    def __init__(self):
        self.reprompted = Reprompted()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt_string": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "validate"
    CATEGORY = "Reprompted"

    def validate(self, prompt_string):
        # Example validation: check if prompt is non-empty and contains no forbidden shortcodes
        if prompt_string.strip() and "forbidden" not in prompt_string:
            return (True,)
        return (False,)

class RepromptedFormatPrompt:
    """
    Node for formatting a prompt string using Reprompted utilities.
    """
    def __init__(self):
        self.reprompted = Reprompted()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt_string": ("STRING", {"multiline": True, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "format"
    CATEGORY = "Reprompted"

    def format(self, prompt_string):
        # Example formatting: strip and normalize whitespace
        return (" ".join(prompt_string.split()),)

# --- API Route Example for Reprompted ---
@PromptServer.instance.routes.get("/reprompted/health")
async def get_reprompted_health(request):
    return web.json_response({"status": "ok"})

# Node registration
NODE_CLASS_MAPPINGS = {
    "RepromptedProcessString": RepromptedProcessString,
    "RepromptedParseAltTags": RepromptedParseAltTags,
    "RepromptedRegisterShortcode": RepromptedRegisterShortcode,
    "RepromptedValidatePrompt": RepromptedValidatePrompt,
    "RepromptedFormatPrompt": RepromptedFormatPrompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RepromptedProcessString": "Reprompted: Process String",
    "RepromptedParseAltTags": "Reprompted: Parse Alt Tags",
    "RepromptedRegisterShortcode": "Reprompted: Register Shortcode",
    "RepromptedValidatePrompt": "Reprompted: Validate Prompt",
    "RepromptedFormatPrompt": "Reprompted: Format Prompt"
}