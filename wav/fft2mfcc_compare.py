#调包实现mfcc
import numpy as np
import sys
import getopt
from python_speech_features import mfcc
import librosa
from scipy.fftpack import dct
import scipy.io.wavfile as wav
# import time
'''
采样率为44100
帧长2048 帧移1024
'''


def main(argv):
    # startTime = time.clock()
    # startTime = time.process_time()
    try:
        opts, args = getopt.getopt(argv[1:], "-i:-o:h", ["input=", "output=", "help"])
    except getopt.GetoptError:
        print('输入格式错误，输入为fft变换后的数据文件，输出为计算得到的mfcc系数数据文件')
        print('python fft2mfcc.py -i Englishfft_for_mfcc.txt -o mfcc.txt')
        sys.exit()

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("fft数据计算mfcc系数")
            print('python fft2mfcc.py -i Englishfft_for_mfcc.txt -o mfcc.txt')
            print('输入为fft变换后的数据文件，输出为计算得到的mfcc系数数据文件')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg
            fs, audio = wav.read("BAC009S0003W0121.wav")
            feature_mfcc = mfcc(audio, samplerate=fs)
            # np.savetxt("mfcc.txt",lif,fmt='%d')
            np.savetxt(output, mfcc_data)
        # endTime = time.process_time()
        # print("运行时间为:%f s" % (endTime - startTime))


if __name__ == "__main__":
    main(sys.argv)

# python fft2mfcc.py -i Englishfft_for_mfcc.txt -o mfcc.txt

#fft2mfcc_compare.py