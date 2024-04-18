def is_palindrome(s):
    # Convert the string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    # Check if the string is equal to its reverse
    return s == s[::-1]

input_string = input("Enter a string to check for palindrome: ")

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print("The input is not a palindrome.")
