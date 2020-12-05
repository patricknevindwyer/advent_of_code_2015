import sys

def read_directions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    return raw.strip()


def deliver(dirs):
    loc_x = 0
    loc_y = 0
    
    # track where we've delivered
    deliveries = {}
    
    # deliver our first spot
    deliveries[(loc_x, loc_y)] = 1
    
    for step in dirs:
        if step == ">":
            loc_x += 1
        if step == "<":
            loc_x -= 1
        if step == "^":
            loc_y -= 1
        if step == "v":
            loc_y += 1
        
        # deliver
        loc = (loc_x, loc_y)
        if loc not in deliveries:
            deliveries[loc] = 0
        
        deliveries[loc] += 1
    
    return deliveries


if __name__ == "__main__":
    
    directions = read_directions(sys.argv[-1])
    deliveries = deliver(directions)
    print("%d houses got presents" % (len(deliveries),))