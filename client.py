
import socket
import time
import csv
import os

HOST = "10.0.0.1"
PORT = 5005

MAX_RETRIES = 3
TIMEOUT = 2

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(TIMEOUT)

try:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            t1 = time.time()
            client_socket.sendto(b"TIME", (HOST, PORT))

            data, server_address = client_socket.recvfrom(1024)
            t4 = time.time()

            print(f"Response received on attempt {attempt}")
            break

        except socket.timeout:
            print(f"Attempt {attempt} timed out.")

    else:
        print("Error: Server did not respond after 3 attempts.")
        raise SystemExit

    t2, t3 = map(float, data.decode().split(","))

    delay = (t4 - t1) - (t3 - t2)
    offset = ((t2 - t1) + (t3 - t4)) / 2

    local_clock = time.time()
    corrected_clock = local_clock + offset

    print("Client local time:", f"{local_clock:.6f}")
    print("Estimated synchronized time:", f"{corrected_clock:.6f}")
    print("Applied correction:", f"{offset * 1000:.3f} ms")
    print("Estimated network delay:", delay, "seconds")
    print("Estimated clock offset:", offset, "seconds")

    # Save results to CSV
    filename = "/home/avani/network-time-sync/results.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Attempt",
                "Network Delay (ms)",
                "Clock Offset (ms)"
            ])

        writer.writerow([
            time.strftime("%Y-%m-%d %H:%M:%S"),
            attempt,
            round(delay * 1000, 3),
            round(offset * 1000, 3)
        ])

    print("Results saved to results.csv")

finally:
    client_socket.close()

