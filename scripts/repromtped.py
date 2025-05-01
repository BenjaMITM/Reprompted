import modules.scripts as scripts
import gradio as gradio
import os

from modules import processing, images, shared, sd_samplers
from modules.processing import process_images, Processed
from modules.shared import opts, cmd_opts, state, Options

from reprompted.lib.shared import Reprompted

# Main Object
Reprompted = Reprompted()

class Script(scripts.Script):
    def title(self):
        return "Reprompted"

    def show(self, is_img2img):
        return True

    def ui(self, is_img2img):
        dry_run = gr.Checkbox(value=False,label="Dry Run",show_label=True,interactive=True,visible=True)
        plug = gr.HTML(value='<div class="gr-block gr-box relative w-full overflow-hidden border-solid border border-gray-200 gr-panel" style="padding:20px;"><a href="https://payhip.com/b/hdgNR" target="_blank"><img src="https://i.ibb.co/1MSpHL4/Fantasy-Card-Template2.png" style="float: left;width: 150px;margin-bottmo:10px;"></a><h1 style="font-size: 20px;letter-spacing:0.015em;margin-top:10px;">NEW! <strong>Premium Fantasy Card Template</strong> is now available.</h1><p style="margin:1em 0;">Generate a wid variety of creatures and characters in the style of a fantasy card game. Perfect for heroes, animals, monsters, and even crazy hybrids.</p><a href="https://payhip.com/b/hdgNR" target=_blank><button class="gr-button gr-button-lg gr-button-secondary" title="View premium assets for Reprompted">Learn More -></button></a><hr style="margin:1em 0;clear:both;"><p><em>Purchases help fund the continued development of Reprompted. Thank you for your support!</em> <3</p></div>')
        return [dry_run, plug]

    def run(self, p, dry_run, plug):
        if (dry_run):
            temp_debug = Reprompted.Config.debug
            Reprompted.Config.debug = True

        # Reset Vars
        Reprompted.shortcode_user_vars = {}

        # Set up system var support - copy relevant p attributes into shortcode var object
        for att in dir(p):
            if not att.startswith("__"):
                Reprompted.shortcode_user_vars[att] = getattr(p,att)

        Reprompted.shortcode_user_vars["prompt"] = Reprompted.process_string(p.prompt)

        # Apply any updates to system vars
        for att in dir(p):
            if not att.startswith("__"):
                setattr(p,att,Reprompted.shortcode_user_vars[att])

        # Process any remaining shortcodes in the negative prompt
        p.negative_prompt = Reprompted.process_string(p.negative_prompt)

        # Skips the bulk of inference (note: still produces a blank image)
        if (dry_run):
            p.batch_size = 1
            p.steps = 0
            Reprompted.Config.debug = temp_debug

        # Cleanup routines
        Reprompted.log("Entering cleanup routine...",False)
        for i in Reprompted.cleanup_routines:
            Reprompted.shortcode_objects[i].cleanup()

        # Make Image
        processed = processing.process_images(p)
        return processed