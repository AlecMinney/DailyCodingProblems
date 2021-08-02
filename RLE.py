def rle(data):
    prev = ''
    final = ""
    count = 1

    if not data: return ""
    for char in data:
        if char == prev:
            count += 1
        else:
            if prev:
                final += str(count) + prev
            prev = char
            count = 1
    final += str(count) + prev
    return final

def rled(data):
    final = ""
    flag = True
    num = 1

    if not data: return ""
    for char in data:
        if flag:
            num = int(char)
            flag = False
        else:
            for i in range(num):
                final += char
            flag = True
    return final

string = input("enter string to encode")
encoded = rle(string)
print(encoded)
string2 = input("enter string to decode")
decoded = rled(string2)
print(decoded)
