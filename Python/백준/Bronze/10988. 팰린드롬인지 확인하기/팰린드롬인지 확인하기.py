def palindrome(s):
    for i in range(int(len(s)/2)):
        if s[i]!=s[len(s)-i-1]:
            return 0
    return 1

print(palindrome(list(input())))