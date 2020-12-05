import sys


def read_dimensions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    dims = []
    for raw_dim in raw.split("\n"):
        dims.append([int(d) for d in raw_dim.strip().split("x")])
    
    return dims


def ribbon_for_dimensions(dim):
    
    # convert to sides
    perims = [
        2 * dim[0] + 2 * dim[1],
        2 * dim[0] + 2 * dim[2],
        2 * dim[1] + 2 * dim[2]
    ]
    
    # smallest side
    perims = sorted(perims)
    
    return perims[0] + (dim[0] * dim[1] * dim[2])


if __name__ == "__main__":
    dims = read_dimensions(sys.argv[-1])
    paper = sum([ribbon_for_dimensions(dim) for dim in dims])
    
    print("%d feet" % (paper,))