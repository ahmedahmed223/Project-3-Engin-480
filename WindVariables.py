import json
import numpy as np
import matplotlib.pyplot as matplotlib

def main():
    with open("line.geojson", "r") as a:
        data = json.load(a)
    feature = data["features"][0]
    coordinates = feature["geometry"]["coordinates"]
    arr = np.array(coordinates)

    matplotlib.figure(figsize=(8, 6))
    matplotlib.plot(arr[:, 0], arr[:, 1])
    matplotlib.xlabel("longitude")
    matplotlib.ylabel("latitude")
    matplotlib.title("Wind Turbine Farms/Generators/Inter-Array Cables")
    matplotlib.grid(True)
    matplotlib.show()


    np.save("line_array.npy", arr)
    
if __name__ == '__main__':
    main()