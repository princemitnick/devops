import datetime
import subprocess
import time

"""
Author : Prince Stanley
Project : Monitoring 
Contributor : Riki
"""

def disk_and_mem_check():

    try:
        res_disk_check = subprocess.run(["df", "-m"], capture_output=True, text=True)
        disk_free = None
        for line in res_disk_check.stdout.splitlines():
            if "/dev/disk3s1s1" in line:
                parts = line.split()
                disk_available = int(parts[3])
                if disk_available < 500:
                    print("⚠️ Avertissement : Espace de disque disponible faible")
                disk_free = disk_available

        res_mem_check = subprocess.run(["free", "-m"], capture_output=True, text=True)
        free_mem = None
        for line in res_mem_check.stdout.splitlines():
            if "Mem:" in line:
                parts = line.split()
                free_mem = int(parts[3])
                if free_mem < 500:
                    print("Avertissement : Memoire disponible faible")

        with open("system.log", "w") as f:
            f.write(f"==========={datetime.date.today()} - {time.strftime('%H:%M:%S')}===============\n")
            f.write(f"Disk Usage (MB): {disk_free}\n")
            f.write(f"Mem Usage (MB): {free_mem} \n")
    except Exception as e:
        print("Exception : ", e)



disk_and_mem_check()
