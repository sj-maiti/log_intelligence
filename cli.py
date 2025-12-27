#!/usr/bin/env python3
import argparse
from core.decorators import timed
from core.metrics import Metrics
from core.visualizer import plot_latency
from core.syscheck import SystemCheck

# test change

@timed
def analyze(logfile):
    m = Metrics(logfile)
    stats = m.latency_stats()
    print(f"\nLatency stats for {logfile}: {stats}")
    if stats:
        plot_latency(m.df["latency"].dropna())
        print("Histogram saved to reports/latency_hist.png")
    print("\nErrors found:")
    for err in m.error_summary():
        print(" -", err)

@timed
def sys_health():
    print("\nSystem Health:")
    print("CPU Usage:", SystemCheck.cpu_usage(), "%")
    print("Memory Usage:", SystemCheck.memory_usage())
    print("Disk Usage:", SystemCheck.disk_usage())

def main():
    parser = argparse.ArgumentParser(description="Production Log Intelligence System")
    parser.add_argument("--log", help="Path to log file")
    parser.add_argument("--syscheck", action="store_true", help="Run system health checks")
    args = parser.parse_args()

    if args.log:
        analyze(args.log)
    if args.syscheck:
        sys_health()

if __name__ == "__main__":
    main()
