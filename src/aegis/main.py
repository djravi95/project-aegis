from .collector.evidence_collector import EvidenceCollector
from .validation.validation_engine import ValidationEngine
from .risk.risk_engine import RiskEngine
from .presentation.terminal_presenter import TerminalPresenter

def main():
    collector = EvidenceCollector()
    package = collector.collect("Hyderabad")
    validator = ValidationEngine()
    result = validator.validate(package)
    assessor = RiskEngine()
    risk_assessment = assessor.assess(package,result)
    print(risk_assessment)
    #presenter = TerminalPresenter()
    #presenter.display(package,result)
    #print("Project Aegis is operational.")


if __name__ == "__main__":
    main()