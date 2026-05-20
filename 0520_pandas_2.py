import pandas as pd

import pandas as pd


data = {
    "Product": ["Apple", " Banana", " Orange", "Mango", "Grape"],
    "Price": [30, 20, 25, 60, 45],
    "Sales": [100, 150, 80, 60, 90],
}


df = pd.DataFrame(data)
print(df)


data = [
    ["Apple",30,100],
    [" Banana",20,150],
    [" Orange",25,80],
    ["Mango",60,60],
    [ "Grape", 45, 90]

]
df = pd.DataFrame(data, columns=["Product", "Price", "Sales"])
print(df)

