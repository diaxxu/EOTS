import subprocess
import sys

def start_core_stream(target_ip="192.168.1.100", port=5000):
    cmd = [
        "libcamera-vid",
        "-t", "0",
        "--width", "1280",
        "--height", "720",
        "--framerate", "60",
        "--inline",
        "--profile", "baseline",
        "-o", f"udp://{target_ip}:{port}"
    ]
    
    try:
        process = subprocess.Popen(cmd)
        process.wait()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    start_core_stream(target_ip="192.168.1.100", port=5000)