import paramiko

def ssh_with_key(host, username, private_key_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        key = paramiko.RSAKey.from_private_key_file(private_key_path)

        client.connect(hostname=host, username=username, pkey=key)
        print(f"Connecté à {host} avec la clé privée")

        stdin, stdout, stderr = client.exec_command("uptime")
        print(stdout.read().decode())
    except Exception as e:
        print(f"Erreur de connexion à {host} : {e}")
    finally:
        client.close()

if __name__ == "__main__":
    ssh_with_key(
        host="192.168.58.107",
        username="test",
        private_key_path="/Users/prstanley/.ssh/id_rsa"
    )