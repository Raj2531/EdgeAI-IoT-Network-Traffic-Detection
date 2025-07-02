import os
import time

def capture_packets(output_file="data/capture.pcap", duration=10):
    print("[*] Starting packet capture...")
    os.system(f"sudo timeout {duration} tcpdump -i any -w {output_file}")
    print(f"[+] Packet capture saved to {output_file}")

if __name__ == "__main__":
    capture_packets()
