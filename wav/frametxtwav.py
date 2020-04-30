#将分帧之后的语音数据还原为分帧之前的语音数据
import numpy as np
import sys
import wave   #语音文件处理包
import getopt
import re

def main(argv):  # 定义一个函数
    try:  # 首先执行try后的程序，如果输入格式不对，则执行except getopt.GetoptError:后的程序
        opts, args = getopt.getopt(argv, "i:o:-f:-l:h",["input", "output", "framelength=", "overlap=", "help"])  # 命令行输入参数
    except getopt.GetoptError:
        print('输入参数错误，输入格式为:python frametxtwav.py -i Englishframe2.txt -o Englishframetxtwav.txt --framelength 8 --overlap 4，\n其中frametxtwav.py为程序文件名称，程序功能是通过分帧后的数据得到原始语音数据，Englishframe2.txt为分帧后的数据文件， Englishframetxtwav.txt为还原的语音数据文件，\n --framelength为分帧的帧长，--overlap为帧移')
        sys.exit()
    # global file
    for opt, arg in opts:
        if opt in ("-h", "--help"):  # 打印帮助
            # test.wav为单声道语音文件，test2.wav为双声道语音文件
            print('输入格式为：')
            print('python framtxtwave.py -i Englishframe1.txt -o Englishframetxtwav1.txt --framelength 4 --overlap 2')
            print('或者：python framtxtwave.py -i Englishframe1.txt -o Englishframetxtwav1.txt -f 4 -l 2')
            print('其中frametxtwav.py为程序文件名称，程序功能是通过分帧后的数据得到原始语音数据，Englishframe2.txt为分帧后的数据文件， Englishframetxtwav.txt为还原的语音数据文件')
            print('-f/-framenlength为分帧的帧长，-l/overlap为帧移')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg  # 取命令行参数，即输入
            file1 = open(input, 'rb')  # 打开分帧后的语音数据文件
        elif opt in ("-o", "--output"):
            output = arg  # 取命令行参数，即输出
            file2 = open(output, 'w+')  # 打开用于保存分帧前的数据的txt文件
        elif opt in ("-f", "--framelength"):
            framelength = arg  # 取命令行framelength后的参数，即帧长
            framelength = int(framelength)
        elif opt in ("-l", "--overlap"):
            overlap = arg  # 取命令行overlap后的参数，即帧移
            overlap = int(overlap)
            x = overlap  #帧移,即每行中原始语音数据的长度
            line1 = file1.readline()  # 每次读出txt文件中的一行内容
            #data = []  # 初始化一个空矩阵
            print('txt文件中的数据的数据类型为:\n', type(line1))  #返回从txt文件中得到的数据的数据类型
            line = line1.decode(encoding='utf-8')  #按utf-8的方式解码，解码成字符串，因为存入txt文件的数据为bytes型，要转为str
            while line:   #当未读到文件末尾
            #for line in lines:

                #x = re.split(r' ', line)[0]  # 正则化以空格分割一行数据，取分割出来的第一个数据
                #y = re.split(r' ', line)[1]
                #line = str(x) + ' ' + str(y) + ' ' +  '\n'  # 重新写行数据
                for i in range(x):   #循环读取一行中的前x个数据
                    #content = str(re.split(r' ', line)[i]) + ' '
                    content = str(re.split(r' ', line)[i]) + '\n'    #读取文件中的前overlap列数据，即未分帧前的数据，去掉了重复的数据
                    file2.write(content)   #将数据写入另一个txt文件中
                    #content = str(re.split(r' ', line)[0]) + ' '+str(re.split(r' ', line)[1]) + ' ' +str(re.split(r' ', line)[i-1])+'\n'
                #line = str(x) + ' ' + '\n'  # 重新写行数据
                #file2.write(line)
                #file2.write(content)
                #content1 = '\n'
                #file2.write(content1)
                line1 = file1.readline()  # 每次读出txt文件中的一行内容
                line = line1.decode(encoding='utf-8')  #按utf-8的方式解码，解码成字符串,因为存入txt文件的数据为bytes型，要转为str
            file1.close()

            #获取分帧数据文件的最后一帧的framelength-overlap长度的数据，并存入文件中
            file1 = open(input, 'rb')  # 打开分帧后的语音数据文件
            line1 = file1.readlines()
            long = len(line1)
            print('文件行数为：',long)
            print('txt文件中的数据的数据类型为:\n', type(line1))  # 返回从txt文件中得到的数据的数据类型
            last_line = line1[-1].decode('utf-8')   #读取文件最后一行数据，并进行解码
            #line = last_line.decode(encoding='utf-8')  # 按utf-8的方式解码，解码成字符串，因为存入txt文件的数据为bytes型，要转为str
            for i in range(x,framelength):  # 循环读取最后一行（即最后一帧）数据的framelength-overlap长度的数据
                # content = str(re.split(r' ', line)[i]) + ' '
                content = str(re.split(r' ', last_line)[i]) + '\n'  # 读取文件中的前overlap列数据，即未分帧前的数据，去掉了重复的数据
                file2.write(content)  # 将数据写入另一个txt文件中

            file1.close()
            file2.close()
            #with open(output, 'w+') as mon:
                 #   mon.write(line)
        '''  
          while line:  # 当未读到文件最后时
                # 把切分出的列表的每个值, 把它们转成np.short型, 并返回迭代器
                num = list(map(np.short, line.split()))  # np.short
                # 用list函数把map函数返回的迭代器遍历展开成一个列表
                data.append(num)
                line = file1.readline()
            

           # file2.close()
        '''
    '''
    lines = f.readlines()
    long = len(lines)
    for line in lines:

        for i in range(4):
            line1 = line
            file.write(line1)
            print("\t")
        print("\n")

        data = np.reshape(line, [long, 4])
    file.close()  # 关闭输出文件
    f.close()  # 关闭输入的语音文件
    exit()
    '''


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])  # 调用函数

#命令行运行的命令
#python frametxtwav.py -i Englishframe1.txt -o Englishframetxtwav1.txt --framelength 4 --overlap 2
#python frametxtwav.py -i Englishframe2.txt -o Englishframetxtwav2.txt --framelength 8 --overlap 4
#python frametxtwav.py -i Englishframe1.txt -o Englishframetxtwav1.txt -f 4 -l 2
#python frametxtwav.py -i Englishframe2.txt -o Englishframetxtwav2.txt -f 8 -l 4
#python frametxtwav.py -h