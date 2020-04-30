#语音数据进行fft(调包，只能处理大于1列数据的数据文件)
import numpy as np
import getopt
import sys
import wave
'''
    说明：本程序对输入数据为1列时能使用自己编写的fft程序进行fft，但运行效率较低，输入较大数据量不容易运行出来，同时也能调fft包实现，且效率较高
    对输入数据数据列数不为1列时只能调fft包进行fft(即自己编写的fft程序对输入数据为多列时不适用)
'''
'''
def fft1(wave_data1):
    fft_data=[]
    k1 = np.arange(0, 80, 1) #采样点数
    x=len(wave_data1)
    print('数据个数=',x)
    N=len(k1)
    print('数据个数',N)
    for j in k1:
        fft_data1=0
        for i in range(0, 80):
            for k in range(0,20):
                for m in range(0,4):
                    fft_data1=fft_data1+wave_data1[k,m]*complex(np.cos(2*np.pi*i*j/N),-np.sin(2*np.pi*i*j/N)) #f=j*fs/N ; t=i/fs
        fft_data.append(fft_data1)
    fft_data = np.array(fft_data)
    return fft_data
'''
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
        print('命令行运行方式：python wavtxtfft.py -i Englishframe1.txt -o fft_Englishframe1.txt')
        sys.exit()

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("对音频数据进行FFT变换")
            print('命令行运行方式：')
            print('Englishframe1.txt为分帧后的语音数据')
            print('对分帧数据运行：python wavtxtfft.py -i Englishframe1.txt -o fft_Englishframe1.txt')
            print('English.txt为1列的原始语音数据')
            print('原始语音数据运行：python wavtxtfft.py -i English.txt -o fft_English.txt')
            print('test.txt为截取的English.txt的前256行数据')
            print('调包实现：python wavtxtfft.py -i test.txt -o fft_test1.txt')
            print('自己编写的fft程序实现：python wavtxtfft.py -i test.txt -o fft_test2.txt')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg

            wave_data = np.loadtxt(input, dtype=np.short)  #读取文件数据
            #wave_data = np.loadtxt(input, dtype=np.float32)
            #print(wave_data)
            # data = wave_data / np.max(wave_data)   # 归一化
            # fft_signal = np.fft.fft(data)

            fft_data = np.fft.fft(wave_data)
            #fft_data = fft1(wave_data)  #自己编写的dft函数，但只能处理一列的数据文件，且运行效率很低
            #print(fft_data)
            length = len(fft_data.T)#得到数据文件列数，（前提是数据不止一列，如果数据只有一列，则得到的是数据的个数）
            #print('文件列数=',length)
            fft_len = len(fft_data)#数据文件行数
            print('文件行数=',fft_len)
            file = open(output, 'w+')
            m = (fft_data.T).ndim  # 判断数据是一维还是多维（对数据取转置，再判断维度，即判断输入数据列数为1列还是多列，1列和多列处理方法不一样）
            if m == 1:  # 如果数据为1列
                print('文件列数=1')
                for i in range(fft_len):
                    s = str(fft_data[i]).replace('[', ").replace('[',")
                    s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                    s = s.replace("'", ").replace(',',")  # 去除单引号，逗号
                    file.write(s)  # 数据存文件
                    file.write('\n')  # 每行读取完以后换行
                file.close()
            else:
                print('文件列数=', length)
                for i in range(fft_len):
                    for j in range(length):
                    #for j in range(4):
                        s = str(fft_data[i,j]).replace('[', '').replace(']','')
                        #s = str(fft_data[i, j]).replace('[', ").replace(']',")
                        s = s.replace('(', '').replace(')', '') + ' '  # 去除小括号，每个数据加空格
                        s = s.replace("'", '').replace(',','')

                        file.write(s)    #数据存文件
                    file.write('\n')  # 每行读取完以后换行
                file.close()


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])

#English.txt为1列的原始语音数据
#python wavtxtfft.py -i English.txt -o fft_English.txt
#Englishframe1.txt为分帧后的语音数据
#python wavtxtfft.py -i Englishframe1.txt -o fft_Englishframe1.txt
#test.txt为截取的English.txt的前256行数据
#python wavtxtfft.py -i test.txt -o fft_test1.txt
#python wavtxtfft.py -i test.txt -o fft_test2.txt
#python wavtxtfft.py -i Englishframe_for_mfcc.txt -o Englishfft_for_mfcc.txt