from capture.packet_capture import capture_packets
from preprocessing.feature_extractor import extract_features
from models.train_model import train
from inference.inference_engine import run_inference
from utils.evaluate import evaluate

if __name__ == "__main__":
    capture_packets(duration=10)
    extract_features("data/capture.pcap")
    train()
    run_inference()
    evaluate()
