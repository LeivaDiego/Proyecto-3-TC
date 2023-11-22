import yaml

class TuringMachine:
    def __init__(self, states=None, input_alphabet=None, tape_alphabet=None, transitions=None, 
                 initial_state=None, final_state=None, simulation_strings=None):
        self.states = states if states is not None else []
        self.input_alphabet = input_alphabet if input_alphabet is not None else []
        self.tape_alphabet = tape_alphabet if tape_alphabet is not None else []
        self.transitions = transitions if transitions is not None else {}
        self.initial_state = initial_state
        self.final_state = final_state
        self.simulation_strings = simulation_strings if simulation_strings is not None else []

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
