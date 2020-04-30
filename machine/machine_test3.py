import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
#生成200个在区间[-0.5,0.5]之间的均匀分布的点
x_data = np.linspace(-0.5,0.5,200) [:,np.newaxis]
#print(x_data)
#生成均值为0，方差为0.2的形式同x_data的数据作为噪声
noise = np.random.normal(0,0.02,x_data.shape)
y_data = np.square(x_data) + noise
#标准二次函数，用于检验模型迭代结果
y1_data = np.square(x_data)
#定文两个占位符
x = tf. placeholder(tf.float32,[None,1])
y = tf. placeholder(tf.float32,[None,1])

'''
tf.random_normal()函数用于从“服从指定正态分布的序列”中随机取出指定个数的值。
tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
    shape: 输出张量的形状，必选
    mean: 正态分布的均值，默认为0
    stddev: 正态分布的标准差，默认为1.0
    dtype: 输出的类型，默认为tf.float32
    seed: 随机数种子，是一个整数，当设置之后，每次生成的随机数都一样
    name: 操作的名称
'''
#定文神经网络中间层
#Weights_L1为权重，biases_L1为偏置
Weights_L1 = tf.Variable(tf.random_normal([1,10]))
biases_L1 = tf.Variable(tf.zeros([1,10]))
#tf. matmul为两个矩阵相乘，tf.multiply为矩阵对应元素相乘
Wx_plus_b_Ll = tf. matmul(x,Weights_L1) + biases_L1
#tf.nn.tanh为双曲正切曲线函数，表达式为：(e^(x)-e^(-x))/(e^(x)+e^(-x))
L1 = tf.nn.tanh(Wx_plus_b_Ll)

#定义神经网络输出层
Weights_L2 = tf.Variable(tf.random_normal([10,1]))
biases_L2 = tf.Variable(tf.zeros([1,1]))
Wx_plus_b_L2 = tf. matmul (L1, Weights_L2) + biases_L2
prediction = tf.nn.tanh(Wx_plus_b_L2)

#二次代价函数
#梯度下降法进行优化
loss = tf.reduce_mean(tf.square(y-prediction))
optiminizer = tf.train.GradientDescentOptimizer(learning_rate=0.4)
train_step = optiminizer.minimize(loss)
#变量初始化
init = tf.global_variables_initializer()
with tf.Session()as sess:
    sess.run(init)
    for _ in range(2000):
        sess.run(train_step,feed_dict={x:x_data,y:y_data})
    #print(x_data)
    #print(prediction)
    #获得预测值
    prediction_value = sess.run(prediction,feed_dict={x:x_data})
   # print(prediction_value)

    #画图
    #解决图中显示中文问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure()
    #画原始数据散点图
    plt.scatter(x_data,y_data)
    #plt.plot(x_data,prediction_value,'r-',label = '预测的二次函数图',lw=4)
    #plt.plot(x_data, y1_data, 'b-', label = '原始真实二次函数图',lw=4)
    plt.plot(x_data, prediction_value, 'r-', lw=4)
    plt.plot(x_data, y1_data, 'b-', lw=4)
    plt.xlabel('x_data')
    plt.ylabel('y_data')
    plt.title(u'二次函数模型迭代预测')
    plt.show()