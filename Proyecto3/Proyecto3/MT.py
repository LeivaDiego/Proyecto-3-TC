import yaml

class MaquinaTuring:
	# Clase que representa una Maquina de Turing cuya configuracion esta definida por el contenido 
	# de un archivo .yaml


	def __init__(self, states=None, input_alphabet=None, tape_alphabet=None, transitions=None, 
				 initial_state=None, final_state=None, simulation_strings=None):
		"""
        Constructor de la clase MaquinaTuring

        Cada componente representa un aspecto fundamental de la MT

        Args:
            states (list): Lista de estados que la MT puede tener.
            input_alphabet (list): Alfabeto de entrada que define los simbolos aceptados en la entrada
            tape_alphabet (list): Alfabeto de la cinta que incluye los símbolos que se pueden escribir en la cinta
            transitions (dict): Diccionario que define las transiciones entre los estados dados
            initial_state (str): Estado inicial de la MT
            final_state (str): Estado o estados finales que determinan la aceptacion de la cadena
            simulation_strings (list): Lista de cadenas a simular

        Las variables se inicializan con valores por defecto en caso de no proporcionarse
        """
		
		# Inicializacion de los componentes de la MT
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
		"""
		Carga la MT con una configuracion especifica definida en un archivo YAML
		
		La configuracion incluye los estados, el alfabeto de entrada, el alfabeto de la cinta, las transiciones, 
		el estado inicial y final, y las cadenas de simulacion

		Args:
			file_path (str): Ruta del archivo YAML
		"""
		
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
		"""
		Imprime la configuraciOn actual de lamt para propositos de testeo

		Metodo para verificar el estado actual de la MT, incluyendo sus componentes
		como estados, alfabetos, transiciones y la configuracion de la cinta
		"""
		
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
		"""
		Reinicia la MT a su estado inicial

		Metodo para resetear la MT antes de ejecutar una nueva simulacion de cadena,
		asegurando que comienza desde su estado inicial y con la cinta limpia
		"""

		self.current_state = self.initial_state
		self.tape = list(input_string) + [None]  # Agregar blanks al final
		self.head_position = 0



	def format_tape(self):
		"""
		Formatea y devuelve el estado actual de la cinta de la MT

		Metodo que proporciona una cadena legible de la cinta, que puede ser usada para mostrar
		el estado actual de la cinta durante la simulacion

		Returns:
			str: Cadena formateada de la cinta
		"""
		
		start = 0
		end = len(self.tape)
		while start < end and self.tape[start] is None:
			start += 1
		while end > start and self.tape[end - 1] is None:
			end -= 1

		# Formatear la cinta para la visualizacion
		tape_str = ''.join([str(sym) if sym is not None else 'B' for sym in self.tape[start:end]])
		return tape_str[:self.head_position - start] + ' ' + str(self.current_state) + ' ' + \
			   tape_str[self.head_position - start:]



	def step(self):
		"""
		Ejecuta un paso de la simulacion de la MT

		Metodo que avanza la MT un paso dependiendo la config de transiciones y el estado actual
		de la cinta. 
		
		Returns:
			bool: Indica si la MT ha llegado a un estado final o se rechaza
		"""
		
		# Comprobar si la cabeza esta fuera del limite de la cinta
		if self.head_position < 0 or self.head_position >= len(self.tape):
			self.tape.append(None)  # Extender la cinta con blanks si es nececario

		current_symbol = self.tape[self.head_position]
		transition_key = (self.current_state, current_symbol)

		# Verificar si la transicion es valida
		if transition_key not in self.transitions:
			return False  # Transicion no valida, detener maquina

		# Obtencion de detalles de la transicion
		next_state, replace_symbol, move_direction = self.transitions[transition_key]
		
		# Actualizar la cinta y el estado actual
		self.tape[self.head_position] = replace_symbol
		self.current_state = next_state
		
		# Imprimir la descripcion instantanea
		print(f"⊢ {self.format_tape()}")

		# Mover la cabeza a la izquierda o derecha
		if move_direction == 'L':
			self.head_position -= 1
		elif move_direction == 'R':
			self.head_position += 1

		return True  # Transicion valida, continuar maquina


	
	def run(self, input_string):
		"""
		Ejecuta la simulacion completa de la MT para una cadena de entrada

		Metodo que procesa una cadena mediante la MT y devuelve el resultado final
		y si la cadena es aceptada o no
		
		Args:
			input_string (str): Cadena de entrada para simular en la MT

		Returns:
			tuple: Resultado final en la cinta y un booleano indicando si la cadena es aceptada
		"""
		
		self.reset(input_string)
		while self.step():
			pass
		return self.tape, self.current_state == self.final_state