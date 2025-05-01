class Shortcode:
    """Use within [switch] to run different logic blocks depending on the value of a var."""
    def __init__(self,Reprompted):
        self.Reprompted = Reprompted

    def run_block(self, pargs, kwargs, context, content):
        _var = self.Reprompted.shortcode_objects["switch"].switch_var

        # self.Reprompted.log(pargs[0])

        if (_var in self.Reprompted.shortcode_user_vars):
            # Default case
            if len(pargs) == 0:
                return(self.Reprompted.parse_alt_tags(content, context))
            
            # Matching case
            elif self.Reprompted.is_equal(self.Reprompted.shortcode_user_vars[_var],pargs[0]):
                self.Reprompted.shortcode_objects["switch"].switch_var = ""
                return(self.Reprompted.parse_alt_tags(content, context))
        
        return("")