from tabulate import tabulate

class Interface:
    
	def consultar_departamento(self):
		departamento = input("Seleccione un departamento: ")
		return departamento.upper()
	
	def consultar_municipio(self):
		municipio = input("Seleccione un municipio: ")
		return municipio.upper()
	
	def consultar_cultivo(self):
		cultivo = input("Seleccione un cultivo (Primera letra en mayúscula): ")
		return cultivo
	
	def consultar_limite(self):
		limite_registros = int(input("Inserte un Número de Registros: "))
		return limite_registros

	def imprimir_datos(self, datos):
		titulos = ['Departamento', 'Municipio', 'Cultivo', 'Topografia', 'Nivel de pH', 'Fósforo', 'Potasio']
		tabla = tabulate(datos, titulos, tablefmt = 'psq1')
		print(tabla)

	def imprimir_mediana(self, medianas):
		titulos = ['Mediana de Nivel pH', 'Mediana de Nivel de Fósforo', 'Mediana de Nivel de Potasio']
		tabla = tabulate(medianas, titulos, tablefmt = 'psq1')
		print("\n", tabla)

		