def isPalindrome(word):
    reversed = ""

    for i in range(len(word)-1,-1,-1):
        reversed += word[i]

    if word == reversed:
        return f"{ word } in reverse is { reversed }. It is a palindrome"
    else :
        return f"{ word } in reverse is { reversed }. It is not a palindrome"

print(isPalindrome("madam"))
print(isPalindrome("erm"))
print(isPalindrome("Hannah"))
print(isPalindrome("12321"))