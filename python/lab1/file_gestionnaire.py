import os
import shutil
from pathlib import Path

def main():
    base_dir = Path.cwd() / "sandbox"

    files = ["file1.txt", "file2.log", "file3.conf"]
    base_dir.mkdir(exist_ok=True)

    for filename in files:
        (base_dir / filename).touch()
        print(f"Fichier céé : {filename}")

    print("\nFichiers dans sandbox : ")
    for file in base_dir.iterdir():
        print(file.name)

    target_dir = base_dir / "archived"
    target_dir.mkdir(exist_ok=True)

    for file in base_dir.glob("*.*"):
        shutil.move(str(file), target_dir)
        print(f"Fichier déplacé : {file.name} -> {target_dir}")

    if not any(base_dir.iterdir()):
        base_dir.rmdir()
        print(f"Dossier supprimé : {base_dir}")

if __name__ == "__main__":
    main()