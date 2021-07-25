import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# call file function
def call_file(path):
  data = pd.read_csv(path, index_col=0)
  return pd.DataFrame(data)

# call file
path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/04_EIA_Henry_Hub_Natural_Gas_Price_Projections.csv'
df = call_file(path)


print(df.columns)


# plot figure
fig, ax = plt.subplots(sharex=True, figsize=(12, 6))

lw = 2

m_size = 15
l_size = 12

source = 'Source: EIA'

ax.plot(df.loc[2010:2020, 'historical'], linewidth=lw, color='#0a8d8f')

ax.plot(df.loc[2019:2040, 'high_oil_and_gas_supply'],
        linewidth=lw, color='black', linestyle='--')

ax.plot(df.loc[2019:2040, 'low_oil_and_gas_supply'],
        linewidth=lw, color='black', linestyle='--')

ax.plot(df.loc[2019:2040, 'reference'], linewidth=lw,
        color='#0a8d8f', linestyle='--')

ax.set_xticks(np.arange(2010, 2045, 5))

ax.set_facecolor('#ECECEC')

plt.xticks(fontsize=l_size)
plt.yticks(fontsize=l_size)
ax.set_ylabel('USD per Million Btu', fontsize=m_size)



ax.set_xlim([2010, 2040])

title = 'EIA Annual Energy Outlook 2020\nProjected Annual Henry Hub Natural Gas Price'
ax.set_title(title, fontsize=20)


ax.fill_between(np.arange(2019, 2041, 1), df.loc[2019:2040, 'high_oil_and_gas_supply'],
                df.loc[2019:2040, 'low_oil_and_gas_supply'], alpha=0.2)


x2 = 0.53
plt.text(0.1045, 0.01, source, fontsize=l_size,
         transform=plt.gcf().transFigure)
plt.text(x2, 0.79, 'Low Oil and Gas Supply',
         fontsize=m_size, transform=plt.gcf().transFigure)
plt.text(x2, 0.425, 'Reference Case',
         fontsize=m_size, color='#0a8d8f', transform=plt.gcf().transFigure)
plt.text(0.16, 0.64, 'Historical Price',
         fontsize=m_size, color='#0a8d8f', transform=plt.gcf().transFigure)
plt.text(x2, 0.29, 'High Oil and Gas Supply',
         fontsize=m_size, transform=plt.gcf().transFigure)

plt.show()
