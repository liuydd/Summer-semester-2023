import io
import pandas as pd
import math

data = []
i=0
while i<=3:
    try:
        input_ = input()
        data.append(input_)
        i+=1
    except EOFError:
        break
data = '\n'.join(data)
df = pd.read_csv(io.StringIO(data))

#apply, 
#for i in df.columns:
    #df['inv_'+i] = math.floor(100/df[i])

print(df.to_string(index=False))