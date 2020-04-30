# 高斯混合模型男生女生身高
import numpy as np
import matplotlib.pyplot as plt
#产生身高数据
def Normal(x,mu,sigma):#返回一个正态分布的概率密度函数
    return np.exp(-(x-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)
np.random.seed(100)  # 固定随机数种子，确保下次运行数据相同
#产生服从正态分布的随机数
boy=np.random.normal(180,np.sqrt(20),6000)
girl=np.random.normal(165,np.sqrt(15),4000)
data=np.concatenate((boy,girl)) #将生成的两组服从正态分布的随机数拼接在一起
N=len(data)
mu1=140;sigma1=10;w1=0.6#对男生身高均值，方差，权重赋初值
mu2=130;sigma2=5;w2=0.4#对女生身高均值，方差，权重赋初值
i=0
while(i!=10000):#用EM算法迭代求参数估计
    i+=1
    gauss1=Normal(data,mu1,np.sqrt(sigma1))#根据初值得到的一个正态分布的概率密度函数
    gauss2=Normal(data,mu2,np.sqrt(sigma2))#根据初值得到的一个正态分布的概率密度函数
    Gamma1=w1*gauss1
    Gamma2=w2*gauss2
    M=Gamma1+Gamma2
    #更新Sigma
    #sigma1=np.dot((Gamma1/M).T,(data-mu1)**2)/np.sum(Gamma1/M)   #np.dot函数：矩阵的乘法
    #sigma2=np.dot((Gamma2/M).T,(data-mu2)**2)/np.sum(Gamma2/M)  #np.dot函数：矩阵的乘法
    sigma1 = np.sum(np.dot((Gamma1 / M).T, (data - mu1) ** 2)) / np.sum(Gamma1 / M)  # np.dot函数：矩阵的乘法
    sigma2=np.sum(np.dot((Gamma2/M).T,(data-mu2)**2))/np.sum(Gamma2/M)  #np.dot函数：矩阵的乘法
    #更新mu
    #mu1=np.dot((Gamma1/M).T,data)/np.sum(Gamma1/M)
    #mu2=np.dot((Gamma2/M).T,data)/np.sum(Gamma2/M)
    mu1 = np.sum(np.dot((Gamma1 / M).T, data)) / np.sum(Gamma1 / M)
    mu2 = np.sum(np.dot((Gamma2 / M).T, data)) / np.sum(Gamma2 / M)
    #更新w1w2
    w1=np.sum(Gamma1/M)/N
    w2=np.sum(Gamma2/M)/N
x1 = np.arange(0,350,1)
y1 = np.exp(-((x1 - mu1)**2)/(2*sigma1**2)) / (sigma1 * np.sqrt(2*np.pi))
#plt.plot(nan)
#plt.subplot(211)
plt.plot(x1,y1,color='g',linestyle='-',label='boy')
#plt.ylabel('boy')
x2 = np.arange(0,330,1)
y2 = np.exp(-((x2 - mu2)**2)/(2*sigma2**2)) / (sigma2 * np.sqrt(2*np.pi))
#plt.plot(nan)
#plt.subplot(212)
plt.plot(x2,y2,color='r',linestyle='-',label='girl')
#plt.ylabel('girl')
#plt.plot(x,gauss1)
plt.show()

print ("迭代",i,"次")
print ("男生身高迭代后的均值:",mu1,"女生身高迭代后的均值：",mu2)
print ("男生身高迭代后的方差:",sigma1,"女生身高迭代后的方差:",sigma2)
print ("权重迭代w1:",w1,"权重迭代w2:",w2)