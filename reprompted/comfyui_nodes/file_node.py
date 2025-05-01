# ComfyUI Node for the 'file' shortcode
from reprompted.lib.shared import Reprompted
import glob
import random
import os

class RepromptedFileNode:
    """
    Node for the 'file' shortcode: Loads a random file matching the pattern and returns its contents.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_string": ("STRING", {"multiline": False, "default": "filename"}),
                "context": ("STRING", {"multiline": False, "default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_file"
    CATEGORY = "Reprompted/Shortcodes"

    def __init__(self):
        self.reprompted = Reprompted()

    def load_file(self, file_string, context):
        # Relative path
        if file_string.startswith("."):
            path = os.path.dirname(context) + "/" + file_string + self.reprompted.Config.txt_format
        else:
            path = self.reprompted.Config.template_directory + "/" + file_string + self.reprompted.Config.txt_format
        files = glob.glob(path)
        if not files:
            return ("",)
        file = random.choice(files)
        self.reprompted.log(f"Loading file: {file}")
        try:
            file_contents = open(file).read().replace('\n', self.reprompted.Config.syntax.n_temp)
        except Exception as e:
            return (f"File load error: {e}",)
        if "else" in getattr(self.reprompted, "shortcode_objects", {}):
            self.reprompted.shortcode_objects["else"].do_else = False
        return (self.reprompted.shortcode_parser.parse(file_contents, path),)