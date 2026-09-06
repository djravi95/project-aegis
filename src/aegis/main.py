from .collector.evidence_collector import EvidenceCollector
from .validation.validation_engine import ValidationEngine
from .presentation.terminal_presenter import TerminalPresenter

def main():
    collector = EvidenceCollector()
    package = collector.collect("Hyderabad")
    validator = ValidationEngine()
    result = validator.validate(package)
    print(result)
    presenter = TerminalPresenter()
    presenter.display(package,result)
    #print("Project Aegis is operational.")


if __name__ == "__main__":
    main()