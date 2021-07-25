import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# call file function


def call_file(path):
    data = pd.read_csv(path, index_col='year')
    return pd.DataFrame(data)


# call file
path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/01_Coal_Prices_Electricity_Sector.csv'
df = call_file(path)

print(df.columns)


lw = 3
source = 'Source: EIA'
# * purchase price is assumed to be delivered coal cost minus transportation cost

m_size = 15
l_size = 12

colors = ['#e15759', '#f28e2b', '#edc948',
          '#59a14f', '#76b7b2', '#4e79a7', '#b07aa1']

# plot figure
fig, ax = plt.subplots(sharex=True, figsize=(12, 6))

ax.plot(df.loc[:, 'delivered'], color='black', linewidth=lw)
ax.plot(df.loc[:, 'transportation'], color=colors[0], linewidth=lw)
ax.plot(df.loc[:, 'delivered'] - df.loc[:, 'transportation'],
        color=colors[1], linewidth=lw)

ax.set_title('US Coal Prices Delivered to Power Sector\n', fontsize=20)
ax.set_ylabel('USD per Short Ton\n', fontsize=m_size)
ax.set_xlim([2008, 2019])
ax.set_ylim([0, 60])
ax.set_facecolor('#ECECEC')

plt.xticks(fontsize=l_size)
plt.yticks(fontsize=l_size)

plt.text(0.1045, 0.01, source, fontsize=l_size,
         transform=plt.gcf().transFigure)
plt.text(0.44, 0.78, 'Delivered Coal Price', fontsize=m_size,
         transform=plt.gcf().transFigure)
plt.text(0.465, 0.53, 'Purchase Price',
         fontsize=m_size, color=colors[1], transform=plt.gcf().transFigure)
# plt.text(0.59, 0.54, '*',
#          fontsize=m_size, color=colors[1], transform=plt.gcf().transFigure)
plt.text(0.442, 0.38, 'Transportation Cost',
         fontsize=m_size, color=colors[0], transform=plt.gcf().transFigure)

plt.show()
