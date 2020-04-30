#fft数据计算mfcc系数
import numpy as np
import sys
import getopt
from scipy.fftpack import dct
import matplotlib.pyplot as plt
#import time
'''
采样率为44100
帧长2048 帧移1024
'''

def main(argv):
    #startTime = time.clock()
   # startTime = time.process_time()
    try:
         opts, args = getopt.getopt(argv[1:], "-i:-o:h", ["input=", "output=","help"])
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
            fft_data = np.loadtxt(input, dtype=np.complex)  # 读取文件数据，数据格式为复数
            '''
            f = open(input, 'rb')

            # 读取fft文件数据
            line = f.readline()
            print(type(line))
            data_list = []
            while line:
                # 把切分出的列表的每个值, 把它们转成np.short型, 并返回迭代器
                num = (list(map(np.complex, line.split())))  # np.short
                # 用list函数把map函数返回的迭代器遍历展开成一个列表
                data_list.append(num)
                line = f.readline()
            f.close()
            fft_data = np.array(data_list)
            '''
            w = []
            for n in range(1, 13):
                w1 = 1 + 6 * np.sin(np.pi * n / 12)  #倒谱提升窗口
                w.append(w1)

            fs = 44100
            mfcc_data = []  # 用来存储mfcc数据

            strlen = len(fft_data)
            # print(frameNum)
            for i in range(strlen):
                y = fft_data[i, :]
                # fft
                # fft_data=np.fft.fft(y)
                yf = np.abs(y)
                # print(yf.shape)
                # 计算谱线能量
                yf = yf ** 2
                # 梅尔滤波器系数
                nfilt = 26  #Mel滤波器组个数
                low_freq_mel = 0
                NFFT = 2048  #和帧长相关
                high_freq_mel = (2595 * np.log10(1 + (fs / 2) / 700))  # 把 Hz 变成 Mel
                mel_points = np.linspace(low_freq_mel, high_freq_mel, nfilt + 2)  # 将梅尔刻度等间隔(在low_freq_mel和high_freq_mel值之间生成nfilt + 2个等间隔数据)
                hz_points = (700 * (10 ** (mel_points / 2595) - 1))  # 把 Mel 变成 Hz
                bin = np.floor((NFFT + 1) * hz_points / fs)  #np.floor函数返回不大于参数的最大整数
                fbank = np.zeros((nfilt, int(np.floor(NFFT / 2 + 1))))
                #实现Mel滤波器组
                for m in range(1, nfilt + 1):
                    f_m_minus = int(bin[m - 1])  # Mel滤波器组的最低频率
                    f_m = int(bin[m])  # Mel滤波器组的中心频率
                    f_m_plus = int(bin[m + 1])  #Mel滤波器组的最低频率
                    #计算每个带通滤波器的传递函数
                    for k in range(f_m_minus, f_m):
                        fbank[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
                    for k in range(f_m, f_m_plus):
                        fbank[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])
                filter_banks = np.dot(yf[0:1025], fbank.T)#dot()返回的是两个数组的点积，如果处理的是一维数组，则得到的是两数组的內积，如果是二维数组（矩阵）之间的运算，则得到的是矩阵积
                filter_banks = np.where(filter_banks == 0, np.finfo(float).eps, filter_banks)  # np.where函数，当filter_banks == 0为真时，选择np.finfo(float).eps（finfo函数是根据括号中的类型来获得信息，获得符合这个类型的数型，eps为当数为负数或0时取非负数的最小整数），否则选择filter_banks
                filter_banks = 10 * np.log10(filter_banks)  # dB一帧的对数能量
                filter_banks -= (np.mean(filter_banks, axis=0) + 1e-8)
                '''
                numpy.mean(a, axis, dtype, out，keepdims )
                mean()函数功能：求取均值 
                经常操作的参数为axis，以m * n矩阵举例(a为输入的mxn矩阵)：
                
                axis 不设置值，对 m*n 个数求均值，返回一个实数
                axis = 0：压缩行，对各列求均值，返回 1* n 矩阵
                axis =1 ：压缩列，对各行求均值，返回 m *1 矩阵
            '''
                # DCT系数
                num_ceps = 12  #通常，对于自动语音识别（ASR），所得到的倒谱系数2-13被保留，其余的被丢弃; num_ceps = 12。丢弃其他系数的原因是它们表示滤波器组系数的快速变化，并且这些细节不会有助于自动语音识别（ASR）。
                c2 = dct(filter_banks, type=2, axis=-1, norm='ortho')[1: (num_ceps + 1)]  # 调用dct函数
                c2 *= w
                mfcc_data.append(c2)  # 将数据添加到mfcc_data

            # np.savetxt("mfcc.txt",lif,fmt='%d')
            np.savetxt(output, mfcc_data)
           # endTime = time.process_time()
            #print("运行时间为:%f s" % (endTime - startTime))
            mfcc_data1 = np.array(mfcc_data)
            mfcc_data2 = mfcc_data1[:,0]
            plt.plot(mfcc_data2)
            plt.show()
if __name__ == "__main__":
    main(sys.argv)

#python fft2mfcc.py -i Englishfft_for_mfcc.txt -o mfcc.txt
