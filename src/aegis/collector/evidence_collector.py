from .rainfall_collector import RainfallCollector
from .dem_collector import DemCollector
from .evidence_package import EvidencePackage
from datetime import datetime


class EvidenceCollector:
    """Coordinates all evidence collectors for a flood-risk analysis"""


    def __init__(self):
        self.rainfall_collector = RainfallCollector()
        self.dem_collector = DemCollector()

    def collect(self, district:str)-> EvidencePackage:
            rainfall = self.rainfall_collector.collect(district)
            dem = self.dem_collector.collect(district)

            return EvidencePackage(

                district=district,
                analysis_time=datetime.now(),
                evidences= {"rainfall": rainfall,
                           "dem": dem
                           },
                collection_status="Completed",
            )




