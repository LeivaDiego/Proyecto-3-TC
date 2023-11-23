from MT import MaquinaTuring

def main():
	mt = MaquinaTuring()
	mt.load_from_yaml("testMT.yaml")
	#mt.debug_print()
	for input_string in mt.simulation_strings:
		print("---------------------------------")
		print(f"Input: {input_string}")
		print("---------------------------------")
		print("Descripciones Instantaneas: ")
		tape_result, is_accepted = mt.run(input_string)
		print("---------------------------------")
		print("Resultado:")
		if is_accepted:
			print("La cadena es aceptada por la MT")
		else:
			print("La cadena es rechazada por la MT")
		print("---------------------------------\n\n")

if __name__ == "__main__":
	main()