def main():
    plate = input("Boundaries:\nBe between 2 and 6 characters inclusive\nNo non-alphanumeric (not letters and numbers) characters are allowed\nThe first two characters must be letters\nThe first number cannot be 0\nLetters cannot be placed after numbers\n" + "Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s.isalnum():
        return False

    if not s[0:2].isalpha():
       return False
    
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            return s[i:].isdigit()
        
    return True



    
     



main()
