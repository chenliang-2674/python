import math
import time

start = time.time()
for i in range(10000000):
    y = math.sin(3.14)
end = time.time()
print("耗时{0}".format(end-start))
   # print(y)
