from concurrent.futures import ThreadPoolExecutor
from core.metrics import Metrics

def analyze_multiple_logs(logfiles):
    results = {}
    with ThreadPoolExecutor(max_workers=len(logfiles)) as ex:
        futures = {ex.submit(Metrics(f).latency_stats): f for f in logfiles}
        for fut in futures:
            results[futures[fut]] = fut.result()
    return results
