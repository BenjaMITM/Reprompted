import random
class Shortcode():
	"""Returns one of multiple options, delimited by newline or vertical pipe"""
	def __init__(self,Reprompted):
		self.Reprompted = Reprompted
	def run_block(self, pargs, kwargs, context, content):
		parts = content.replace(self.Reprompted.Config.syntax.n_temp,"|").split("|")
		# Remove empty lines
		parts = list(filter(None, parts))
		# self.Reprompted.log(f"List of options: {parts}")
		return self.Reprompted.parse_alt_tags(random.choice(parts),context)