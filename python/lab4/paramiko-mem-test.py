from sys import stdout

import paramiko

def nodes_mem_check(host, username, password):

    records = {}
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, username=username, password=password)
        print(f"==========={host}===========")
        stdin, stdout, stderr = client.exec_command("free -m")
        for line in stdout.read().decode().splitlines():
            print(line)
            if "Mem:" in line:
                parts = line.split()
                free_mem = int(parts[3])
                if free_mem < 500:
                    records = {
                        f"{host}": free_mem
                    }
    except Exception as e:
        print(e)

    if len(records) > 0:
        print(records)
        print(f"La memoire disponible du serveur {host} est faible")

if __name__ == "__main__":

    hosts = [
        "192.168.58.100",
        "192.168.58.107",
        "192.168.58.108"
    ]
    for host in hosts:
        nodes_mem_check(
            host=f"{host}",
            username="test",
            password="test"
        )
