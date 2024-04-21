import subprocess

def is_xvfb_installed() -> bool:
    try:
        # Try to run `Xvfb -help` and capture its output
        subprocess.run(["Xvfb", "-help"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        # If a FileNotFoundError is raised, Xvfb is not installed
        return False
    except subprocess.CalledProcessError:
        # If Xvfb exists but the command failed for other reasons, it's still installed
        return True
