from src.facility import *

class FacilityFactory:
    def __init__(self):
        pass

    def create_facility(self, facility_type):
        if facility_type is FacilityType.WheatField:
            return WheatField()
        elif facility_type is FacilityType.Bakery:
            return Bakery()
