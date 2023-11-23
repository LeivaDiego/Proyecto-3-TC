from MT import MaquinaTuring

def main():
	mt = MaquinaTuring()
	mt.load_from_yaml("testMT.yaml")
	#mt.debug_print()
	for input_string in mt.simulation_strings:
		tape_result, is_accepted = mt.run(input_string)
		result_str = ''.join([str(sym) if sym is not None else '' for sym in tape_result])  # Formatear la cinta
		print(f"Input: {input_string}, Result: {result_str}, Accepted: {is_accepted}\n")

if __name__ == "__main__":
	main()