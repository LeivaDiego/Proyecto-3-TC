from MT import TuringMachine

def main():
    mt = TuringMachine()
    mt.load_from_yaml("testMT.yaml")
    mt.debug_print()

if __name__ == "__main__":
    main()