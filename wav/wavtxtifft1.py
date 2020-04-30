#语音数据进行fft（不调包，但只能处理一列数据的数据文件）
import numpy as np
import getopt
import sys
import wave

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
        print('输入格式错误，输入为语音数据文件，输出为进行fft变换之后的数据文件')
        print('命令行运行方式：python wavtxtifft1.py -i fft_test1.txt -o ifft_test1.txt')
        sys.exit()

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("对音频数据进行FFT变换，原始语音数据为一行一个数据的形式")
            print('命令行运行方式：python wavtxtifft1.py -i fft_test1.txt -o ifft_test1.txt')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg

            fft_data = np.loadtxt(input, dtype=np.complex)
            #fft_data = np.array(fft_data)  # 转换成数组
            #wave_data = np.loadtxt(input, dtype=np.float32)
            #print('原始语音数据：\n',fft_data)

            #ifft_data = np.fft.ifft(fft_data)  #调用fft包
            ifft_data = ifft1(fft_data)  # 自己编写的ifft函数，但只能处理一列的数据文件，且运行效率很低
            ifft_data = np.real(ifft_data)  # 取出实部
            ifft_data = np.round(ifft_data)  # 返回浮点数的四舍五入值。
            #print('ifft变换后的数据:\n',ifft_data)
           # file = open(output, 'w+')
            #file.write(str(ifft_data))  # 数据存文件
           # file.write('\n')  # 每行读取完以后换行
            #file.close()

            #length = len(fft_data.T)#得到数据文件列数，（前提是数据不止一列，如果数据只有一列，则得到的是数据的个数）
            #print('文件列数=',length)
            ifft_len = len(ifft_data)#数据文件行数
            print('文件行数=',ifft_len)
            file = open(output, 'w+')
            for i in range(ifft_len):
                #for j in range(length):
                #for j in range(4):
                s = str(ifft_data[i])
                if (i==0):
                    s = str(ifft_data[i]).replace('[', '')
                    s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                    s = s.replace("'", '').replace(',', '')
                elif (i==ifft_len-1):
                    s = str(ifft_data[i]).replace('[', '')
                    s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                    s = s.replace("'", '').replace(',', '')
                s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                s = s.replace("'", '').replace(',', '')
                s = float(s)
                s = int(s)
                s = str(s)
                file.write(s)  # 数据存文件
                file.write('\n')  # 每行读取完以后换行
            file.close()


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])


#python wavtxtifft1.py -i fft_test1.txt -o ifft_test1.txt
#python wavtxtifft1.py -i fft_test1.txt -o ifft_test2.txt
