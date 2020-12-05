import sys


def read_dimensions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    dims = []
    for raw_dim in raw.split("\n"):
        dims.append([int(d) for d in raw_dim.strip().split("x")])
    
    return dims


def paper_for_dimensions(dim):
    
    # convert to sides
    sides = [
        dim[0] * dim[1],
        dim[0] * dim[2],
        dim[1] * dim[2]
    ]
    
    # smallest side
    sides = sorted(sides)
    
    # final calculation
    return (sides[0] * 3) + (sides[1] * 2) + (sides[2] * 2)


if __name__ == "__main__":
    dims = read_dimensions(sys.argv[-1])
    paper = sum([paper_for_dimensions(dim) for dim in dims])
    
    print("%d sqft" % (paper,))