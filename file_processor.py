import pandas as pd
import json
from datetime import datetime
from normalizador import *


# leer archivo 
df = pd.read_excel('infome_2023.xlsx', parse_dates=['Fecha'])

#Cambiar formato de fecha
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d-%m-%Y')

df['Fecha'] = df['Fecha'].dt.strftime('%Y-%m-%d')


#Normalizar comerciales

df['Empleado_Vendedor'] = df['Empleado_Vendedor'].apply(estandarVendedor) 

def custom_encoder(obj):
    if isinstance(obj, str):
        return obj.encode('utf-8').decode('unicode-escape')
    return obj
# Aplicar la función de codificación al DataFrame
df_encoded = df.applymap(custom_encoder)

#acá hacemos la suma 
df['Cant'] = -df['Cant']
df['Valor_Unitario'] = -df['Valor_Unitario']
df['Subtotal'] = -df['Subtotal']


# ''records' orientation se utiliza comúnmente para una lista de diccionariosords' orientation is often used for a list of dictionaries
json_data = df.to_json(orient='records', force_ascii=False,  indent=4,  date_format='iso')

# Save JSON to a file
with open('informe_2023.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)


 