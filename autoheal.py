import time
import requests
import subprocess
from datetime import datetime

ENDPOINT = "http://localhost:8000/"
LOG_FILE = "./autoheal.log"
CHECK_INTERVAL = 30


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def check_service():
    try:
        response = requests.get(ENDPOINT, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def restart_service():
    subprocess.run(["docker", "compose", "restart"], check=True)


if __name__ == "__main__":
    log("Autoheal script started")

    while True:
        if not check_service():
            log("Service is DOWN. Restarting...")
            restart_service()
            log("Service restarted")

        time.sleep(CHECK_INTERVAL)