import re
def a(x):
    s = re.split('a|i|o|u', x)
    x=''
    for i in s:
        x += i
    return x
if __name__ == "__main__":
    o = "hihi hi"
    print(a(o))
