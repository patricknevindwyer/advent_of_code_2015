import sys


def read_instructions(filename):
    """
    toggle 461,550 through 564,900
    turn off 812,389 through 865,874
    turn on 599,989 through 806,993
    """
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    steps = []
    
    for line in raw.split("\n"):
        task = None
        rect = None
        
        # figure out the action
        if line.startswith("toggle"):
            task = "toggle"
            rect = line[7:]
        elif line.startswith("turn off"):
            task = "off"
            rect = line[9:]
        elif line.startswith("turn on"):
            task = "on"
            rect = line[8:]
        
        # parse the range
        tl, br = rect.split(" through ")
        t, l = tl.split(",")
        b, r = br.split(",")
        
        steps.append((task, int(t), int(l), int(b), int(r)))
    
    return steps
    

class Grid:
    
    def __init__(self, size=1000, fill=0):
        self.grid = []
        for idx_y in range(size):
            self.grid.append([fill for idx_x in range(size)])
    
    def update(self, top=0, left=0, bottom=0, right=0, fn=None):
        
        for idx_y in range(top, bottom + 1):
            for idx_x in range(left, right + 1):
                self.grid[idx_y][idx_x] = fn(self.grid[idx_y][idx_x])
    
    def count(self, state=1):
        cnt = 0
        for idx_y in range(len(self.grid)):
            for idx_x in range(len(self.grid)):
                if self.grid[idx_y][idx_x] == state:
                    cnt += 1
        return cnt


if __name__ == "__main__":
    steps = read_instructions(sys.argv[-1])
    grid = Grid()
    
    funcs = {
        "toggle": lambda c: (c + 1) % 2,
        "off": lambda c: 0,
        "on": lambda c: 1
    }
    
    for task, t, l, b, r in steps:
        grid.update(top=t, left=l, bottom=b, right=r, fn=funcs[task])
    print("%d cells active" % (grid.count(),))