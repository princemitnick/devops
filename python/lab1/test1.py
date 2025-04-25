import sys
import os

def main():
    print(f"Python version : {sys.version.split()[0]}")
    print(f"Current directory : {os.getcwd()}")

if __name__ == "__main__":
    main()