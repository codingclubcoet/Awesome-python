#using geopy module we can calculate the distance

try:
	from geopy import distance as d
except ImportError:
	print("[!] Sorry geopy not installed")
	print("[!] To install pip3 install geopy")

india = ("20.5937° N, 78.9629° E")
japan = ("36.2048° N, 138.2529° E")

dis = d.distance(india,japan).km

print("The distance between India and Japan is {} kilometers".format(dis))
