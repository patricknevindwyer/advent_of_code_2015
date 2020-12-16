import sys


def read_strings(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    return raw.split("\n")


def has_substring_doubling(s):
    # 12345
    for idx in range(len(s) - 3):
        root = s[idx:idx + 2]
        if root in s[idx + 2:]:
            print("  doubling of [%s]" % (root,))
            return True
    return False
    

def has_vampire_letter(s):
    for idx in range(len(s) - 2):
        left = s[idx]
        pivot = s[idx + 1]
        right = s[idx + 2]
        
        if (left == right):# and (right != pivot):
            print("  vampire")
            return True
    return False
    
        
def is_nice(s):
    print("?[%s]" % (s,))
    return has_substring_doubling(s) and has_vampire_letter(s)


if __name__ == "__main__":
    strings = read_strings(sys.argv[-1])
    nice_strings = [s for s in strings if is_nice(s)]
    print(nice_strings)
    print(len(nice_strings))

