import numpy as np
import random
import math
import statistics
import pandas as pd
import matplotlib as plt
from io import StringIO
import math
a = np.array([4.98 , 5.09 , 4.87 , 5.2 , 4.86, 4.94 , 4.95 , 5.08 , 5.06 , 5.18 , 4.75 , 5.08 , 4.91 , 4.8 , 5.03 , 4.95 , 4.8 , 5.08 , 5.04 , 4.9 , 5.03 , 5.33 , 4.88 , 4.89 , 4.85 , 5.16 , 4.94 , 4.99 , 5.16 , 4.93])
n = len(a)
b = np.copy(a)

k = int(random.randint(1, int(n * 0.5))) # 0 отсутствует фактически, чтобы было всё плохо всегда
for i in range(0, k):
    r = random.randint(0, int(n * 0.5))
    b[r] = math.nan
c = pd.DataFrame(data={'exp': b})
print(c)
mn = statistics.mean(a)
mm = statistics.mean(b) #просто демонстрация того, что так не работает
mm1 = np.nanmean(b) #игнорирование nan. Т.к. там убираются некоторые данные, то это значение должно отличаться
print('Without nan: ', mn)
print(mm, '  It does not work this way!')
print('Instead this: ', mm1)
rude = c.mean() #это уже . Здесь по умолчанию, как видно, игнорируются nan
print('Using pandas: ', rude)
harm = statistics.harmonic_mean(a)
print('Harmonic mean (without nan): ', harm)
c.isnull().sum()
print(c.isnull().sum())
c = c.fillna(rude)
c.plot()
c.plot.kde()
ar = pd.DataFrame(a)
ar.plot.kde()