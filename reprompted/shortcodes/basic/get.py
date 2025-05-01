class Shortcode():
    def __init__(self,Reprompted):
        self.Reprompted = Reprompted
    def run_atomic(self, pargs, kwargs, context):
        if ("_var" in kwargs): parg = self.Reprompted.parse_alt_tags(kwargs["_var"],context)
        else: parg = pargs[0]

        if (parg in self.Reprompted.shorcode_user_vars):
            if ("after" in kwargs):
                self.Reprompted.shortcode_user_vars[parg] = str(self.Reprompted.shortcode_user_vars[parg]) + kwargs["after"]
            return(str(self.Reprompted.shortcode_user_vars[parg]))
        else:
            return("")