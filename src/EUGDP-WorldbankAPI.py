import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import world_bank_data as wb
from datetime import datetime
# https://pypi.org/project/world-bank-data/

startYear = '1998'
currentYear = str(datetime.now().year - 1)

GDP_EU = pd.DataFrame(
    wb.get_series('NY.GDP.MKTP.KD.ZG',
                  id_or_value='id',
                  country='EUU',
                  simplify_index=1))

recentGDP_EU = GDP_EU.loc[startYear:currentYear]

sampleAverage = recentGDP_EU.mean()[0]
tcks = np.arange(-5, 5, 0.5)

plt.style.use('seaborn')
fig = plt.figure(figsize=(12, 8), dpi=120)
plt.plot(recentGDP_EU, lw=3)

plt.title('European Union - % Annual GDP growth', weight='bold')
plt.hlines(y=0,
           xmin=startYear,
           xmax=currentYear,
           color='grey')
plt.hlines(y=sampleAverage,
           xmin=startYear,
           xmax=currentYear,
           color='red')
plt.xlim(startYear, currentYear)
plt.yticks(tcks)
plt.figtext(0.88, 0.91, "Red line is the sample average",
            ha="center", weight='bold')
# 0.5, 0.001
plt.tight_layout()
plt.show()
fig.savefig('output/EU_GDP')
