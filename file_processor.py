import pandas as pd


# leer archivo 
df = pd.read_excel('informe2023.xlsx', parse_dates=['Fecha'])

df['Fecha'] = df['Fecha'].dt.strftime('%d-%m-%Y')


def custom_encoder(obj):
    if isinstance(obj, str):
        return obj.encode('utf-8').decode('unicode-escape')
    return obj

df_encoded = df.applymap(custom_encoder)

# 'records' orientation is often used for a list of dictionaries
json_data = df.to_json(orient='records', force_ascii=False,  indent=4,  date_format='iso')

# Save JSON to a file
with open('anual2023.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

# Print JSON to the console
print(len(json_data))
