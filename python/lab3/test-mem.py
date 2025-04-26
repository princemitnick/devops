import datetime
import subprocess
import time


def disk_and_mem_check():
    disk_free = None
    free_mem = None
    res_disk_check = subprocess.run(["df", "-m"], capture_output=True, text=True)
    for line in res_disk_check.stdout.splitlines():
        if "/dev/disk3s1s1" in line:
            disk_free = line.split()[4]
            if int(disk_free.lstrip()[0]) < 20:
                print("⚠️ Avertissement : Espace de disque presqu'insuffisant")

    res_mem_check = subprocess.run(["free", "-m"], capture_output=True, text=True)
    for line in res_mem_check.stdout.splitlines():
        if "Mem:" in line:
            free_mem = int(line.split()[3])
            if free_mem < 500:
                print("Avertissement : Memoire disponible faible")

    with open("system.log", "w") as f:
        f.write(f"==========={datetime.date} - {datetime.time}===============\n")
        f.write(f"Disk Usage : {disk_free}\n")
        f.write(f"Mem Usage : \n")



disk_and_mem_check()