from string import ascii_lowercase

with open("The list.txt") as file:
    nnlist = [line.strip("\n") for line in file.readlines()]

bad = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]
dbl = [letter + letter for letter in ascii_lowercase] # Makes a list of double letters because I'm way too lazy for that :)

naughty = []
nice = []

for entry in nnlist:
    if any(a in entry for a in bad):
        pass
    else:
        v_count = 0
        for cha in entry:
            if cha in vowels:
                v_count += 1
            
        if (v_count > 2):
            if (any(b in entry for b in dbl)):
                nice.append(entry)
