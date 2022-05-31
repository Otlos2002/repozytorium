import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Zadanie 1
# x = np.arange(-5,6)
# plt.plot(x,x**2-4*x,label='x^2-4x')
# plt.title('Wykres funkcji f(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.yticks([-5,-3,-1,1,3,5])
# plt.show()

#Zadanie 2
# ax1 = plt.subplot(311)
# x1 = np.arange(4,10)
# x2 = np.arange(0,10,0.1)
# f1 = np.sqrt(x1)
# f2 = np.cos(x2)+0.4
# lab = r"$f(x)=\sqrt{x}$"
# ax1.bar(x1,f1,label=lab)
# ax1.set_xlabel('x')
# ax1.set_ylabel('wyniki funkcji')
# ax1.set_title('Wykres słupkowy funkcji')
# ax1.set_label(lab)
# ax1.legend()
# 
# ax2 = plt.subplot(313)
# ax2.plot(x2,f2,'og',linewidth=5,label='cos(x)+0.4')
# ax2.set_title('Wykres cos(x)+0.4')
# ax2.set_xlabel('x')
# ax2.set_ylabel('cos(x)+0.4')
# ax2.legend()
# plt.savefig('tytol.png')
# plt.show()


#Zadanie 3
# df = pd.read_csv('../cars.csv',sep=';',decimal='.')
# df2 = df.sample(100)
# df2 = df2.groupby('Cylinders')
# etykiety = list(df2.groups.keys())
# wartosci = list(df2.agg('Cylinders').count())
# print(etykiety)
# print(wartosci)
# plt.pie(x=wartosci,labels=etykiety,autopct="%1.1f%%")
# plt.show()

#Zadanie 4
# df = pd.read_csv('../iris.data',header=0,sep=',',decimal='.')
# sns.scatterplot(data=df,x='petal length',y='petal width',hue='class',palette=['red','green','blue'])
# plt.show()
