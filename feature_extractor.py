import pandas as pd
import pyshark

def extract_features(pcap_file):
    print("[*] Extracting features from:", pcap_file)
    capture = pyshark.FileCapture(pcap_file, only_summaries=True)
    data = []

    for packet in capture:
        try:
            data.append({
                'time': float(packet.time),
                'src': packet.source,
                'dst': packet.destination,
                'protocol': packet.protocol,
                'length': int(packet.length),
                'info': packet.info
            })
        except Exception:
            continue

    df = pd.DataFrame(data)
    df.to_csv("data/features.csv", index=False)
    print("[+] Features extracted to data/features.csv")

if __name__ == "__main__":
    extract_features("data/capture.pcap")
