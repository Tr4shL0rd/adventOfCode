import string
def attempt1():
    ALPHABET = list(string.ascii_letters)
    #print(ALPHABET)
    letter_priority = {}
    score = 1
    for letter in ALPHABET:
        letter_priority[letter] = score
        score += 1
    #print(letter_priority)
    #exit()
    total_sum = 0
    priorities = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lineNum = 1
        for line in lines:
            lineNum += 1
            comp1,comp2 = line.strip()[:len(line.strip())//2], line.strip()[len(line.strip())//2:]
            print(f"line {lineNum}\n\tcompartment1: {comp1}\n\tcompartment2: {comp2}")
            for let1 in comp1:
                if let1 in comp2:
                    print(f"\"{let1}\" in comp1 & comp2")
                    total_sum += letter_priority[let1]
                    priorities.append(let1)
                    #total_sum.append(let1)
            #print(total_sum)
            print(priorities)
            for p in priorities:
                print(letter_priority[p])
            #for let in total_sum:
                #total_sum.append(letter_priority[let])
            #input()
attempt1()