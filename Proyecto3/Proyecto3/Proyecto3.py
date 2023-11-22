from MT import TuringMachine

def main():
    mt = TuringMachine()
    mt.load_from_yaml("testMT.yaml")

if __name__ == "__main__":
    main()