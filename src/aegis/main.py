from collector.evidence_collector import EvidenceCollector

def main():
    collector = EvidenceCollector()
    package = collector.collect("Hyderabad")
    print(package)
    print("Project Aegis is operational.")


if __name__ == "__main__":
    main()