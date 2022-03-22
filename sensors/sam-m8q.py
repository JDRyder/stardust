import melopero_samm8q as samm8q

def gps():
	sensor = samm8q.SAM_M8Q()#default address 0x42
	#sensor = samm8q.SAM_M8Q(i2c_addr = myaddress, i2c_bus = mybus)

	sensor.get_pvt()

	longitude = sensor.pvt_data["longitude"]
	latitude = sensor.pvt_data["latitude"]

	print("We are at lat " + str(latitude) + " and longitude " + str(longitude))
