from Subsystem import (RawMaterials, Mixing, Calenders, Building, Curing, FinalFinish, Logistics)

def main():
	raw = RawMaterials()
	mixer = Mixing()
	calender = Calenders()
	builder = Building()
	cure = Curing()
	tester = FinalFinish()
	trucks = Logistics()


	raw.get_materials()
	mixer.mix_materials()
	calender.cut_cords()
	builder.assembly_tires()
	cure.cure_tires()
	tester.test_tires()
	print(trucks.send_tires())


if __name__ == "__main__":
	main()