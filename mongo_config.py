import pymongo


# 连接 mongo 数据库, 主机是本机, 端口是默认端口
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['crawler']