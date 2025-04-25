def write_file():
    with open('file.txt', 'w') as f:
        f.write("Serveur : nginx\n")
        f.write("Status : ok\n")
        f.write("IP : 10.0.0.4")

def read_file():
    with open("file.txt", 'r') as f:
        content = f.read()
    print(content)

def parsing_file():
    with open("file.txt", 'r') as f:
        for line in f:
            if "IP" in line:
                print("Addresse IP trouvée : ", line.strip())

if __name__ == "__main__":
    write_file()
    read_file()
    parsing_file()