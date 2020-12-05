import sys


def read_steps(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    steps = []
    step_map = {"(": 1, ")": -1}
    for s in raw.strip():
        steps.append(step_map[s])
    
    return steps


def ride(steps=None, start=0):
    
    for step in steps:
        start += step
    
    return start
    

if __name__ == "__main__":
    steps = read_steps(sys.argv[-1])
    dest = ride(start=0, steps=steps)
    print(dest)