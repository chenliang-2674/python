import wave
import numpy as np
import sys
import getopt

def main(argv):
    """
        通过 getopt模块 来识别参数demo
    """

    try:
        """
            options, args = getopt.getopt(args, shortopts, longopts=[])

            参数args：一般是sys.argv[1:]。过滤掉sys.argv[0]，它是执行脚本的名字，不算做命令行参数。
            参数shortopts：短格式分析串。例如："hp:i:"，h后面没有冒号，表示后面不带参数；p和i后面带有冒号，表示后面带参数。
            参数longopts：长格式分析串列表。例如：["help", "ip=", "port="]，help后面没有等号，表示后面不带参数；ip和port后面带冒号，表示后面带参数。

            返回值options是以元组为元素的列表，每个元组的形式为：(选项串, 附加参数)，如：('-i', '192.168.0.1')
            返回值args是个列表，其中的元素是那些不含'-'或'--'的参数。
        """
        #opts, args = getopt.getopt(argv, "hi:p:rl", ["help", "input=", "password=","right","left"])
        opts, args = getopt.getopt(argv, "hi:o:lrA", ["help", "input=", "output=","left","right","all"])
    except getopt.GetoptError:
        print('双声道:python holiday02.py -i lanTian2.wav -o wavData.txt -l')
        print('or双声道:python holiday02.py --input=lanTian2.wav --output=wavData.txt --all')
        print('单身道:python holiday02.py -i BAC009S0003W0121.wav -o wavData.txt')
        sys.exit(2)

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('双声道:python holiday02.py -i lanTian2.wav -o wavData.txt -l')
            print('or双声道:python holiday02.py --input=lanTian2.wav --output=wavData.txt --all')
            print('单身道:python holiday02.py -i BAC009S0003W0121.wav -o wavData.txt')
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg

            f = wave.open(input, 'rb')
            params = f.getparams()  # get wave file params
            nchannels, sampwidth, framerate, nframes = params[:4]
            print("wav params is :", params)

            # open a txt file
            #file = open("wavData.txt", 'w')
            file = open(output, 'w')
            data = f.readframes(nframes)
            # 将字符串转换为数组，得到一维的short类型的数组
            data = np.fromstring(data, dtype=np.short)
            # 整合左声道和右声道的数据
            data = np.reshape(data, [nframes, nchannels])  #将采样数据规整为每行nchannels个数据，如果为单声道，每行一个数据，如果双声道，每行就两个数据
            j=0#用j来判断左右声道数据
            length=len(data)#该段语音有多少个采样点


            #左声道j=0
        elif opt in ("-l", "--left"):
            #data=data[:,0]
            j=0
        elif opt in ("-r", "--right"):
            #data=data[:,1]
            j=1#右声道j=1
        elif opt in ("-A", "--all"):
            for i in range(length):
                # s = str(data[i, 0]).replace('[', ").replace('[',")
                #同时打印左右声道数据，中间空格分开
                s = str(data[i, 0]).replace('[', ").replace('[',")+' '+str(data[i, 1]).replace('[', ").replace('[',")
                s = s.replace("'", ").replace(',',") + '\n'  # 去除单引号，逗号，每行末尾追加换行符
                file.write(s)
            file.close()
            f.close()
            exit()#为了不影响下面的，如若没有exit，打完双声道左右数据，还会打印单声道一列数据
            #file.close()
            '''
            在这里需要考虑到左右声道数据同时打印在txt文件，和分别打印，只定义j没能实现，定义了两次for循环
            将file和f关闭，防止下面打印左右声道又关闭依次，不然报错ValueError: I/O operation on closed file.
            '''
            #f.close()  # close wave file
            #break

    for i in range(length):
        # s = str(bins[i,0]).replace('[',").replace('[',")+'\t'+str(data[i]).replace('[',").replace('[',")#去除[],这两行按数据不同，可以选择
        # s = str(data[i, 0]).replace('[', ").replace('[',")
        s = str(data[i,j]).replace('[', ").replace('[',")
        s = s.replace("'", ").replace(',',") + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()

    f.close()  # close wave file


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    main(sys.argv[1:])


#python holiday02.py -i BAC009S0003W0121.wav
#python holiday02.py -i lanTian2.wav -l
#python holiday02.py -i lanTian2.wav -o wavData.txt -l



