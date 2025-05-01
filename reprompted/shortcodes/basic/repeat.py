class Shortcode:
    """Returns the content of an arbitrary number of times"""
    def __init__(self,Reprompted):
        self.Reprompted = Reprompted
    def run_block(self,pargs,kwargs,context,content):
        final_string = ""

        if ("_times" in kwargs): _times = self.Reprompted.parse_alt_tags(kwargs["_times"],context)
        else: _times = pargs[0]

        for x in range(0, int(_times) + 1):
            final_string += self.Reprompted.parse_alt_tags(content,context)

            return(final_string)