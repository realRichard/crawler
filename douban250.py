import requests
from pyquery import PyQuery as pq

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



def movies_from_url(url):
	# 请求
	r = requests.get(url)
	page = r.content
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
		log('Top250 movies', movies)


if __name__ == '__main__':
	main()
