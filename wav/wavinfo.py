#解析.wav文件，得到采样频率，声道数，量化位数，采样点数
import argparse
import numpy as np
import sys
import wave   #语音文件处理包
import getopt

def main(argv):  #定义一个函数
    try:  #首先执行try后的程序，如果输入格式不对，则执行except getopt.GetoptError:后的程序
        opts, args = getopt.getopt(argv[1:], "i:o:h", ["input", "output","help"])  #命令行输入参数
    except getopt.GetoptError:
        print('输入参数错误，输入格式为:python wavinfo.py -i voice.wav -o text1.txt,\n其中wavinfo.py为程序文件名称，voice.wav为语音文件，text1.txt为.wav文件的数据保存到的文件')
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):   #打印帮助
            print('读取语音文件声道数，采样频率，采样深度，采样点数')
            print('输入格式为:')
            print('python wavinfo.py -i voice.wav -o text1.txt')
            print('其中wavinfo.py为程序文件名称，voice.wav为语音文件，text1.txt为.wav文件的数据保存到的文件' )
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
            f = wave.open(input, "rb")
            # 读取格式信息
            # 一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
            params = f.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            print("声道数=", nchannels, "\n量化位数=", sampwidth, "\n采样频率=", framerate, "\n采样点数=", nframes)
        elif opt in ("-o", "--output"):
            output = arg
            params = f.getparams()
            # file = open('results_storage.txt', 'a')
            file = open(output, 'w+')
            bins = ['声道数', '量化位数（byte单位）', '采样频率', '采样点数']
            # i=0
            # 保存到本地txt文件
            params = params[:4]
            for i in range(4):
                # s = str(bins[i]).replace('[',").replace('[',")+'\t'+str(data[i]).replace('[',").replace('[',")#去除[],这两行按数据不同，可以选择
                s = str(bins[i]).replace('[', ").replace('[',") + '=' + str(params[i]).replace('[', ").replace('[',")
                s = s.replace("'", ").replace(',',") + '\n'  # 去除单引号，逗号，每行末尾追加换行符
                file.write(s)
            file.close()
            f.close()


if __name__ == '__main__':
    main(sys.argv)  # 调用函数
#python wavinfo.py -i English.wav -o Englishinfo_for_mfcc.txt
#python wavinfo.py -i voice.wav -o text1.txt
#python wavinfo.py -h