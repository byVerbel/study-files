import pandas as pd

def caso_who(ruta_archivo_csv: str)-> dict:
    archivo = ruta_archivo_csv
    try:
        if archivo.endswith('csv'):
            pass
        else:
            salida = 'Extensión inválida.'
            return salida
            exit()
        df = pd.read_csv(ruta_archivo_csv)
    except:
        salida = 'Error al leer el archivo de datos.'
        return salida
        exit()

    df['total_cases'] = (df['total_cases_per_million']*df['population'])/1000000
    df['total_beds'] = (df['hospital_beds_per_thousand']*df['population'])/1000
    df['razon'] = df['total_cases']/df['total_beds']
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
    df_respuesta = df.groupby(['date','continent'])['razon'].mean().unstack()
    df_respuesta.plot()
    df_respuesta.plot().get_figure().savefig('output.png')
    return df_respuesta.to_dict()

print(caso_who('owid-covid-data.csv'))