from .collector.evidence_collector import EvidenceCollector
from .validation.validation_engine import ValidationEngine

def main():
    collector = EvidenceCollector()
    package = collector.collect("Hyderabad")
    validator = ValidationEngine()
    result = validator.validate(package)
    print(package)
    print(result)
    print("Project Aegis is operational.")


if __name__ == "__main__":
    main()