import glob
import random
import os

class Shortcode():
    def __init__(self,Reprompted):
        self.Reprompted = Reprompted
    
    def run_atomic(self, pargs, kwargs, context):
        file_string = pargs[0]
        # Relative path
        if (file_string[0] == "."):
            path = os.path.dirname(context) + "/" + file_string + self.Reprompted.Config.txt_format
            # Absolute path
        else: path = self.Reprompted.Config.template_directory + "/" + file_string + self.Reprompted.Config.txt_format

        files = glob.glob(path)
        file = random.choice(files)

        self.Reprompted.log(f"Loading file: {file}")

        file_contents = open(file).read().replace('\n', self.Reprompted.Config.syntax.n_temp)

        self.Reprompted.shortcode_objects["else"].do_else = False
        return(self.Reprompted.shortcode_parser.parse(file_contents,path))