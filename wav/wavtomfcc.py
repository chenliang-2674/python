#实现wav语音文件读取数据，分帧，fft，最后实现mfcc
import numpy as np
import sys
import getopt
from scipy.fftpack import dct
import matplotlib.pyplot as plt
import wave   #语音文件处理包

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
        opts, args = getopt.getopt(argv[1:], "i:o:-f:-l:h", ["input", "output","framelength=","overlap=","help"])  #命令行输入参数
    except getopt.GetoptError:
        print('输入参数错误，输入格式为:python wavtomfcc.py -i English.wav -o English_wavtomfcc.txt -f 2048 -l 1024，\n其中wavtomfcc.py为程序文件名称，English.wav为语音文件，English_wavtomfcc.txt为进行mfcc后的数据文件，\n-f为分帧的帧长，-l为帧移')
        sys.exit()
    #global file
    for opt, arg in opts:
        if opt in ("-h", "--help"):   #打印帮助
            #test.wav为单声道语音文件，test2.wav为双声道语音文件
            print('输入wav语音文件，进行分帧，fft,最后进行mfcc，最终得mfcc数据')
            print('输入格式为：')
            print('python wavtomfcc.py -i English.wav -o English_wavtomfcc.txt -f 2048 -l 1024')
            print('或者：python wavtomfcc.py -i English.wav -o English_wavtomfcc.txt --framelength 2048 --overlap 1024')
            print('其中wavtomfcc.py为程序文件名称，English.wav为语音文件，English_wavtomfcc.txt为进行mfcc后的数据文件')
            print('-f/-framenlength为分帧的帧长，-l/overlap为帧移' )
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg   #取命令行参数，即输入
            file1 = wave.open(input, 'rb')  # 打开语音数据文件
            params = file1.getparams()  # 得到语音参数
            nchannels, sampwidth, framerate, nframes = params[:4]  # 分别为声道数，量化位数，采样频率，采样点数
            print("声道数=", nchannels, "\t量化位数=", sampwidth, "\t采样频率=", framerate, "\t采样点数=", nframes)
            wavdata = file1.readframes(nframes)
            # 将字符串转换为数组，得到一维的short类型的数组
            # data = np.fromstring(data, dtype=np.short)
            wavdata = np.frombuffer(wavdata, dtype=np.short)
            # 整合左声道和右声道的数据
            wavdata = np.reshape(wavdata, [nframes, nchannels])  # 将采样数据规整为每行nchannels个数据，如果为单声道，每行一个数据，如果双声道，每行就两个数据
            length = len(wavdata)  # 该段语音采样点个数
        elif opt in ("-o", "--output"):
            output = arg   #取命令行参数，即输出
            file2 = open(output, 'w+')  # 打开进行mfcc后的数据保存的txt文件
        elif opt in ("-f", "--framelength"):
            framelength = arg   #取命令行framelength后的参数，即帧长
            framelength = int(framelength)
        elif opt in ("-l", "--overlap"):
            overlap = arg  #取命令行overlap后的参数，即帧移
            overlap = int(overlap)
            if nchannels==2:
                print('输入错误，输入的语音文件只能为单声道的，否则后续处理结果不正确')
                sys.exit()
            else:
                # wave_data = np.append(wavdata[0], wavdata[1:] - 0.9375 * wavdata[:-1])  # 预加重
                # signal = wavdata.T  # 将列矩阵转为行矩阵
                # # signal = wavdata.T
                # Frame = enframe(signal[0], framelength, overlap)  # 调用分帧函数
                wave_data = np.append(wavdata[0], wavdata[1:] - 0.9375 * wavdata[:-1])  #预加重
                signal = wave_data.T  # 将列矩阵转为行矩阵
                #signal = wavdata.T
                Frame = enframe(signal, framelength, overlap)  # 调用分帧函数
                win = np.hamming(framelength)
                Frame = Frame*win
               # fft_data = np.fft.fft(Frame)  #对分帧后的数据进行fft变换

                #进行mfcc
                w = []
                for n in range(1, 13):
                    w1 = 1 + 6 * np.sin(np.pi * n / 12)  # 倒谱提升窗口
                    w.append(w1)
                #归一化
                for i in range(1,13):
                    w = w/max(w)

                fs = 44100
                mfcc_data = []  # 用来存储mfcc数据

                strlen = len(Frame)
                print(strlen)
                # print(frameNum)
                for i in range(strlen):
                    y = Frame[i, :]
                    yf = np.fft.fft(y)
                    # fft
                    # fft_data=np.fft.fft(y)
                    yf = np.abs(yf)
                    # print(yf.shape)
                    # 计算谱线能量
                    yf = yf ** 2
                    # 梅尔滤波器系数
                    nfilt = 24  # Mel滤波器组个数
                    low_freq_mel = 0
                    NFFT = 2048  # 和帧长相关
                    high_freq_mel = (2595 * np.log10(1 + (fs / 2) / 700))  # 把 Hz 变成 Mel
                    mel_points = np.linspace(low_freq_mel, high_freq_mel,
                                             nfilt + 2)  # 将梅尔刻度等间隔(在low_freq_mel和high_freq_mel值之间生成nfilt + 2个等间隔数据)
                    hz_points = (700 * (10 ** (mel_points / 2595) - 1))  # 把 Mel 变成 Hz
                    bin = np.floor((NFFT + 1) * hz_points / fs)  # np.floor函数返回不大于参数的最大整数
                    fbank = np.zeros((nfilt, int(np.floor(NFFT / 2 + 1))))
                    # 实现Mel滤波器组
                    for m in range(1, nfilt + 1):
                        f_m_minus = int(bin[m - 1])  # Mel滤波器组的最低频率
                        f_m = int(bin[m])  # Mel滤波器组的中心频率
                        f_m_plus = int(bin[m + 1])  # Mel滤波器组的最低频率
                        # 计算每个带通滤波器的传递函数
                        for k in range(f_m_minus, f_m):
                            fbank[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
                        for k in range(f_m, f_m_plus):
                            fbank[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])
                    filter_banks = np.dot(yf[0:1025],fbank.T)  # dot()返回的是两个数组的点积，如果处理的是一维数组，则得到的是两数组的內积，如果是二维数组（矩阵）之间的运算，则得到的是矩阵积
                    filter_banks = np.where(filter_banks == 0, np.finfo(float).eps,filter_banks)  # np.where函数，当filter_banks == 0为真时，选择np.finfo(float).eps（finfo函数是根据括号中的类型来获得信息，获得符合这个类型的数型，eps为当数为负数或0时取非负数的最小整数），否则选择filter_banks
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
                    num_ceps = 12  # 通常，对于自动语音识别（ASR），所得到的倒谱系数2-13被保留，其余的被丢弃; num_ceps = 12。丢弃其他系数的原因是它们表示滤波器组系数的快速变化，并且这些细节不会有助于自动语音识别（ASR）。
                    c2 = dct(filter_banks, type=2, axis=-1, norm='ortho')[1: (num_ceps + 1)]  # 调用dct函数
                    c2 *= w
                    mfcc_data.append(c2)  # 将数据添加到mfcc_data

                # np.savetxt("mfcc.txt",lif,fmt='%d')
                np.savetxt(output, mfcc_data)
                # endTime = time.process_time()
                # print("运行时间为:%f s" % (endTime - startTime))
                mfcc_data1 = np.array(mfcc_data)
                mfcc_data2 = mfcc_data1[:, 0]
                plt.plot(mfcc_data2)
                plt.show()
if __name__ == "__main__":
    main(sys.argv)

#python wavtomfcc.py -h
#python wavtomfcc.py -i English.wav -o English_wavtomfcc.txt -f 2048 -l 1024
#python wavtomfcc.py -i English.wav -o English_wavtomfcc.txt --framelength 2048 --overlap 1024
#python wavtomfcc.py -i English.wav -o mfcc.txt -f 2048 -l 1024