import wave
import numpy as np
import sys
import getopt


def enframe(signal, wlen, inc):
    '''
    参数含义：
    signal:原始音频型号
    nw:每一帧的长度
    inc:相邻帧的间隔
    '''
    signal_length = len(signal)  # 信号总长度
    if signal_length <= wlen:  # 若信号长度小于一个帧的长度，则帧数定义为1
        nf = 1
    else:  # 否则，计算帧数
        nf = int(np.ceil((1.0 * signal_length - wlen + inc) / inc))
        #np.ceil计算大于等于改值的最小整数，将小数点后部分删除
    pad_length = int((nf - 1) * inc + wlen)  # 所有帧加起来总的铺平后的长度
    zeros = np.zeros((pad_length - signal_length,))  # 不够的长度使用0填补，类似于FFT中的扩充数组操作
    #np.concatenate（）连接两个维度相同的矩阵
    pad_signal = np.concatenate((signal, zeros))  # 填补后的信号记为pad_signal
    indices = np.tile(np.arange(0, wlen), (nf, 1)) + np.tile(np.arange(0, nf * inc, inc), (wlen, 1)).T
    # 相当于对所有帧的时间点进行抽取，得到nf*nw长度的矩阵
    #tile() 函数，就是将原矩阵横向、纵向地复制展开
    indices = np.array(indices, dtype=np.int32)  # 将indices转化为矩阵
    frames = pad_signal[indices]  # 得到帧信号

    return frames#返回帧信号矩阵


def main(argv):
    try:

        #opts, args = getopt.getopt(argv, "-h-i:-f:-o:", ["help", "input=", "framelength", "overlap"])
         opts, args = getopt.getopt(argv, "-h-i:-o:-f:-l:", ["help", "input=", "output=","framelength=","overlap="])
    except getopt.GetoptError:
        print('Error: python holiday04.py -i BAC009S0003W0121.txt -o frame02.txt --framelength 200 --overlap 100')
        print('   or: python holiday04.py -i BAC009S0003W0121.txt -o frame01.txt -f 200 -l 100')
        sys.exit(2)

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("音频的分帧")
            print('python holiday04.py -i BAC009S0003W0121.txt -o frame02.txt --framelength 200 --overlap 100')
            print('or: python holiday04.py -i BAC009S0003W0121.txt -o frame01.txt -f 200 -l 100')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg

        elif opt in ("-f", "--framelength"):
            framelength = int(arg)
            print(framelength)

        elif opt in ("-l", "--overlap"):
            overlap = int(arg)

            f = open(input)
            # f = open("wavData(left).txt")
            # f = open("lanTian2.txt")
            # wavData(left)
            line = f.readline()
            data_list = []
            while line:
                # 把切分出的列表的每个值, 把它们转成np.short型, 并返回迭代器
                num = list(map(np.short, line.split()))  # np.short
                # 用list函数把map函数返回的迭代器遍历展开成一个列表
                data_list.append(num)
                line = f.readline()
            f.close()
            wave_data = np.array(data_list)
            signal = wave_data.T

            Frame = enframe(signal[0], framelength, overlap)  # signal[0]是为了保证维度一致

            file = open(output, 'w+')

            np.savetxt(file,Frame, fmt='%d', delimiter=' ')
            file.close()


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])


#python holiday04.py -i BAC009S0003W0121.txt -o frame02.txt --framelength 200 --overlap 100
#python holiday04.py -i BAC009S0003W0121.txt -o frame01.txt -f 200 -l 100
#python holiday04.py -i lanTian2.txt -o frame01.txt -f 200 -l 100