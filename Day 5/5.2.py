import re
import fileinput

# nnlist = [letter for point in fileinput.input() for letter in point]
nnlist = [point for point in fileinput.input()]

# Part 2
print(len([line for line in nnlist if (re.search(r'(..).*\1', line) and re.search(r'(.).\1', line))]))

# Shout out to u/technojamin from the AoC subreddit for this solution. I couldn't for the life of me get it with what I knew
# but my understanding of regex is far greater for this.
# Still prefer using open/with than fileinput though