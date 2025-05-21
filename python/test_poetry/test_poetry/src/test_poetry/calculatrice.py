import argparse
import logging

logging.basicConfig(level=logging.INFO)

def add(a, b):
    return a + b

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Additionne deux nombres.")
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)

    args = parser.parse_args()

    result = add(args.a, args.b)

    logging.info(f"Resultat : {result}")