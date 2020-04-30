#文本数据文件转为.wav语音文件
import numpy as np
import sys
import wave   #语音文件处理包
import getopt


def main(argv):   #定义一个函数


    try:  #首先执行try后的程序，如果输入格式不对，则执行except getopt.GetoptError:后的程序

        #opts, args = getopt.getopt(argv, "i:o:r:d:c:h", ["input", "output","rate=","depth=","channel=","help"])
        opts, args = getopt.getopt(argv, "i:o:-r:-d:-c:h", ["input", "output", "rate=", "depth=", "channel=", "help"])
    except getopt.GetoptError:
        print('输入格式错误，应该输入：python txt2wav.py -i text2.txt -o txt2wav.wav -r 16000 -d 2 -c 2\n或者输入格式为：python txt2wav.py -i text2.txt -o txt2wav.wav --rate=16000 --depth=2 --channel=2')
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):   #打印帮助
            print("输入格式为：")
            print('python txt2wav.py -i text2.txt -o txt2wav.wav -r 16000 -d 2 -c 2')
            print('或者为：python txt2wav.py -i text2.txt -o txt2wav.wav --rate=16000 --depth=2 --channel=2')
            print("其中txt2wav.py为程序文件，text2.txt为采用语音转数据得到的语音数据文件，\ntxt2wav.wav为要转为的语音文件名称，-r或--rate代表采样率，-d或者--depth代表采样深度，-c或者--channel代表声道数")
            sys.exit()
        elif opt in ("-i", "--input"):    #输入为txt数据文件
            input = arg
        elif opt in ("-o", "--output"):   #输出为wav语音文件
            output = arg
        elif opt in ("-r", "--rate"):     #输入的采样频率
            rate = arg
            rate=int(rate)
        elif opt in ("-d", "--depth"):    #输入的量化位数
            depth = arg
            depth = int(depth)
        elif opt in ("-c", "--channel"):   #输入的声道数
            channel = arg
            channel = int(channel)
    '''
        f = open(input)
        data_lists = f.readlines()  # 读出的是str类型

        dataset = []
        # 对每一行作循环
        for data in data_lists:
            data1 = data.strip('\n')  # 去掉开头和结尾的换行符
            data2 = data1.split('\t')  # 把tab作为间隔符
            dataset.append(data2)  # 把这一行的结果作为元素加入列表dataset
        f.close()
        wave_data = np.array(dataset)
        '''

    f = open(input)  #打开输入文件

    '''
    long = f.readlines()  #一次性读取文件所有行
    linenumber = len(long)
    print("文件行数(即采样点数)：",linenumber + 1)
    '''
    print("声道数：",channel)
    print("量化位数：",depth)
    print("采样频率：", rate)
    line = f.readline()  # 每次读出txt文件中的一行内容
    data = []   #初始化一个空矩阵
    i=0
    while line:    #当未读到文件最后时
        num = list(map(np.short,
                       line.split()))  # 用list函数把map函数返回的迭代器遍历展开成一个列表，map(np.short, line.split())表示把切分出的列表的每个值,把它们转成short型,并返回迭代器
        data.append(num)    #将从文件中读到的数据放入列表的两个中括号之间
        i = i+1
        line = f.readline()
    f.close()
    wavdata = np.array(data)  # 将列表数据转换成数组
    print("文件行数(即采样点数)：",i)

    f = wave.open(output, "wb")   #新建并打开wav文件

    # 配置声道数、量化位数和采样频率
    f.setnchannels(channel)  # 配置声道数
    f.setsampwidth(depth)  # 配置量化位数
    f.setframerate(rate)  # 配置采样频率

    f.writeframes(wavdata.tostring())  # 将wav_data转换为二进制数据写入文件
    f.close()


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])

#运行的命令行
#python txt2wav.py -i text3.txt -o test3(还原).wav -r 16000 -d 2 -c 1
#python txt2wav.py -i text2.txt -o test2(还原).wav -r 16000 -d 2 -c 2
#python txt2wav.py -i text2.txt -o test2(还原).wav --rate 16000 --depth 2 --channel 2
#python txt2wav.py -i English.txt -o English(还原).wav -r 44100 -d 2 -c 1
#python txt2wav.py -i text3.txt -o test3(还原).wav --rate 16000 --depth 2 --channel 1
