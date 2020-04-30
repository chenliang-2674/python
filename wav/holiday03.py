
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