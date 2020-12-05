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
    
    for step_idx in range(len(steps)):
        step = steps[step_idx]
        start += step
        if start < 0:
            return step_idx + 1
    
    return None
    

if __name__ == "__main__":
    steps = read_steps(sys.argv[-1])
    dest = ride(start=0, steps=steps)
    print(dest)