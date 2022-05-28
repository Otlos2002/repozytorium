# import numpy as np
# import pandas as pd
# import matplotlib.pylab as plt
# import matplotlib.ticker as tic
# import seaborn as sns
#
# # #dziendobry
# #
# # # #zadanie 1 ------------------------------------------------------------------------
# x = np.linspace(-3, 3, 30)
# plt.plot(x, (x ** 2) + 5, 'r--s' , label='f(x)')
# plt.axis([-3, 3, 5, 14])
# plt.xlabel('x')
# plt.ylabel('f(x)', rotation=0)
# plt.title('x^2 + 5')
# plt.legend()
# plt.show()
#
# # # #zadanie 2 ------------------------------------------------------------------------
# x1 = np.linspace(0.0, 10.0, 100)
# y1 = np.cos(x1) + 0.4
# plt.subplot(3, 2, 1)
# plt.plot(x1, y1, 'r-.', label='sin(x) + 0.4')
# plt.title('Wykres sin(x) + 0.4')
# plt.xlabel('x')
# plt.ylabel('sin(x) + 0.4')
# plt.legend(loc='lower left')
#
# x2 = np.arange(1, 5 + 1)
# y2 = (x2 + 5) / 2
# plt.subplot(3, 2, 4)
# plt.bar(x=x2, height=y2, color=['blue'], label='f(x) = (x + 5) / 2)')
# plt.title('Wykres słupkowy funkcji')
# plt.xlabel('x')
# plt.ylabel('Wykres funkcji')
# plt.legend(loc='upper left')
#
# # plt.savefig('andrzej_patalon_zadanie2.png')
# #
# plt.show()
# #
# zadanie 3 ------------------------------------------------------------------------
# df = pd.read_csv('cars.csv', header=0, decimal='.', sep=';')
# df = df.head(100)
# groups = df.groupby(['Model year'])
# policzone = groups.size()
# plt.pie(x=policzone, labels=policzone.index,
#         autopct=lambda pct: "{:.0f}%".format(pct), textprops=dict(color='black', size=14), )
# plt.title('Procentowy udział lat modeli samochodów')
# plt.legend(loc='lower left')
# plt.show()
#
# #zadanie 4 --------------------------------------------------------------------------
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# df = df[df['class'] == 'Iris-setosa']
# colors = np.array([0 for _ in range(0, len(df.index))])
# df['colors'] = colors
# sizes = np.random.randn(len(df.index))
# sizes = np.abs(sizes) * 100
# df['sizes'] = sizes
#
# sb.set()
# plot = sb.relplot(data=df, x='sepal length', y='sepal width', hue='colors', palette=['r'],
#                   sizes='sizes', legend=True)
# plot.fig.set_size_inches(6, 6)
# plt.show()
#
