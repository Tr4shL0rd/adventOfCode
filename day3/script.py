import string
def attempt1():
    ALPHABET = list(string.ascii_letters)
    #print(ALPHABET)
    letter_priority = {}
    score = 1
    for letter in ALPHABET:
        letter_priority[letter] = score
        score += 1
    print(letter_priority)
    exit()
    
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lineNum = 1
        for line in lines:
            lineNum += 1
            comp1,comp2 = line.strip()[:len(line.strip())//2], line.strip()[len(line.strip())//2:]
            print(f"line {lineNum}\n\tcompartment1: {comp1}\n\tcompartment2: {comp2}")
            for let1 in comp1:
                if let1 in comp2:
                    print(f"{let1} in comp1 & comp2")
            #input()
attempt1()