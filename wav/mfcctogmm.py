#将本地的MFCC数据读入，判断是否符合正态分布
import sys
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy import stats
from itertools import chain
import matplotlib.pyplot as plt
import getopt

def main(argv):
    try:
         opts, args = getopt.getopt(argv[1:], "i:-h", ["input","help"])
    except getopt.GetoptError:
        print('对得到的MFCC数据进行判断，是否服从正态分布')
        print('命令行输入格式为：python mfcctogmm.py -i mfcc.txt')
        sys.exit(2)

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("对得到的MFCC数据进行判断，是否服从正态分布")
            print('命令行输入格式为：python mfcctogmm.py -i mfcc.txt')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
            file = open(input, 'rb')  #打开输入的数据文件
            line = file.readline()  #每次读取一行内容
            data_list = []    #定义一个空列表，用于存储数据
            while line:
                # 用list函数把map函数返回的迭代器遍历展开成一个列表，map(np.double, line.split())表示把切分出的列表的每个值,把它们转成double型,并返回迭代器
                num = list(map(np.double, line.split()))
                data_list.append(num)  # 将从文件中读到的数据放入列表的两个中括号之间
                line = file.readline()  #每次都需要进行重新读下一行
            file.close()
            data = np.array(data_list)   #将列表转为数组

            n = data.ndim  #获取数组维度
            if n == 2:  # 判断是否是二维数据
                data = list(chain(*data))  # 将数据从二维转换一维

            data_max = int(max(data))   #取数据最大值，并转化为int型
            data_min = int(min(data))   #取数据最小值，并转化为int型
            if data_max < 0:
                data_max = data_max - 1
            else:
                data_max = data_max + 1

            if data_min < 0:
                data_min = data_min - 1
            else:
                data_min = data_min + 1
            gap = int((abs(data_max) + abs(data_min)) / 10)   #数据间隔
            if gap == 0 or gap < 0:    #如果分组间隔等于0或小于0，默认分组间隔为1
                gap = 1
            area = list(range(data_min, data_max, gap)) #数据范围，将数据分为等间隔
            group = pd.cut(data, area, right=True, include_lowest=True)  # 分组区间
            # pd.cut()的作用，有点类似给成绩设定优良中差
            # right：bool型参数，默认为True表示是否包含区间右部
            # include_lowest：bool型的参数，表示区间的左边是开还是闭的，默认为false，也就是不包含区间左部（闭）

            frequency = group.value_counts()  # 计算频数

            n = frequency.values.sum()  # 频数总和
            strlen = len(frequency)
            mean = []
            # 求出区间的中位数Vj，作为每组的代表数据
            for i in range(strlen):
                qujian_mean = sum([frequency.index[i].right, frequency.index[i].left]) / 2  #区间中值为Vj
                mean.append(qujian_mean)

            # 求数据的估计均值
            val_sum = 0
            for j in range(strlen):
                val = mean[j] * frequency.values[j]  #中值乘以频数的值
                val_sum = val + val_sum  #累加
            mu = val_sum / n  #求均值

            # 求数据的标准差
            val_pow = 0
            for i in range(strlen):
                variance = ((mean[i] - mu) ** 2) * frequency.values[i]
                val_pow = variance + val_pow
            stand = np.sqrt(val_pow / n)

            # 求标准正态分布的值x
            X = []
            for i in range(strlen):
                x = (frequency.index[i].left - mu) / stand
                X.append(x)
            X.append((frequency.index[strlen - 1].right - mu) / stand)

            P = []
            for i in range(strlen):
                p = norm.cdf(X[i + 1]) - norm.cdf(X[i])  #求估计概率
                P.append(p)
                #norm.cdf：返回概率密度函数在负无穷到x上的积分，也就是概率分布函数的值

            # 检验统计量地值 卡方值
            c1 = strlen
            # 卡方分位数,查表得到临界值
            k0 = stats.chi2.isf(0.05, strlen - 3)

            k1 = 0
            for i in range(strlen):
                b = ((mean[i] - n * P[i]) ** 2) / (n * P[i])
                k1 = k1 + b
            '''
            统计假设为：
            H0：F(x)=F0(x)，则符合正态分布
            H1:F(x)!=F0(x)，则不符合正态分布
            拒绝域为k1>k0，k1为检验统计量的值，k0为卡方分布的值
            '''
            if k1 > k0:
                print("假设H0为：输入的数据服从正态分布。\n此时检验统计量的值大于临界值，则拒绝假设H0，认为输入的数据不符合正态分布！")
            if k1 < k0:
                print("假设H0为：输入的数据服从正态分布。\n此时检验统计量的值小于临界值，则接受假设H0，认为输入的数据符合正态分布！")
            mfcc_data = np.loadtxt(input, dtype=np.float)
            plt.plot(mfcc_data)
            plt.show()




if __name__ == "__main__":
    main(sys.argv)  # sys.argv为要处理的参数列表


#python mfcctogmm.py -i mfcc.txt
