#语音数据进行ifft(调包和不调包)
import numpy as np
import getopt
import sys
import wave
'''
    说明：本程序对输入数据为1列和多列时均能调ifft包进行傅里叶逆变换，但自己编写的ifft程序未能正确实现ifft
'''
def ifft1(fft_data):
    fft_data = fft_data.conjugate()  # 取共轭复数
    ifft_data=[]
    k1 = np.arange(0, len(fft_data), 1) #采样点数
    x=len(fft_data)
    print('数据个数=',x)
    N=len(k1)
    #print('数据个数',N)
    for i in range(0, len(fft_data)):
        fft_data1=0
        for j in k1:
            fft_data1=fft_data1+(1/(2*np.pi))*fft_data[j]*complex(np.cos(2*np.pi*i*j/N) ,-np.sin(2*np.pi*i*j/N)) #f=j*fs/N ; t=i/fs
        ifft_data.append(fft_data1)
    ifft_data = np.array(ifft_data)
    return ifft_data
def main(argv):
    try:
         opts, args = getopt.getopt(argv, "-i:-o:h", ["input=", "output=","help"])
    except getopt.GetoptError:
        print('输入格式错误，输入为语音数据文件，输出为进行ifft变换之后的数据文件')
        print('命令行运行方式：python wavtxtifft.py -i fft_Englishframe1.txt -o ifft_Englishframe1.txt')
        sys.exit()

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("对音频数据进行IFFT变换")
            print('命令行运行方式：')
            print('分帧数据ifft变换：python wavtxtifft.py -i fft_Englishframe1.txt -o ifft_Englishframe1.txt')
            print('1列的数据调包实现ifft：python wavtxtifft.py -i fft_test1.txt -o ifft_test1.txt')
            print('1列的数据不调包实现ifft：python wavtxtifft.py -i fft_test1.txt -o ifft_test2.txt')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg

            #wave_data = np.loadtxt(input, dtype=np.short)  #读取文件数据
            fft_data = np.loadtxt(input, dtype=np.complex)  #输入数据格式为complex
            print('原始fft数据:\n',fft_data)
            # data = wave_data / np.max(wave_data)   # 归一化
            # fft_signal = np.fft.fft(data)

            #ifft_data = np.fft.ifft(fft_data)
            ifft_data = ifft1(fft_data)  # 自己编写的ifft函数，但只能处理一列的数据文件，且运行效率很低


            ifft_data = np.real(ifft_data)  # 取出实部
            ifft_data = np.round(ifft_data)  # 返回浮点数的四舍五入值。
            print('ifft变换后的数据:\n',ifft_data)
            length = len(ifft_data.T)#得到数据文件列数，（前提是数据不止一列，如果数据只有一列，则得到的是数据的个数）
            print('文件列数=',length)
            fft_len = len(ifft_data)#数据文件行数
            print('文件行数=',fft_len)
            file = open(output, 'w+')
            m = (ifft_data.T).ndim  # 判断数据是一维还是多维（对数据取转置，再判断维度，即判断输入数据列数为1列还是多列，1列和多列处理方法不一样）
            if m==1:  #如果数据为1列
                for i in range(fft_len):
                    s = str(ifft_data[i]).replace('[', ").replace('[',")
                    s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                    s = s.replace("'", ").replace(',',") + '\n'  # 去除单引号，逗号，每行末尾追加换行符
                    s = float(s)
                    s = int(s)
                    s = str(s)
                    file.write(s)  # 数据存文件
                    file.write('\n')  # 每行读取完以后换行
                file.close()
            else:  #数据列数大于1列
                for i in range(fft_len):
                    for j in range(length):
                    #for j in range(4):
                        s = str(ifft_data[i,j]).replace('[', '').replace(']','')
                        s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                        s = s.replace("'", '').replace(',','')
                        s = float(s)
                        s = int(s)
                        s = str(s)
                        file.write(s)    #数据存文件
                        file.write(' ')  #每个数据写入后，在数据后面加个空格
                    file.write('\n')  # 每行读取完以后换行
                file.close()


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])


#python wavtxtifft.py -i fft_Englishframe1.txt -o ifft_Englishframe1.txt
#fft_test1.txt为程序5进行fft之后得到的fft变换数据
#python wavtxtifft.py -i fft_test1.txt -o ifft_test1.txt
#python wavtxtifft.py -i fft_test1.txt -o ifft_test2.txt
'''
逆向快速傅里叶变换(IFFT)的计算原理是将频域（注意频域是复数）数据进行取共轭复数（虚部取反），
然后再进行FFT变换，这样便将频域信号转换到时域。
因为FFT变换的结果是复数，所以从频域进行FFT变换过来的结果也是复数，而此时只需取复数的实部，便是原时域信号。

先将要做Ifft的数据取共轭，然后fft，
结果再除以N（N为数据长度），结果就是ifft的结果。不过和直接ifft算法相比有精度上的误差。
'''