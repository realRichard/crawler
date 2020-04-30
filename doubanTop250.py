from utils import (
	models_from_url,
	download_img,
	save_to_file,
	insert_many,
	log,
)

from mongo_config import db


def main():
	# 'https: // movie.douban.com/top250'
	# 豆瓣网直接复制下来的 url 有病, invalidURL  , no host supplied
	'''
	前三页的 url
	https://movie.douban.com/top250
	https://movie.douban.com/top250?start=25&filter=
	https://movie.douban.com/top250?start=50&filter=
	'''
	# 用于将所有 movie 的字典形式保存在一个 list, 便于插入 mongodb
	movie_list = []
	for i in range(0, 250, 25):
		url = 'https://movie.douban.com/top250?start={}'.format(i)
		movies = models_from_url(url)
		# 合并 list
		movie_list += movies
		# download_img('doubanTop250', movies)
	log('movie_list', type(movie_list), len(movie_list))
	# 两种存储数据的方式, mongodb, 写入数据文件(json格式)
	insert_many(db, 'doubanTop250', movie_list)
	# 写入文件
	save_to_file(movie_list, 'doubanTop250.txt')


if __name__ == '__main__':
	main()