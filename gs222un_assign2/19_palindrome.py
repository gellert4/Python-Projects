def is_palindrome(s):
    letters = ""
    for char in s:
        if char.isalpha():
            letters += char
    letters = letters.lower().replace(" ", "")
    return letters == letters[::-1]


print("Is palindrome if it contains the same sequence of letters" +
      "when read backwards. We make no difference between upper" +
      "and lower case letters.")
a = input("Please provide a sentence: ")
print(f"Your sentence is palindrome: {is_palindrome(a)}")
