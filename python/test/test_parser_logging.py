import argparse
import  logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def add(a, b):
    logging.info(f"Résultat: {a} + {b} = {a + b}")

def subs(a, b):
    logging.info(f"Résultat: {a} - {b} = {a - b}")

def div(a, b):
    try:
        logging.info(f"Résultat: {a} / {b} = {a / b}")
    except:
        logging.error("Division par zero interdite")

def mul(a, b):
    print( a * b)

parser = argparse.ArgumentParser("Addition, soustraction, Division, Multiplication")

parser.add_argument("param1", type=int, help="Premier entier")
parser.add_argument("param2", type=int, help="Deuxieme entier")
parser.add_argument("param3", type=str, help="Operateur +, -, /, x")

args = parser.parse_args()

operator = args.param3

if operator == "+":
    add(args.param1, args.param2)
elif operator == "-":
    subs(args.param1, args.param2)
elif operator == "/":
    div(args.param1, args.param2)
elif operator == "x":
    mul(args.param1, args.param2)
else:
    logging.error("Operateur non reconnu. Utilisez +, - / ou x")