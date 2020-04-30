import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
#定义一个占位符
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1,input2)
#会话
with tf.Session()as sess:
    #前面先使用占位符占float32位的位置，在运行时赋值
   print(sess.run(output,feed_dict={input1:[8.0],input2:[2.0]}))
