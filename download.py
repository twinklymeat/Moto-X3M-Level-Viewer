import urllib.request
import os

try:
    os.makedirs("moto")
except:
    pass
try:
    os.makedirs("winter")
except:
    pass
try:
    os.makedirs("pool")
except:
    pass
try:
    os.makedirs("spooky")
except:
    pass

for i in range(1,26):
    print(f"Downloading Map {i}...")
    urllib.request.urlretrieve(f"https://moto-x3m.net/assets/levels/map{i}.json", f"moto\\{i}.json")
    print("Finished")

for i in range(1,26):
    print(f"Downloading Winter Map {i}...")
    urllib.request.urlretrieve(f"https://moto-x3m.net/winter/assets/levels/map{i}.json", f"winter\\{i}.json")
    print("Finished")

for i in range(1,23):
    print(f"Downloading Pool Party Map {i}...")
    urllib.request.urlretrieve(f"https://moto-x3m.net/pool-party/assets/levels/map{i}.json", f"pool\\{i}.json")
    print("Finished")

for i in range(1,23):
    print(f"Downloading Spooky Land Map {i}...")
    urllib.request.urlretrieve(f"https://moto-x3m.net/spooky-land/assets/levels/map{i}.json", f"spooky\\{i}.json")
    print("Finished")