#将极坐标数据，转换到直角坐标，还原为fft原始数据
import numpy as np
import getopt
import sys

def main(argv):
    try:
         opts, args = getopt.getopt(sys.argv[1:], "-i:-o:-h", ["input=", "output=","help"])
    except getopt.GetoptError:
        print('将极坐标数据，转换到直角坐标，还原为fft原始数据')
        print('python polartxtfft.py -i fft_test1_polar.txt -o polar_test1_fft.txt')
        sys.exit()

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("将极坐标数据，转换到直角坐标，还原为fft原始数据")
            print('输入格式为：')
            print('python polartxtfft.py -i fft_test1_polar.txt -o polar_test1_fft.txt')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg

            polar_data = np.loadtxt(input, dtype=np.float)  #加载数据文件，读入数据，数据类型为float，不能为short
            polar_data_len = len(polar_data)  # 输入数据长度
            #m = (polar_data.T).ndim  #判断数据是一维还是多维（对数据取转置，再判断维度，即判断输入数据列数）
            file = open(output, 'w+')  #打开输出文件

            # 循环读取每行数据，将极坐标转为直角坐标，还原为fft原始数据
            for i in range(polar_data_len):
                Amplitude = polar_data[i,0]  #取极坐标的幅值，即模
                angle = polar_data[i,1]  #取极坐标的角度，即相位
                #print(Amplitude, angle)
                angle = angle*(np.pi/180)  #角度转弧度（因为下面cos函数计算时，是按照弧度计算的）
                data_real = Amplitude*np.cos(angle)  #计算实部
                data_imag = Amplitude*np.sin(angle)  #计算虚部
                #如下判断语句主要用于判断复数的虚部是否大于零，从而判断虚部前是否需要加"+"号，因为负数前面不需要加"+"号
                if(data_imag>0):   #复数的虚部大于零，则虚部前加"+"号
                    complex_data = str(data_real) + '+' + str(data_imag) + 'j' + '\n'  # 将幅度和相位数据中间加空格和@符号
                elif(data_imag<0):  #复数的虚部小于零，则虚部前不加"+"号
                    complex_data= str(data_real) + str(data_imag) + 'j' + '\n'  #将幅度和相位数据中间加空格和@符号
                else:    #复数的虚部等于零，取绝对值后再在虚部前加"+"号
                    complex_data = str(data_real)  + '+' + str(abs(data_imag)) + 'j' + '\n'  # 将幅度和相位数据中间加空格和@符号
                file.write(complex_data)  #将每行数据写入文件
            file.close()


if __name__ == "__main__":
    main(sys.argv)  #调用函数


#python polartxtfft.py -i fft_test1_polar.txt -o polar_test1_fft.txt
