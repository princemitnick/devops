import paramiko

def nodes_mem_check(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    record = {}
    try:
        client.connect(hostname=host, username=username, password=password)
        print(f"================ {host} ============")

        stdin, stdout, stderr = client.exec_command("free -m")
        for line in stdout.read().decode().splitlines():
            if "Mem:" in line:
                parts = line.split()
                free_mem = int(parts[3])
                print(f"Memoire libre sur {host} : {free_mem} MB")

                if free_mem < 500:
                    record[host] = free_mem
    except Exception as e:
        print(f"Erreur sur {host} : {e}")
    finally:
        client.close()
    return record

if __name__ == "__main__":
    hosts = [
        "192.168.58.100",
        "192.168.58.107",
        "192.168.58.108"
    ]
    alert_records = {}

    for host in hosts:
        records = nodes_mem_check(
            host=host,
            username="test",
            password="test"
        )
        alert_records.update(records)

        if alert_records:
            print("\n🛑 Alerte memoire faible detectee sur les serveurs suivants : ")
            for host, mem in alert_records.items():
                print(f" - {host} : {mem} MB de memoire libre")
        else:
            print("\n✅ Tous les serveurs ont assez de mémoire disponible.")