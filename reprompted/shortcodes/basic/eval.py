class Shortcode():
    def __init__(self,Reprompted):
        self.Reprompted = Reprompted
    def run_block(self, pargs, kwargs, context, content):
        return str(eval(content))