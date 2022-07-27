import pandas as pd
 
df = pd.read_excel(io = "correo.xlsx", sheet_name="Hoja1",usecols=["correo"])
 
print(df)
