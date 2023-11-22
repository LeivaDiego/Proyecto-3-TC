from MT import MaquinaTuring

def main():
	mt = MaquinaTuring()
	mt.load_from_yaml("testMT.yaml")
	mt.debug_print()
	for input_string in mt.simulation_strings:
		tape_result, is_accepted = mt.run(input_string)
		print(f"Input: {input_string}, Result: {tape_result}, Accepted: {is_accepted}")

if __name__ == "__main__":
	main()