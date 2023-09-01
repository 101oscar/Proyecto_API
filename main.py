from ui.ui import Interface
import api.api as api

class Aplicacion:
	campos = ['departamento', 'municipio', 'cultivo', 'topografia', 
				'ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']

	def _init_(self):
		self.datos = []
		
	def borrar_datos(self):
		self.datos = []

	def filtrar_datos(self):
		departamento = Interface().consultar_departamento()
		municipio = Interface().consultar_municipio()
		cultivo = Interface().consultar_cultivo()
		limite = Interface().consultar_limite()
		self.datos = api.obtener_datos(departamento, municipio, cultivo, limite, self.campos)

	def calcular_mediana(self):
		medianas = {self.campos[4]: [], self.campos[5]: [], self.campos[6]: []}
		for campo in medianas:
			mediana = api.calcular_mediana(self.datos, campo)
			medianas[campo].append(mediana)
		return medianas

	def menu(self):	
		confirmacion_consulta = "S"
		while confirmacion_consulta == "S":
			self.filtrar_datos()
			Interface().imprimir_datos(self.datos)
			Interface().imprimir_mediana(self.calcular_mediana())
			confirmacion_consulta = input("Desea hacer otra consulta (S/Any)?: ").upper()
			if confirmacion_consulta != "S":
				self.borrar_datos()

Aplicacion().menu()

	