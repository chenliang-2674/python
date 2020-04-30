import tensorflow as tf
import numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
#原始模型
x_data = np.random.rand(100)
y_data = x_data*0.1+0.2

#构造一个线性模型
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k*x_data + b

#二次代价函数
#梯度下降法进行优化
loss = tf.reduce_mean(tf.square(y_data-y))

optiminizer = tf.train.GradientDescentOptimizer(learning_rate=0.4)
#最小化代价函数
train = optiminizer.minimize(loss)

#变量初始化
init = tf.global_variables_initializer()
#会话
with tf.Session()as sess:
    sess.run(init)
    for step in range(1000):
        #每次run一下train,更新一下train的值
          sess.run(train)
          #每100次打印一次结果
          if step%100 == 0:
              print(step,sess.run([k,b]))