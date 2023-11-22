import yaml

class MaquinaTuring:
	def __init__(self, states=None, input_alphabet=None, tape_alphabet=None, transitions=None, 
				 initial_state=None, final_state=None, simulation_strings=None):
		self.states = states if states is not None else []
		self.input_alphabet = input_alphabet if input_alphabet is not None else []
		self.tape_alphabet = tape_alphabet if tape_alphabet is not None else []
		self.transitions = transitions if transitions is not None else {}
		self.initial_state = initial_state
		self.final_state = final_state
		self.current_state = initial_state
		self.simulation_strings = simulation_strings if simulation_strings is not None else []
		self.tape = []
		self.head_position = 0

	def load_from_yaml(self, yaml_file):
		with open(yaml_file, 'r') as file:
			data = yaml.safe_load(file)
		
		# Asignar los valores a las propiedades de la clase
		self.states = data.get('q_states', {}).get('q_list', [])
		self.initial_state = data.get('q_states', {}).get('initial')
		self.final_state = data.get('q_states', {}).get('final')
		self.input_alphabet = data.get('alphabet', [])
		self.tape_alphabet = data.get('tape_alphabet', [])
		
		# Procesar las transiciones
		self.transitions = {}
		for transition in data.get('delta', []):
			key = (transition['params']['initial_state'], transition['params'].get('tape_input'))
			value = (transition['output']['final_state'],
					 transition['output'].get('tape_output'),
					 transition['output']['tape_displacement'])
			self.transitions[key] = value

		self.simulation_strings = data.get('simulation_strings', [])

	def debug_print(self):
		print("Turing Machine Configuration:")
		print("States:", self.states)
		print("Input Alphabet:", self.input_alphabet)
		print("Tape Alphabet:", self.tape_alphabet)
		print("Initial State:", self.initial_state)
		print("Final State:", self.final_state)
		print("Transitions:")
		for key, value in self.transitions.items():
			print(f"  {key} -> {value}")
		print("Simulation Strings:", self.simulation_strings)

	def reset(self, input_string):
		self.current_state = self.initial_state
		self.tape = list(input_string) + [None]  # Agregar blanks al final
		self.head_position = 0

	def step(self):
		if self.head_position < 0 or self.head_position >= len(self.tape):
			self.tape.append(None)  # Extender la cinta con blanks si es nececario

		current_symbol = self.tape[self.head_position]
		transition_key = (self.current_state, current_symbol)

		if transition_key not in self.transitions:
			return False  # Transicion no valida, detener maquina

		next_state, replace_symbol, move_direction = self.transitions[transition_key]
		self.tape[self.head_position] = replace_symbol
		self.current_state = next_state

		if move_direction == 'L':
			self.head_position -= 1
		elif move_direction == 'R':
			self.head_position += 1

		return True  # Transicion valida, continuar maquina


	def run(self, input_string):
		self.reset(input_string)
		while self.step():
			pass
		return self.tape, self.current_state == self.final_state