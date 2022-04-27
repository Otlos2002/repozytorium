import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
ts = pd.Series(np.random.randn(1000))

ts = ts.cumsum()
print(ts)
ts.plot()
plt.savefig('wykres.png')
# # plt.show()
#
# data = {'Kraj':['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         "Stolica" :['Bruksela', 'New Delhi', 'Brasilia','Warszawa'],
#         'Populacja': [111965343, 133233442, 12888223, 38600991],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa']}
#
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby('Kontynent').agg({'Populacja':['sum']})
# print(grupa)
#
# grupa.plot(kind='bar', xlabel = "Kontynent", ylabel ='Populacja w mld', rot = 0,
#            title = 'Populacja dla kontynentow')
# plt.show()
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynenty')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis ='x', labelrotation = 0 )
# wykres.legend()
#
# plt.show()
#
# df = pd.read_csv('dane.csv', header = 0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
# grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20,figsize =(6,6), legend=(0,0))
# plt.show()

df = pd.DataFrame(ts)

df['Średnia krocząca'] = df.rolling(window=50).mean()
df.plot()
plt.legend(['Wartości', 'Średnia krocząca'])
plt.show()
