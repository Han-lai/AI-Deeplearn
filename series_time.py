import pandas as pd
import numpy as np
ts = pd.Series(np.random.randn(5),
               index= pd.date_range('20200301',periods=5)) # 預設 頻率 為日
print(ts)
print('')