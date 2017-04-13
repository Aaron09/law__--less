"""
Object for tracking top n sentences in chronological order for data visualization
"""
class Sentence(object):

	def __init__(self, text, highlight):
		self.text = text
		self.highlight = highlight