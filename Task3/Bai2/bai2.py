import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv("C:/Users/gaasu/Desktop/ThucTap-VCCorp/Task3/pokemon.csv")
# df = pd.read_csv("pokemon.csv") //Loi khong mo file

# In ra man hinh cac row data co speed > 80 va attack > 52
print(df.query("Speed > 80 & Attack > 52"))


# In ra man hinh bieu do chi so Attack theo stt, (x, y) = (stt, attack)
plt.plot(df["#"], df["Attack"], 'ro')
plt.show()