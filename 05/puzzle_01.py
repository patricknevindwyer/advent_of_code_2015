import sys


def read_strings(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    return raw.split("\n")


def has_vowels(s, count=3):
    vs = "aeiou"
    return len([c for c in s if c in vs]) >= count


def has_runs(s, length=2, count=1):
    runs = []
    
    carry = [s[0]]
    
    for c in s[1:]:
        if c == carry[0]:
            carry.append(c)
        else:
            runs.append("".join(carry))
            carry = [c]
    
    runs.append("".join(carry))
    
    return len([r for r in runs if len(r) >= length]) >= count


def excludes_bad_strings(s):
    for bad in ["ab", "cd", "pq", "xy"]:
        if bad in s:
            return False
    return True
    
    
def is_nice(s):
    return has_vowels(s) and has_runs(s) and excludes_bad_strings(s)


if __name__ == "__main__":
    strings = read_strings(sys.argv[-1])
    nice_strings = [s for s in strings if is_nice(s)]
    print(nice_strings)
    print(len(nice_strings))

