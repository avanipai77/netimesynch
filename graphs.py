import pandas as pd
import matplotlib.pyplot as plt

# Read all experimental data
data = pd.read_csv("results.csv")

# Separate normal and delayed measurements
normal = data[data["Network Delay (ms)"] <= 50]
delayed = data[data["Network Delay (ms)"] > 50]

# Graph 1: Network delay comparison
plt.figure()
plt.bar(
    ["Normal Network", "Delayed Network"],
    [
        normal["Network Delay (ms)"].mean(),
        delayed["Network Delay (ms)"].mean()
    ]
)
plt.ylabel("Average Network Delay (ms)")
plt.title("Network Delay Comparison")
plt.tight_layout()
plt.savefig("network_delay.png")
plt.close()

# Graph 2: Clock offset comparison
plt.figure()
plt.bar(
    ["Normal Network", "Delayed Network"],
    [
        normal["Clock Offset (ms)"].abs().mean(),
        delayed["Clock Offset (ms)"].abs().mean()
    ]
)
plt.ylabel("Mean Absolute Clock Offset (ms)")
plt.title("Clock Offset Comparison")
plt.tight_layout()
plt.savefig("clock_offset.png")
plt.close()

print("Graphs generated successfully!")
print("Normal measurements:", len(normal))
print("Delayed measurements:", len(delayed))
