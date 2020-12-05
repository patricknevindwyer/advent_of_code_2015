import sys

def read_directions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    return raw.strip()


def deliver(dirs):
    
    s_loc_x = 0
    s_loc_y = 0

    r_loc_x = 0
    r_loc_y = 0
    
    # track where we've delivered
    deliveries = {}
    
    # deliver our first spot
    deliveries[(s_loc_x, s_loc_y)] = 1
    deliveries[(r_loc_x, r_loc_y)] = 1
    
    for step_idx in range(len(dirs)):
        step = dirs[step_idx]
        
        if step_idx % 2 == 0:
            if step == ">":
                s_loc_x += 1
            if step == "<":
                s_loc_x -= 1
            if step == "^":
                s_loc_y -= 1
            if step == "v":
                s_loc_y += 1
            
            # deliver
            loc = (s_loc_x, s_loc_y)
            if loc not in deliveries:
                deliveries[loc] = 0
        
            deliveries[loc] += 1
            
        else:
            if step == ">":
                r_loc_x += 1
            if step == "<":
                r_loc_x -= 1
            if step == "^":
                r_loc_y -= 1
            if step == "v":
                r_loc_y += 1
        
            # deliver
            loc = (r_loc_x, r_loc_y)
            if loc not in deliveries:
                deliveries[loc] = 0
        
            deliveries[loc] += 1
        
    
    return deliveries


if __name__ == "__main__":
    
    directions = read_directions(sys.argv[-1])
    deliveries = deliver(directions)
    print("%d houses got presents" % (len(deliveries),))