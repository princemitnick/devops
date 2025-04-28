import paramiko

def ssh_command(host, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        client.connect(hostname=host, username=username, password=password)
        print(f"Connecté à {host}")

        stdin, stdout, stderr = client.exec_command(command)

        print("Resultat de la commande : ")
        for line in stdout.read().decode().splitlines():
            print(line)
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        client.close()

if __name__ == "__main__":
    hosts = ["192.168.58.108", "192.168.58.100", "192.168.58.107"]

    for host in hosts:
        ssh_command(
            host=f"{host}",
            username="test",
            password="test",
            command="uptime"
        )