import pandas as pd
import numpy as np
from core.parser import LogParser

class Metrics:
    def __init__(self, logfile):
        self.logfile = logfile
        self.df = pd.DataFrame(list(LogParser(logfile)))

    def latency_stats(self):
        self.df["latency"] = self.df["msg"].str.extract(r"latency=(\d+)").astype(float)
        latencies = self.df["latency"].dropna()
        if latencies.empty:
            return {}
        return {
            "mean": np.mean(latencies),
            "max": np.max(latencies),
            "min": np.min(latencies),
            "std": np.std(latencies)
        }

    def error_summary(self):
        return self.df[self.df["level"] == "ERROR"]["msg"].tolist()
