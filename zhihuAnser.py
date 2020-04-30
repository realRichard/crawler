from utils import (
	models_from_url,
	save_to_file,
	insert_many,
	log,
)

from mongo_config import db


def main():
    # https://www.zhihu.com/collection/38887091?ssr_src=heifetz&page=1
    # https://www.zhihu.com/collection/38887091?ssr_src=heifetz&page=2
    # https://www.zhihu.com/collection/38887091?ssr_src=heifetz&page=3
	# 用于将所有 anser 的字典形式保存在一个 list, 便于插入 mongodb
	anser_list = []
	for i in range(1, 11):
		url = 'https://www.zhihu.com/collection/38887091?ssr_src=heifetz&page={}'.format(i)
		ansers = models_from_url(url)
		# 合并 list
		anser_list += ansers
	log('anser_list', type(anser_list), len(anser_list))
	# 两种存储数据的方式, mongodb, 写入数据文件(json格式)
	# insert_many(db, 'zhihuAnser', anser_list)
	# 写入文件
	save_to_file(anser_list, 'zhihuAnser.txt')


if __name__ == '__main__':
	main()