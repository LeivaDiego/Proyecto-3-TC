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
