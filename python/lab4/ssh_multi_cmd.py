import paramiko

def execute_multiple_commands(host, username, private_key_path, commands):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        key = paramiko.RSAKey.from_private_key_file(private_key_path)
        client.connect(hostname=host, username=username, pkey=key)
        result = {}
        for cmd in commands:
            print(f"Execution de {cmd}")
            stdin, stdout, stderr = client.exec_command(cmd)
            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()

            if error:
                print(f"Erreur pour la commande '{cmd} : {error}")
            else:
                print(output)
    except Exception as e:
        print(f"Erreur de connexion à {host} : {e}")
    finally:
        client.close()

if __name__ == "__main__":

    hosts = ["192.168.58.100",
             "192.168.58.108",
             "192.168.58.107"]

    commands = [
        "hostname",
        "uptime",
        "df -h",
        "free -mh"
    ]

    for host in hosts:
        execute_multiple_commands(
            host=host,
            username="test",
            private_key_path="/Users/prstanley/.ssh/id_rsa",
            commands=commands
        )