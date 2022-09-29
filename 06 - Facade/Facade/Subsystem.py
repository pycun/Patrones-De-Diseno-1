class RawMaterials:
    
    def get_materials(self):
        print('RawMaterials -> get_materials')
        return "*Materials arrived."
    
class Mixing:
    
    def mix_materials(self):
        print('Mixing -> mix_materials')
        return "*Mixing done."
    
class Calenders:
    
    def cut_cords(self):
        print('Calenders -> cut_cords')
        return "*Cord materials are cut."

class Building:
    
    def assembly_tires(self):
        print('Building -> assembly_tires')
        return "*Green tire is obtained."
    
class Curing: 
    
    def cure_tires(self):
        print('Curing -> cure_tires')
        return "*Tires are cured."
    
class FinalFinish:
    
    def test_tires(self):
        print('FinalFinish -> test_tires')
        return "*Tires are tested."
    
class Logistics:
    
    def send_tires(self):
        print('Logistics -> send_tires')
        return "*Tires are sold. You can buy a new Maserati"
