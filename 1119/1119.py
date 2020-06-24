import re
def a(x):
    return ''.join(re.split('a|i|e|o|u', x))
    # sorry for the one liner but hey
if __name__ == "__main__":
    o = "hihi hi"
    print(a(o))
