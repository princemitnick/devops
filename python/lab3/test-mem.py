import subprocess

def mem_check():
    res = subprocess.run(["free", "-m"], capture_output=True, text=True)
    print(res.stdout)


mem_check()