import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib
from pylab import mpl

from utils import (
    get_data,
    log,
    merge_array,
    get_dict,
)


mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['font.size'] = 6.0


# fontP = font_manager.FontProperties()
# fontP.set_family('SimHei')
# fontP.set_size(14)


# # 设置 matplotlib 正常显示中文和负号
# matplotlib.rcParams['font.family'] = 'SimHei'   # 用黑体显示中文
# matplotlib.rcParams['axes.unicode_minus'] = False     # 正常显示负号


def time_bar():
    data = get_data('doubanTop250.txt', 'time')
    # log(len(data))
    count = {}
    for i in set(data):
        count[i] = data.count(i)
    log('count', count)
    d = pd.Series(count)
    index = d.index
    values = d.values
    log(index, values)
    plt.bar(index, values, color='rgb')
    plt.xlabel('year')
    plt.ylabel('frequentcy')
    plt.title('douban Movie year frequency bar chart')
    # plt.savefig('doubanTime.', dpi=600)
    plt.show()


def region_pie():
    data = merge_array('doubanTop250.txt', 'region')
    # log('region', len(data), data)
    count = {}
    for i in set(data):
        count[i] = data.count(i)
    log('count', count)
    d = pd.Series(count)
    index = d.index
    values = d.values
    log(index, values)
    plt.pie(values, labels=index, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('douban Movie region')
    # plt.savefig('doubanRegion.', dpi=600)
    plt.show()


def category_pie():
    data = merge_array('doubanTop250.txt', 'category')
    # log('category', len(data), data)
    count = {}
    for i in set(data):
        count[i] = data.count(i)
    log('count', count)
    d = pd.Series(count)
    index = d.index
    values = d.values
    log(index, values)
    plt.pie(values, labels=index, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('douban Movie category')
    # plt.savefig('doubanCategory.', dpi=600)
    plt.show()


def score_barh():
    data = get_dict('doubanTop250.txt', 'title', 'score')
    log(data)
    d = pd.Series(data)
    index = d.index
    values = d.values
    log(index, values)
    plt.barh(index, values, color='rgb')
    plt.ylabel('movie name')
    plt.xlabel('score')
    plt.xlim(9, 10)
    plt.title('score the top ten')
    # plt.savefig('doubanScore')
    plt.show()


def main():
    # time_bar()
    # region_pie()
    # category_pie()
    score_barh()


if __name__ == '__main__':
    main()