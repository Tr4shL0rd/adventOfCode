def attempt1():
    elves = {}
    with open("input.txt", "r") as cal:
        lines = cal.readlines()
        elf_id = 1
        for line in lines:
            if line == "\n":
                elf_id += 1
            print(f"Elf#{elf_id}\t{line.strip()}")
            if line != "\n":
                elves[f"Elf#{elf_id}"] = int(line.strip())
    print(elves)

def attempt2():
    elves = {}
    x = []
    calories = []
    for i in range(1,255):
        elves[f"elf#{i}"] = 0
    with open("input.txt", "r") as cal:
        lines = cal.readlines()
        elf_id = 1
        for line in lines:
            if line == "\n":
                elf_id += 1
                calories = []
            else:
                calories.append(int(line.strip()))
                elves[f"elf#{elf_id}"] = calories
            x.append(sum(calories))

                #print(elves[f"elf#{elf_id}"])
            #print(line.strip())
        #print(elves[f"{max(elves)}"])
        #print(sum(elves[f"{max(elves)}"]))
        #print(calories)
        #print(elves[max(elves)])

        # stackoverflow https://stackoverflow.com/questions/60965915/python-program-program-to-find-largest-sequence-in-a-given-list-of-numbers
        from itertools import groupby
        from operator import itemgetter
        new_l = []
        for k, g in groupby(enumerate(x), lambda ix : ix[0] - ix[1]):
            new_l.append(list(map(itemgetter(1), g)))

        print(new_l)
        print(max(new_l, key=lambda x: len(x)))
        #print(x)
def attempt3():
    calories = []
    sums = []
    with open("input.txt", "r") as cal:
        for line in cal.readlines():
            if line.strip() != "":
                calories.append(int(line))
            else:
                elf_total = sum(calories)
                sums.append(elf_total)
                calories = []
    print(max(sums))
attempt3()