import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, municipio, cultivo, limite, campos):
	client = Socrata ("www.datos.gov.co", None )
	results = client.get("ch4u-f3i5",departamento = departamento, municipio = municipio, cultivo = cultivo, limit = limite)
	results_df = pd.DataFrame.from_records( results )
	return results_df[campos]


