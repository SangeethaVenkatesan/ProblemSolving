
def validAnagram(s, t):
    # made up of same list of characters
    # Counter(s) == Counter(t)
    # sorted(s) == sorted(t)
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
    for i in range(len(t)):
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    check = validAnagram(s, t)
    print(check)

    # time complexity : O(s+t)
    # space complexity : O(s+t)
