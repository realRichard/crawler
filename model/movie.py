from model import Model


class Movie(Model):
	'''
	电影类, 继承自 Model 类
	'''
	def __init__(self, form):
		self.title = form.get('title', '')
		self.quote = form.get('quote', '')
		self.cover_url = form.get('cover_url', '')
		self.ranking = form.get('ranking', 0)
		self.score = form.get('score', 0)
		self.number_of_comments = form.get('number_of_comments', 0)
		self.bd = form.get('bd', '')
		self.time = form.get('time', '')
		self.region = form.get('region', '')
		self.category = form.get('category', '')