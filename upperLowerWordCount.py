def main():
    print("This program counts the number of uppercase and lowercase letters, and words in a string.\n")
    string = input("Enter text:\n")
    upper = 0
    lower = 0
    words = 0
    
    for char in string:
        if char.isupper():
            upper += 1
        else:
            lower += 1    
        
    words = len(string.split())
        
    print (f"\nThe amount of uppercase letters in your text is {upper}\nThe amount of lowercase letters in your text is {lower}\nThe total word count is {words}")
main()
