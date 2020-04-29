import time
import os
import json

import requests
from pyquery import PyQuery as pq

from model.movie import Movie


def timestamp_datetime(value):
    format = '%H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt


def log(*args, **kwargs):
	unix_timestamp = int(time.time())
	dt = timestamp_datetime(unix_timestamp)
	with open('log.txt', 'a', encoding='utf-8') as f:
		print(dt, *args, file=f, **kwargs)


# 用一个字典解析语法
def transfer(i):
	dicts = {k: v for k, v in i.__dict__.items()}
	return dicts


# 把每个 object 转成, 字典表示
def dict_from_object(models):
	dicts = [transfer(i) for i in models]
	return dicts


def download_img(folder, models):
	# 如果没有此目录就创建
	if not os.path.exists(folder):
		os.makedirs(folder)
	# models 是一个 list, 每一个 model 是一个 object
	for m in models:
		filename = m['title'].split()[0] + '.jpg'
		path = os.path.join(folder, filename)
		if not os.path.exists(path):
			log('下载图片', filename)
			headers = {
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
			}
			r = requests.get(m['cover_url'], headers)
			with open(path, 'wb') as f:
				f.write(r.content)
		else:
			log(filename, '图片已下载过, 无需重复下载')


def models_from_url(url):
    # 缓存
	page = cached_url(url)
	# 返回一个 pyquery 对象
	e = pq(page)
	# 使用 jquery 语法, 得到 25 个div
	items = e('.item')
	# 用函数解析每个div, 组一个数组返回, 里面是 movie object
	models = [model_from_item(i) for i in items]
	dicts = dict_from_object(models)
	return dicts


def insert_many(db, documents, s):
    # MongoDB的每个数据库又包含许多集合 collection
	# 它们类似于关系型数据库中的表
	db[documents].insert_many(s)


def save_to_file(s, filename):
	# 先转成 json 格式
	# json.dumps 序列化时对中文默认使用的ascii编码
	# 想输出真正的中文需要指定 ensure_ascii = False
	# data = json.dumps(s, indent=2, ensure_ascii=False)
	folder = 'data'
	if not os.path.exists(folder):
		os.makedirs(folder)
	path = os.path.join(folder, filename)
	if not os.path.exists(path):
		log('写入文件')
		# open() 一定要指定 encoding='utf-8' 
		# 不然和 gbk 扯上关系, 可能中文 windows 默认打开文件 gbk, fuck
		with open(path, 'w', encoding='utf-8') as fp:
			json.dump(s, fp, ensure_ascii=False, indent=2)
	else:
		log('数据已保存, 无需再次保存')


def model_from_item(item):
	e = pq(item)
	# 保存电影信息
	form = {}
	form['title'] = e('.title').text()
	form['quote'] = e('.inq').text()
	form['cover_url'] = e('img').attr('src')
	form['score'] = float(e('.rating_num').text())
	form['ranking'] = int(e('em').text())
	# 选评论人数比较麻烦
	star = e('.star')
	span = pq(star)
	number_of_comments = span('span:nth-child(4)').text()
	form['number_of_comments'] = number_of_comments
	form['bd'] = e('.bd > p:nth-child(1)').text()
	form['time'] = int(form.get('bd').split('\n', 1)[1][:4])
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
		'''
		user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
		User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36
		'''
		headers = {
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
		}
		r = requests.get(url, headers=headers)
		with open(path, 'wb') as f:
			# 写入文件保存
			log('写入文件缓存')
			log('content', r, r.status_code, r.url)
			f.write(r.content)
		return r.content
