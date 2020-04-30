#将txt语音数据进行分帧
# -*- coding: utf-8 -*-
import numpy as np
import sys
import wave   #语音文件处理包
import getopt


def main(argv):  #定义一个函数
    try:  #首先执行try后的程序，如果输入格式不对，则执行except getopt.GetoptError:后的程序
        opts, args = getopt.getopt(argv, "i:o:f:l:h", ["input", "output","framelength","lap","help"])  #命令行输入参数
    except getopt.GetoptError:
        print('输入参数错误，输入格式为:python wav2txt.py -i test.wav -o text3.txt -l/-r/-a，\n其中wav2txt.py为程序文件名称，test.wav为语音文件，text3.txt为.wav文件的数据保存到的文件，\n-l/-r/-a分别为左声道，右声道，双声道，对于单声道语音文件，最后这部分没必要加，但对双声道数据则可以分别保存左声道，右声道，或两个声道的数据')
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):   #打印帮助
            #test.wav为单声道语音文件，test2.wav为双声道语音文件
            print('单声道:python wav2txt.py -i test.wav -o text3.txt')
            print('打印双声道的左声道数据:python wav2txt.py -i test2.wav -o text3.txt -l')
            print('打印双声道的右声道数据:python wav2txt.py -i test2.wav -o text3.txt -r')
            print('打印双声道的数据:python wav2txt.py -i test2.wav -o text3.txt或者python wav2txt.py -i test2.wav -o text3.txt -a')
            print('无-o项时输出到屏幕上:python wav2txt.py -i test2.wav' )
            sys.exit()
        #判断双声道的且输入参数中含有-l/-r/-a等的情况，包括左声道，右声道，和双声道
        elif opt in ("-i", "--input"):
            input = arg
            f = open(input, 'rb')  # 打开语音文件
        elif opt in ("-o", "--output"):
            output = arg
            f1 = open(output, 'w')  # 打开输出的txt文件
        elif opt in ("-f", "--framelength"):  # 输入的采样频率
            framelength = arg
            framelength = int(framelength)
        elif opt in ("-l", "--lap"):  # 输入的采样频率
            lap = arg
            lap = int(lap)


        lines = f.readlines()
        for line in lines:
            for i in range(4):
                line1 = line.split('\t')
                f1.write(line1)
            print("\n")
        f1.close()  # 关闭输出文件
        f.close()  # 关闭输入的语音文件
        exit()

if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])  #调用函数


#https://blog.csdn.net/luolinll1212/article/details/98940838