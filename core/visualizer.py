import matplotlib.pyplot as plt

def plot_latency(latencies):
    plt.figure(figsize=(6,4))
    plt.title("Latency Distribution")
    plt.hist(latencies, bins=10, color="skyblue", edgecolor="black")
    plt.xlabel("Latency (ms)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("reports/latency_hist.png")
    plt.close()
