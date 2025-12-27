
import time
import random
from datetime import datetime

LOG_FILE = "sample.log"

symbols = ["AAPL", "GOOG", "MSFT", "TSLA", "AMZN"]
levels = ["INFO", "WARNING", "ERROR"]

def random_trade_log():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    symbol = random.choice(symbols)
    price = round(random.uniform(100, 2000), 2)
    latency = random.randint(10, 5000)
    level = random.choices(levels, weights=[85, 10, 5])[0]
    msg = ""
    if level == "INFO":
        msg = f"Trade executed: symbol={symbol} price={price} latency={latency}ms"
    elif level == "WARNING":
        msg = f"High latency detected: symbol={symbol} latency={latency}ms"
    else:  # ERROR
        msg = f"Trade failed: symbol={symbol} price={price} latency={latency}ms reason=Timeout"
    return f"[{now}] {level}: {msg}"

def main():
    with open(LOG_FILE, "a") as f:
        while True:
            log_entry = random_trade_log()
            f.write(log_entry + "\n")
            f.flush()
            print(log_entry)  # Optional: See output in terminal
            time.sleep(random.uniform(0.2, 1.5))  # Simulate real-time logs

if __name__ == "__main__":
    main()
