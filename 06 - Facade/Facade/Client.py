from Facade import TireFabric

def main():
	FACADE = TireFabric()
	result = FACADE.sell_tires()
	print(result)


if __name__ == "__main__":
	main()