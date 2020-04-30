#语音数据进行fft（不调包，但只能处理一列数据的数据文件）
import numpy as np
import getopt
import sys
import wave

def fft1(wave_data1):
    fft_data=[]
    k1 = np.arange(0, len(wave_data1), 1) #采样点数
    x=len(wave_data1)
    print('数据个数=',x)
    N=len(k1)
    #print('数据个数',N)
    for j in k1:
        fft_data1=0
        for i in range(0, len(wave_data1)):
            fft_data1=fft_data1+wave_data1[i]*complex(np.cos(2*np.pi*i*j/N),-np.sin(2*np.pi*i*j/N)) #f=j*fs/N ; t=i/fs
        fft_data.append(fft_data1)
    fft_data = np.array(fft_data)
    return fft_data

def main(argv):
    try:
         opts, args = getopt.getopt(argv, "-i:-o:h", ["input=", "output=","help"])
    except getopt.GetoptError:
        print('输入格式错误，输入为语音数据文件，输出为进行fft变换之后的数据文件')
        print('命令行运行方式：python wavtxtfft1.py -i test.txt -o fft_test2.txt')
        sys.exit()

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("对音频数据进行FFT变换，原始语音数据为一行一个数据的形式")
            print('命令行运行方式：python wavtxtfft1.py -i test.txt -o fft_test1.txt')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg

            wave_data = np.loadtxt(input, dtype=np.short)
            #wave_data = np.loadtxt(input, dtype=np.float32)
            print('原始语音数据：\n',wave_data)
            # data = wave_data / np.max(wave_data)   # 归一化
            # fft_signal = np.fft.fft(data)

            fft_data = np.fft.fft(wave_data)  #调用fft包
            #fft_data = fft1(wave_data)  #自己编写的dft函数，但只能处理一列的数据文件，且运行效率很低
            print('fft变换后的数据:\n',fft_data)
            file = open(output, 'w+')
            file.write(str(fft_data))  # 数据存文件
           # file.write('\n')  # 每行读取完以后换行
            file.close()

        #fft_data = fft(wave_data)
            #fft_data = fft_signal.T  # 转置是为了下面打印与fft的结果一致

            #length = len(fft_data.T)#得到数据文件列数，（前提是数据不止一列，如果数据只有一列，则得到的是数据的个数）
            #print('文件列数=',length)
            fft_len = len(fft_data)#数据文件行数
            print('文件行数=',fft_len)
            file = open(output, 'w+')
            for i in range(fft_len):
                #for j in range(length):
                #for j in range(4):
                s = str(fft_data[i])
                if (i==0):
                    s = str(fft_data[i]).replace('[', '')
                    s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                    s = s.replace("'", '').replace(',', '')
                elif (i==fft_len-1):
                    s = str(fft_data[i]).replace('[', '')
                    s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                    s = s.replace("'", '').replace(',', '')
                s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                s = s.replace("'", '').replace(',', '')
                file.write(s)  # 数据存文件
                file.write('\n')  # 每行读取完以后换行
            file.close()


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])


#python wavtxtfft1.py -i test.txt -o fft_test1.txt
#python wavtxtfft1.py -i test.txt -o fft_test2.txt
