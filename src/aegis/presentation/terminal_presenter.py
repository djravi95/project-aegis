from ..models.validation_result import ValidationResult
from ..models.risk_result import RiskResult
from ..config.required_evidence import REQUIRED_EVIDENCE

class TerminalPresenter:
    """Displays Project Aegis results in the terminal"""

    def display(self, package, validation_result,risk_result):
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

        

        for evidence_name,status in validation_result.validation_details.items():
                evidence = package.evidences[evidence_name]
                if status == 'VALID':
                     symbol= '✓'
                else: symbol = '✗'

                print(f"{evidence.name:<20}: {symbol} {status}")


        print()
        print(f"{'Overall Status':<20}: {validation_result.status}")
        print()
        print("-" * 60)

        print("Warnings")
        print("-" * 60)

        if not validation_result.warnings:

             print("None")

        else: 
             for action in validation_result.warnings:
                  print(f". {action}")

        print()

        print("-" * 60)
        print("Risk Assessment")
        print("-" * 60)


        print(f"{'Overall Risk':<20}: {risk_result.risk_level}")
        print(f"{'Risk Score':<20}: {risk_result.risk_score} / 100")
        print(f"{'Confidence':<20}: {risk_result.confidence}")

        print()

        print("Risk Contribution")
        print("-" * 60)

        print(f"{'Rainfall':<20}: {risk_result.rainfall_assessment.score}")
        print(f"{'DEM':<20}: {risk_result.dem_assessment.score}")
                

        print("Rainfall Assessment")
        print("-" * 60)
        print()

        print(f"{'Level':<20}: {risk_result.rainfall_assessment.level}")
        print(f"{'Score':<20}: {risk_result.rainfall_assessment.score}")
        print(f"{'Reason':<20}: {risk_result.rainfall_assessment.reason}")

        print()

        print("DEM Assessment")
        print("-" * 60)
        print()
        
        print(f"{'Level':<20}: {risk_result.dem_assessment.level}")
        print(f"{'Score':<20}: {risk_result.dem_assessment.score}")
        print(f"{'Reason':<20}: {risk_result.dem_assessment.reason}")
    
        print()

        print("-" * 60)
        print("Recommended Actions")
        print("-" * 60)

        for action in risk_result.recommended_actions:
             print(f". {action}")

        print()

        print("=" * 60)


        


        
        
        
        
        