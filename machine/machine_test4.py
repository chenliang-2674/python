import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
#载入数据集
mnist = input_data.read_data_sets('C:/Users/CL/Desktop/学习/python/machine/data/MNIST_data',one_hot=True)  #one-hot编码把分类数据转化为二进制格式，供机器学习使用。
#每个批次的大小
batch_size = 50
#计算一共有多少个批次
n_batch = mnist.train.num_examples//batch_size

#定义两个placeholder，784为图片尺寸，图片为28x28，将图片展开成一维向量就是784,
x = tf. placeholder(tf.float32,[None,784])
#输出为10个神经元，偏置值为10
y = tf. placeholder(tf.float32,[None,10])

#创建一个简单的神经网络
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
#Softmax就是把一个N*1的向量归一化为（0，1）之间的值，由于其中采用指数运算，使得向量中数值较大的量特征更加明显。
#prediction = tf.matmul(x,W)+b
prediction = tf.nn.softmax(tf.matmul(x,W)+b)

#二次代价函数
#loss = tf.reduce_mean(tf.square(y-prediction))
#交叉熵
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
#使用梯度下降法
optiminizer = tf.train.GradientDescentOptimizer(learning_rate=0.4)
train_step = optiminizer.minimize(loss)

#初始化变量
init = tf.global_variables_initializer()

#结果存放在一个布尔型列表中
#tf.argmax(y,1)表示矩阵y按照行取每行最大值所在位置(即取每行最大值，即概率最大的，即为图片的标签)，0为按列取。tf.equal比较两个值是否相等，相等返回True，否则返回false
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))
#求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))  #tf.cast是将布尔型数据即true和false转化为1和0。再求平均值，即为准确率

with tf.Session()as sess:
    sess.run(init)
    for epoch in range(21):    #21代表训练21次
        for batch in range(n_batch):  #n_batch代表总共有多少个批次
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)  #batch_xs存放图片一维数据，batch_ys存放图片标签，每获得一个批次图片的数据，就run一下进行训练，每批次训练21次
            sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})  #将数据传入进行训练
        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("Iter"+str(epoch)+",Test_accuracy:"+str(acc))