"""
Author : Prince Stanley 
Project : lab3
"""

import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print(f"Code retour : {result.returncode}")
print(f"Sortie standard: {result.stdout}")
print(f"Erreur standard : {result.stderr}")

def check_disk_usage():
    res = subprocess.run(["df", "-mh"], capture_output=True, text=True)
    #print(res.stdout.strip())

    for line in res.stdout.strip():
        if "Used" in line:
            print("line")



check_disk_usage()
