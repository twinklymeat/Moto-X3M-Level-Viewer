import urllib.request
import os
import pathlib


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
    urllib.request.urlretrieve(f"https://html5.gamedistribution.com/rvvASMiM/5b0abd4c0faa4f5eb190a9a16d5a1b4c/assets/levels/map{i}.json", pathlib.Path("moto",f"{i}.json"))
    print("Finished")

for i in range(1,26):
    print(f"Downloading Winter Map {i}...")
    urllib.request.urlretrieve(f"https://html5.gamedistribution.com/rvvASMiM/bcacf81441bd4c7799a622171116ea9d/assets/levels/map{i}.json", pathlib.Path("winter",f"{i}.json"))
    print("Finished")

for i in range(1,23):
    print(f"Downloading Pool Party Map {i}...")
    urllib.request.urlretrieve(f"https://html5.gamedistribution.com/f804d079d19f44d3b951ead4588e974a/assets/levels/map{i}.json", pathlib.Path("pool",f"{i}.json"))

for i in range(1,23):
    print(f"Downloading Spooky Land Map {i}...")
    urllib.request.urlretrieve(f"https://html5.gamedistribution.com/b8a342904608470a9f3382337aca3558/assets/levels/map{i}.json", pathlib.Path("spooky",f"{i}.json"))
    print("Finished")
