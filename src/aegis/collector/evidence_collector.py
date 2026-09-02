from .rainfall_collector import RainfallCollector
from .evidence_package import EvidencePackage
from datetime import datetime


class EvidenceCollector:
    """Coordinates all evidence collectors for a flood-risk analysis"""


    def __init__(self):
        self.rainfall_collector = RainfallCollector()

    def collect(self, district:str)-> EvidencePackage:
            rainfall = self.rainfall_collector.collect(district)

            return EvidencePackage(

                district=district,
                analysis_time=datetime.now(),
                evidences={"rainfall": rainfall},
                collection_status="Completed",
            )




