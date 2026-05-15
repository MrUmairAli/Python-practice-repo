'''import json
m=["january","march","may","july","august","october","december"]
n=["april","june","september","november"]
o=["february"]
q=[m,n]
with open("hy.json","w") as d:
  json.dump(q,d)
with open("hy.json","r") as d:
  p=json.load(d)
print(p)
print(p[1])'''
import json

m = ["january","march","may","july","august","october","december"]
n = ["april","june","september","november"]

# Append each list as a separate JSON object per line
with open("hw.json", "a") as f:
    json.dump(m, f)
    f.write("\n")
    json.dump(n, f)
    f.write("\n")

# Read and parse each JSON line
with open("hw.json", "r") as f:
    for line in f:
        data = json.loads(line)  # <-- use json.loads(), not json.load()
        print(data)

