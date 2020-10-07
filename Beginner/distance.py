#using geopy module we can calculate the distance

try:
	from geopy import distance as d
except ImportError:
	print("[!] Sorry geopy not installed")
	print("[!] To install pip3 install geopy")

india = ("20.5937° N, 78.9629° E")
usa = ("37.0902° N, 95.7129° W")

dis = d.distance(india,usa).km

print("The distance between India and USA is {} kilometers".format(dis))