
import wave
import numpy as np
import sys
import getopt


def main(argv):


    try:

        opts, args = getopt.getopt(argv, "hi:o:r:d:c:", ["help", "input=", "output=","rate=","depth=","channel="])
    except getopt.GetoptError:
        print('Error: python holiday03.py -i wavData(all).txt -o Intro02.wav -r 16000 -d 2 -c 2')
        print('   or: python holiday03.py -i wavData(all).txt -o Intro02.wav --rate=16000 --depth=2 --channel=2')
        sys.exit(2)

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("为真实还原，输入的参数尽量和原语音一致")
            print('python holiday03.py -i wavData(all).txt -o Intro02.wav -r 16000 -d 2 -c 2')
            print('or: python tholiday03.py -i wavData(all).txt -o Intro02.wav --rate=16000 --depth=2 --channel=2')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg
        elif opt in ("-r", "--rate"):
            rate = arg
            rate=int(rate)
        elif opt in ("-d", "--depth"):
            depth = arg
            depth = int(depth)
        elif opt in ("-c", "--channel"):
            channel = int(arg)

    # wavData(all).txt
    # wavData(single).txt
    # https://blog.csdn.net/qq_35451572/article/details/79663356
    f = open(input)
    line = f.readline()
    data_list = []
    while line:
        #把切分出的列表的每个值, 把它们转成np.short型, 并返回迭代器
        num = list(map(np.short, line.split()))  # np.short
        #用list函数把map函数返回的迭代器遍历展开成一个列表
        data_list.append(num)
        line = f.readline()
    f.close()
    wave_data = np.array(data_list)

    # 打开WAV文档
    f = wave.open(output, "wb")

    # 配置声道数、量化位数和取样频率
    f.setnchannels(channel)  # 配置声道数
    f.setsampwidth(depth)  # 配置量化位数
    #f.setframerate(framerate)  # 配置取样频率
    f.setframerate(rate)  # 配置取样频率
    # f.setnframes(38000)

    # 将wav_data转换为二进制数据写入文件
    f.writeframes(wave_data.tostring())
    f.close()


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])

#python holiday03.py -i wavData(all).txt -o Intro02.wav -r 16000 -d 2 -c 2
#python holiday03.py -i wavData(all).txt -o Intro02.wav --rate=16000 --depth=2 --channel=2

#python holiday03.py -i lanTian2.txt -o lanTian2(还原).wav -r 16000 -d 2 -c 2
#python holiday03.py -i BAC009S0003W0121.txt -o BAC009S0003W0121(还原).wav -r 16000 -d 2 -c 1



import numpy as np
import sys
import wave   #语音文件处理包
import getopt


def main(argv):   #定义一个函数


    try:  #首先执行try后的程序，如果输入格式不对，则执行except getopt.GetoptError:后的程序

        opts, args = getopt.getopt(argv, "i:o:r:d:c:h", ["input", "output","rate=","depth=","channel=","help"])
    except getopt.GetoptError:
        print('输入格式错误，应该输入：python txt2wav.py -i text2.txt -o txt2wav.wav -r 16000 -d 2 -c 2\n或者输入格式为：python txt2wav.py -i text2.txt -o txt2wav.wav --rate=16000 --depth=2 --channel=2')
        #print('   or: python holiday03.py -i wavData(all).txt -o Intro02.wav --rate=16000 --depth=2 --channel=2')
        sys.exit()

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):   #打印帮助
            print("输入格式为：")
            print('python txt2wav.py -i text2.txt -o txt2wav.wav -r 16000 -d 2 -c 2')
            print('或者为：python txt2wav.py -i text2.txt -o txt2wav.wav --rate=16000 --depth=2 --channel=2')
            print("其中txt2wav.py为程序文件，text2.txt为采用语音转数据得到的语音数据文件，\ntxt2wav.wav为要转为的语音文件名称，-r或--rate代表采样率，-d或者--depth代表采样深度，-c或者--channel代表声道数")
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg
        elif opt in ("-r", "--rate"):
            rate = arg
            rate=int(rate)
        elif opt in ("-d", "--depth"):
            depth = arg
            depth = int(depth)
        elif opt in ("-c", "--channel"):
            channel = arg
            channel = int(channel)

    # wavData(all).txt
    # wavData(single).txt
    # https://blog.csdn.net/qq_35451572/article/details/79663356
    f = open(input)
    line = f.readline()  #每次读出txt文件中的一行内容
    data_list = []
    while line:
        #把切分出的列表的每个值, 把它们转成np.short型, 并返回迭代器
        num = list(map(np.short, line.split()))  # 用list函数把map函数返回的迭代器遍历展开成一个列表，map(np.short, line.split())表示把切分出的列表的每个值,把它们转成short型,并返回迭代器
        #用list函数把map函数返回的迭代器遍历展开成一个列表
        data_list.append(num)
        line = f.readline()
    f.close()
    wave_data = np.array(data_list)  #将列表数据转换成数组

    # 打开WAV文档
    f = wave.open(output, "wb")

    # 配置声道数、量化位数和取样频率
    f.setnchannels(channel)  # 配置声道数
    f.setsampwidth(depth)  # 配置量化位数
    #f.setframerate(framerate)  # 配置取样频率
    f.setframerate(rate)  # 配置取样频率
    # f.setnframes(38000)

    # 将wav_data转换为二进制数据写入文件
    f.writeframes(wave_data.tostring())
    f.close()


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])

#python holiday03.py -i wavData(all).txt -o Intro02.wav -r 16000 -d 2 -c 2
#python holiday03.py -i wavData(all).txt -o Intro02.wav --rate=16000 --depth=2 --channel=2

#python holiday03.py -i lanTian2.txt -o lanTian2(还原).wav -r 16000 -d 2 -c 2
#python holiday03.py -i BAC009S0003W0121.txt -o BAC009S0003W0121(还原).wav -r 16000 -d 2 -c 1


'''
 f = open(input)
    line = f.readline()  # 每次读出txt文件中的一行内容
    long=f.readlines()
    linenumber = len(long)
    print("文件行数：",linenumber+1)
    wave_data = np.zeros((linenumber+1, channel))
    i = 0
    while line:
        #num = np.array([np.short(x) for x in line.split()])
        num = np.array([line.split()],dtype=np.short)
        wave_data[i, :] = num
        print(wave_data)
        line = f.readline()
        i = i + 1
    f.close()
'''