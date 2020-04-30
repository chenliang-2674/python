#将txt语音数据进行分帧
# -*- coding: utf-8 -*-
import numpy as np
import sys
import wave   #语音文件处理包
import getopt

def enframe(data, wlen, inc):   #data为语音数据，wlen为帧长，inc为帧移
    data_length = len(data)  # 信号总长度
    if data_length <= wlen:  # 若信号长度小于一个帧的长度，则帧数定义为1
        nf = 1
    else:  # 否则，计算帧数
        nf = int(np.ceil((1.0 * data_length - wlen + inc) / inc))
        #np.ceil计算大于等于改值的最小整数，将小数点后部分删除
    pad_length = int((nf - 1) * inc + wlen)  # 所有帧加起来总的铺平后的长度
    #zeros = np.zeros((pad_length - data_length,))
    #pad_signal = np.concatenate((data, zeros))  # 补充完整的语音数据
    pad_signal = np.pad(data, (0, pad_length - data_length), 'constant')  # 用0填充最后不足一帧的数据
    indices = np.tile(np.arange(0, wlen), (nf, 1)) + np.tile(np.arange(0, nf * inc, inc), (wlen, 1)).T  #每帧的索引，将原矩阵横向、纵向地复制展开
    #tile() 函数，就是将原矩阵横向、纵向地复制展开
    indices = np.array(indices, dtype=np.int32)  # 将indices转化为矩阵，数值类型为32位整型
    frames = pad_signal[indices]  # 得到帧信号, 用索引拿数据

    return frames  #返回分帧后的语音数据矩阵

def main(argv):  #定义一个函数
    try:  #首先执行try后的程序，如果输入格式不对，则执行except getopt.GetoptError:后的程序
        opts, args = getopt.getopt(argv, "i:o:-f:-l:h", ["input", "output","framelength=","overlap=","help"])  #命令行输入参数
    except getopt.GetoptError:
        print('输入参数错误，输入格式为:python wavtxtframe.py -i English.txt -o Englishframe1.txt -f 4 -l 2，\n其中wavtxtframe.py为程序文件名称，English.txt为语音数据文件，Englishframe1.txt为分帧后的语音数据文件，\n-f为分帧的帧长，-l为帧移')
        sys.exit()
    #global file
    for opt, arg in opts:
        if opt in ("-h", "--help"):   #打印帮助
            #test.wav为单声道语音文件，test2.wav为双声道语音文件
            print('输入格式为：')
            print('python wavtxtframe.py -i English.txt -o Englishframe1.txt -f 4 -l 2')
            print('或者：python wavtxtframe.py -i English.txt -o Englishframe1.txt --framelength 4 --overlap 2')
            print('其中wavtxtframe.py为程序文件名称，English.txt为语音数据文件，Englishframe1.txt为分帧后的语音数据文件')
            print('-f/-framenlength为分帧的帧长，-l/overlap为帧移' )
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg   #取命令行参数，即输入
            file1 = open(input, 'rb')  # 打开语音数据文件
        elif opt in ("-o", "--output"):
            output = arg   #取命令行参数，即输出
            file2 = open(output, 'w+')  # 打开分帧后的数据保存的txt文件
        elif opt in ("-f", "--framelength"):
            framelength = arg   #取命令行framelength后的参数，即帧长
            framelength = int(framelength)
        elif opt in ("-l", "--overlap"):
            overlap = arg  #取命令行overlap后的参数，即帧移
            overlap = int(overlap)

            line = file1.readline()  # 每次读出txt文件中的一行内容
            data = []  #初始化一个空矩阵
            while line:   #当未读到文件最后时
                # 把切分出的列表的每个值, 把它们转成np.short型, 并返回迭代器
                num = list(map(np.short, line.split()))  # np.short
                # 用list函数把map函数返回的迭代器遍历展开成一个列表
                data.append(num)
                line = file1.readline()
            file1.close()
            wavdata = np.array(data)  # 将列表数据转换成数组
            signal = wavdata.T  #将列矩阵转为行矩阵
            Frame = enframe(signal[0], framelength, overlap)  # 调用分帧函数
            #for i in Frame:

            np.savetxt(file2, Frame, fmt='%d', delimiter=' ')
            print(Frame)
            file2.close()

    '''
    lines = f.readlines()
    long = len(lines)
    for line in lines:
        
        for i in range(4):
            line1 = line
            file.write(line1)
            print("\t")
        print("\n")
        
        data = np.reshape(line, [long, 4])
    file.close()  # 关闭输出文件
    f.close()  # 关闭输入的语音文件
    exit()
    '''
if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])  #调用函数


#https://blog.csdn.net/luolinll1212/article/details/98940838
#python wavtxtframe.py -i English.txt -o Englishframe1.txt -f 4 -l 2
#python wavtxtframe.py -i English.txt -o Englishframe1.txt --framelength 4 --overlap 2
#python wavtxtframe.py -i English.txt -o Englishframe2.txt --framelength 8 --overlap 4
#python wavtxtframe.py -i English.txt -o Englishframe2.txt -f 8 -l 4
#python wavtxtframe.py -i English.txt -o Englishframe_for_mfcc.txt -f 2048 -l 1024