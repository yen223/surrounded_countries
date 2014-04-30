east = {}
west = {}
north = {}
south = {}

with open('east') as f:
    for idx,line in enumerate(f):
        east[line.strip()] = idx

with open('west') as f:
    for idx,line in enumerate(f):
        west[line.strip()] = idx

with open('north') as f:
    for idx,line in enumerate(f):
        north[line.strip()] = idx

with open('south') as f:
    for idx,line in enumerate(f):
        south[line.strip()] = idx

for c1 in south:
    for c2 in south:
        if c1 not in north or c1 not in south or c1 not in east or c1 not in west:
            continue
        if c2 not in north or c2 not in south or c2 not in east or c2 not in west:
            continue
        if north[c1] < north[c2] and east[c1] < east[c2] and west[c1] < west[c2] and south[c1] < south[c2]:
            print "{} and {}".format(c1, c2)
