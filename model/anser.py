from model import Model


class Anser(Model):
	'''
	Anser 类, 继承自 Model 类
	'''
	def __init__(self, form):
		self.link = form.get('link', '')
		self.question = form.get('question', '')
		self.agree = form.get('agree', 0)
		self.author = form.get('author', '')
		self.anser = form.get('anser', '')
		self.comments = form.get('comments', 0)
