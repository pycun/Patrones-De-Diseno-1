from Subsystem import (RawMaterials, Mixing, Calenders, Building, Curing, FinalFinish, Logistics)

class TireFabric:
    
    def __init__(self):
        self.raw = RawMaterials()
        self.mixer = Mixing()
        self.calender = Calenders()
        self.builder = Building()
        self.cure = Curing()
        self.tester = FinalFinish()
        self.trucks = Logistics()
        
    def sell_tires(self):
        self.raw.get_materials()
        self.mixer.mix_materials()
        self.calender.cut_cords()
        self.builder.assembly_tires()
        self.cure.cure_tires()
        self.tester.test_tires()
        result = "-------- \n" + self.trucks.send_tires()
        return result