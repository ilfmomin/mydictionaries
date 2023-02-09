import json

# load the eq_data json file 
with open("eq_data.json", "r") as y:
    x = json.load(y)

# the amount of earthquakes 
print("Number of earthquakes: ", len(x["features"]))

# get the information of earthquakes that had a magnitude of 6 or more 
eq_dict = {}
for i, eq in enumerate(x["features"]):
    if eq["properties"]["mag"] > 6:
        eq_dict[i] = {
            "location": eq["properties"]["place"],
            "magnitude": eq["properties"]["mag"],
            "longitude": eq["geometry"]["coordinates"][0],
            "latitude": eq["geometry"]["coordinates"][1]
        }

# Print the new updated dictionary containing earthquakes with magnitude of 6 or more 
print("Earthquakes with magnitude > 6:")
print(eq_dict)

for i, eq in eq_dict.items():

    print("Location:", eq["location"])
    print("Magnitude:", eq["magnitude"])
    print("Longitude:", eq["longitude"])
    print("Latitude:", eq["latitude"])
    print()