import subprocess

def mem_check():
    res = subprocess.run(["free", "-m"], capture_output=True, text=True)
    for line in res.stdout.splitlines():
        print(line)


mem_check()