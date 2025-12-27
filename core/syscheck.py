import subprocess
import psutil

class SystemCheck:
    @staticmethod
    def cpu_usage():
        return psutil.cpu_percent(interval=1)

    @staticmethod
    def memory_usage():
        mem = psutil.virtual_memory()
        return f"{mem.percent}% used of {mem.total/1e9:.2f} GB"

    @staticmethod
    def disk_usage():
        return subprocess.getoutput("df -h / | tail -1")
