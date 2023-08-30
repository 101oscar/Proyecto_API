from ui.ui import Interface
from api.api import obtener_datos


class Aplicacion:
	campos = ['departamento', 'municipio', 'cultivo', 'topografia', 
			'ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']

	def filtrar_datos(self):
		departamento = Interface().consultar_departamento()
		municipio = Interface().consultar_municipio()
		cultivo = Interface().consultar_cultivo()
		limite = Interface().consultar_limite()
		datos = obtener_datos(departamento, municipio, cultivo, limite, self.campos)
		return datos

	def menu(self):
		confirmacion_consulta = "S"
		datos = self.filtrar_datos()
		while (confirmacion_consulta == "S"):
			Interface().imprimir_datos(datos)
			confirmacion_consulta = input("Deseas hacer otra consulta (S/Any)?: ").upper()

Aplicacion().menu()


	