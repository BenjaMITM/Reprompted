class Shortcode():
    """Houses a comment that does not affect your final prompt."""
    def __init__(self,Reprompted):
        self.Reprompted = Reprompted
    def run_atomic(self, pargs, kwargs, context):
        return("")
        