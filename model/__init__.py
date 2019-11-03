class Model(object):
	'''
	基类, 提供打印方法
	'''
	def __repr__(self):
		# 实例的直接父类名
		name = self.__class__.__name__
		# 将实例对象自己拥有的属性转为 k, v 对形式的 tuple
		properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
		# 注意换行符的斜杠, 别弄反了, 
		s = '\n{}\n< {} >'.format(name, '\n'.join(properties))
		return s