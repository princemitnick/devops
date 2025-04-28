import paramiko
import csv
import datetime

def execute_commands_and_log(hosts, username, private_key_path, commands, csv_file_path):

    with open(csv_file_path, mode='w', newline='') as csvfile:
        fieldnames = ["Date", "Host", "Commande", "Resultat"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for host in hosts:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                key = paramiko.RSAKey.from_private_key_file(private_key_path)
                client.connect(hostname=host, username=username, pkey=key)

                for cmd in commands:
                    print(f"Execution de : {cmd}")
                    stdin, stdout, stderr = client.exec_command(cmd)
                    output = stdout.read().decode().strip()
                    error = stderr.read().decode().strip()

                    result = output if output else error

                    writer.writerow(
                        {
                            "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "Host": host,
                            "Commande": cmd,
                            "Resultat": result
                        }
                    )

            except Exception as e:
                print(f"Erreur de connexion a {host} : {e}")
            finally:
                client.close()


if __name__ == "__main__":
    hosts = [
        "192.168.58.100",
        "192.168.58.107",
        "192.168.58.108"
    ]

    commands = [
        "hostname",
        "uptime",
        "df -h",
        "free -m"
    ]

    private_key_path = "/Users/prstanley/.ssh/id_rsa"
    csv_file_path = "monitoring_report.csv"

    execute_commands_and_log(hosts, "test", private_key_path, commands, csv_file_path)