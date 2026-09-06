from ..validation.validation_result import ValidationResult
from ..config.required_evidence import REQUIRED_EVIDENCE

class TerminalPresenter:
    """Displays Project Aegis results in the terminal"""

    def display(self, package, validation_result):
        print("=" * 60)
        print(f"{'PROJECT AEGIS':^60}")
        print("=" * 60)
        print()

        print(f"{'District':<20}: {package.district}")
        print(f"{'Analysis Time':<20}: {package.analysis_time}")
        print()

        print("-" * 60)
        print("Evidence Summary")
        print("-" * 60)

        for _,evidence in package.evidences.items():

            print(f"{'Name':<20}: {evidence.name}")
            print(f"{'Value':<20}: {evidence.value} {evidence.unit}")
            print(f"{'Source':<20}: {evidence.source}")
            print(f"{'Location':<20}: {evidence.location}")
            print(f"{'Status':<20}: {evidence.status}")
            print(f"{'Confidence':<20}: {evidence.confidence}")
            print()

        print("-" * 60)
        print("Validation Summary")
        print("-" * 60)

        

        for evidence_name in REQUIRED_EVIDENCE:
                evidence = package.evidences[evidence_name]
                print(evidence.name)
                print(validation_result.status)

        print()
        print("=" * 60)


        


        
        
        
        
        