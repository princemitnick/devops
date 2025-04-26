import subprocess

def mem_check():
    res = subprocess.run(["free", "-m"], capture_output=True, text=True)
    print(res.stdout)
    for line in res.stdout:
        if "free" in line:
            print("yes")


mem_check()