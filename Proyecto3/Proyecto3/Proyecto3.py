from MT import MaquinaTuring

def main():
	print("Maquina de Turing Reconocedora")
	mtr = MaquinaTuring()
	mtr.load_from_yaml("Reconocedora.yaml")
	#mt.debug_print()
	for input_string in mtr.simulation_strings:
		print("---------------------------------")
		print(f"Input: {input_string}")
		print("---------------------------------")
		print("Descripciones Instantaneas: ")
		tape_result, is_accepted = mtr.run(input_string)
		print("---------------------------------")
		print("Resultado:")
		if is_accepted:
			print("La cadena es aceptada por la MT")
		else:
			print("La cadena es rechazada por la MT")
		print("---------------------------------\n\n")
	
	print("Maquina de Turing Alteradora")
	mta = MaquinaTuring()
	mta.load_from_yaml("Alteradora.yaml")
	#mt.debug_print()
	for input_string in mta.simulation_strings:
		print("---------------------------------")
		print(f"Input: {input_string}")
		print("---------------------------------")
		print("Descripciones Instantaneas: ")
		tape_result, is_accepted = mta.run(input_string)
		print("---------------------------------")
		print("Resultado:")
		if is_accepted:
			print("La cadena es aceptada por la MT")
		else:
			print("La cadena es rechazada por la MT")
		print("---------------------------------\n\n")

if __name__ == "__main__":
	main()