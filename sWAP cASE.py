def swap_case(s):
    newString = ""
    for char in s:
        if (char.isupper()==False):
            newString = newString + char.upper()
        if (char.isupper()==True):
            newString = newString + char.lower()
    return newString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print (result)
