import requests
from pyquery import PyQuery as pq
import os

from model.movie import Movie

from utils import log


def movie_from_item(item):
	e = pq(item)
	# 保存电影信息
	form = {}
	form['title'] = e('.title').text()
	form['quote'] = e('.inq').text()
	form['cover_url'] = e('img').attr('src')
	form['score'] = e('.rating_num').text()
	form['ranking'] = e('em').text()
	# 实例化一个 movie 类
	movie = Movie(form)
	return movie


def cached_url(url):
	'''
	把资源缓存到本地, 这样之后就不用每次执行网络请求
	节省时间
	'''
	folder = 'cached'
	filename = url.split('=', 1)[-1] + '.html'
	path = os.path.join(folder, filename)
	# 如果本地有缓存, 直接读取返回
	if os.path.exists(path):
		with open(path, 'rb') as f:
			s = f.read()
			log('缓存返回')
			return s
	else:
		# 如果本地没有缓存
		# 判断是否有此目录, 没有就创建
		if not os.path.exists(folder):
			os.makedirs(folder)
		# 执行网络请求, 并且把页面写入本地
		log('开始执行请求')
		r = requests.get(url)
		with open(path, 'wb') as f:
			# 写入文件保存
			log('写入文件缓存')
			f.write(r.content)
		return r.content
		

def movies_from_url(url):
	# 缓存
	page = cached_url(url)
	# 返回一个 pyquery 对象
	e = pq(page)
	# 使用 jquery 语法, 得到 25 个div
	items = e('.item')
	# 用函数解析每个div, 组一个数组返回, 里面是 movie object
	movies = [movie_from_item(i) for i in items]
	return movies
	

def main():
	# 'https: // movie.douban.com/top250'
	# 豆瓣网直接复制下来的 url 有病, invalidURL  , no host supplied
	'''
	前三页的 url
	https://movie.douban.com/top250
	https://movie.douban.com/top250?start=25&filter=
	https://movie.douban.com/top250?start=50&filter=
	'''
	for i in range(0, 250, 25):
		url = 'https://movie.douban.com/top250?start={}'.format(i)
		movies = movies_from_url(url)
		log('movies', i, movies)


if __name__ == '__main__':
	main()
