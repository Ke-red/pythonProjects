def main():
    print("This program counts the number of uppercase and lowercase letters, and words in a string.\n")
    string = input("Enter text:\n")
    upper = 0
    lower = 0
    words = 0
    numbers = 0
    
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1    
        elif char.isdigit():
            numbers += 1
    
    words = len(string.split())
        
    print(f"\nThe total uppercase letters is {upper}\nThe total lowercase letters is {lower}\nThe total numbers is {numbers}\nThe total word count is {words}")
main()
