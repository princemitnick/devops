import argparse
import logging
import os.path


def read_last_lines(file_path: str, n: int) -> list[str]:
    """
    Lit les `n` dernieres lignes d'un fichier texte.
    Retourne une liste de lignes (sans les \n)
    :param file_path:
    :param n:
    :return:
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Fichier introuvable : {file_path}")

    with open(file_path, "r") as f:
        lines = f.readlines()
        return [line.rstrip for line in lines[-n:]]

def main():

    parser = argparse.ArgumentParser(description="Visualiser un fichier log")
    parser.add_argument("file", help="Chemin vers le fichier log")
    parser.add_argument("-n", "--lines", type=int, default=10, help="Nombre de lignes a afficher")
    parser.add_argument("--debug", action="store_true", help="Activer le mode debug")
    args = parser.parse_args()

    logging_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=logging_level, format="%(levelname)s: %(message)s")

    try:
        result = read_last_lines(args.file, args.lines)
        logging.info("Derniere lignes du fichier %s : ", args.file)
        for line in result:
            print(line)
    except Exception as e:
        logging.error("Erreur inattendu : %s", str(e))


if __name__ == "__main__":
    main()