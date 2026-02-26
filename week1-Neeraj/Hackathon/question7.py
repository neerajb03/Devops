import subprocess

def pip_freeze():
    try:
        result = subprocess.run(
            ["pip", "freeze"],
            capture_output=True,
            text=True,
            check=True
        )
        packs = result.stdout.strip().split("\n")
        return packs
    except Exception as e:
        print("An error occurred:",e)
        return []

if __name__ == "__main__":
    for x in pip_freeze():
        print(x)