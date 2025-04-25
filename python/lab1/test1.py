import datetime
import sys
import os
from pathlib import Path
import shutil

def main():
    print(f"Python version : {sys.version.split()[0]}")
    print(f"Current directory : {os.getcwd()}")

def test():
    files = ["nginx.log","httpd.log","nginx.conf","docker.log","k8s.conf","gmail.txt", "grafana.conf","pipo.log","email.txt"]
    base_dir = Path.cwd() / f"{datetime.date.today()}"
    base_dir.mkdir(exist_ok=True)

    conf_dir = (base_dir / "conf")
    log_dir = base_dir / "log"
    txt_dir = base_dir / "txt"

    conf_dir.mkdir(exist_ok=True)
    log_dir.mkdir(exist_ok=True)
    txt_dir.mkdir(exist_ok=True)

    for filename in files:
        (base_dir / filename).touch()

    for file in base_dir.glob("*.log"):
        try:
            shutil.move(str(file), log_dir)
            print(f"Déplacé {file.name} dans log/")
        except Exception as e:
            print(f"erreur lors du déplacement de {file.name} : {e}")

    for file in base_dir.glob("*.txt"):
        try:
            shutil.move(str(file), txt_dir)
            print(f"Déplacé {file.name} dans txt/")
        except Exception as e:
            print(f"erreur lors du déplacement de {file.name} : {e}")

    for file in base_dir.glob("*.conf"):
        try:
            shutil.move(str(file), conf_dir)
            print(f"Déplacé {file.name} dans conf/")
        except Exception as e:
            print(f"erreur lors du déplacement de {file.name} : {e}")



if __name__ == "__main__":
    main()
    test()