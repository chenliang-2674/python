'''
   import tensorflow as tf
   import keras  #引入keras
   #sess = tf.compat.v1.Session()

   a = tf.compat.v1.constant(10)
   b= tf.compat.v1.constant(12)
   sess.run(a+b)
   sess.close()
   keras.backend.clear_session()



   a = tf.constant([[0, 1, 2, 3], [4, 5, 6, 7]], dtype=tf.float32)
   a_rank = tf.rank(a) # 获取张量的秩
   a_shape = tf.shape(a) # 获取张量的形状
   b = tf.reshape(a, [4, 2]) # 对张量进行重构
   # 运行会话以显示结果
   with tf.Session() as sess:
      print('constant tensor: {}'.format(sess.run(a)))
      print('the rank of tensor: {}'.format(sess.run(a_rank)))
      print('the shape of tensor: {}'.format(sess.run(a_shape)))
      print('reshaped tensor: {}'.format(sess.run(b)))
      # 对张量进行切片
      print("tensor's first column: {}".format(sess.run(a[:, 0])))
   keras.backend.clear_session()
'''

'''
import tensorflow as tf
import keras  #引入keras
from keras.backend.tensorflow_backend import set_session
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)
set_session(sess)
keras.backend.clear_session() #此句代码分量很重
'''
'''
import tensorflow as tf
import keras
from future import absolute_import, division, print_function, unicode_literals
#查看tensorflow版本
print(tf.__version__)
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)
'''


'''
import tensorflow as tf
#创建一个常量op
m1=tf.constant([[3,3]])
m2=tf.constant([[2],[3]])
product = tf.matmul(m1,m2)  #matmul是两个矩阵相乘
print(product)
#下面两段程序等价
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

with tf.Session()as sess:
   result = sess.run(product)
   print(result)
'''


import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error
#定义一个变量
x = tf.Variable([1,2])
#定义一个常量
a = tf.constant([2,3])
#减法
sub = tf.subtract(x,a)
#加法
add = tf.add(x,a)
#变量初始化
init = tf.global_variables_initializer()
#会话
with tf.Session()as sess:
   sess.run(init)
   print(sess.run(sub))
   print(sess.run(add))