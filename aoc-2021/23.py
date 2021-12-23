#!/usr/bin/env python3.10
part1, part2 = 11332, 49936

# Did both parts by hand. 
# The key is to minimize the movement of D blocks as much as possible
# Then prioritize minimizing the movement of C, then B, and then finally A.
# In general, you should always move A instead of (B,C,D) if possible.

# Part 1 has multiple solutions, so you need to be careful.
# I suspect Part 2 has very few valid solutions due to the blocking nature of
# the rules, you find out very quickly that you're stuck and can restart.

# I did it in vim while keeping track of my moves in a python console. It's easy
# to lose track of what moves you made so it's best to do this in a spreadsheet.

# If I were to write a solution for this in code, it would probably be using A*
# to implement a depth-first search with h(x) being the energy required if
# moving through other amphipods was possible, or just plain old Dijkstra.
# But I don't think it's going to be a lot of fun, since most of the rules are
# just busywork and a test of reading comprehension, which you doesn't matter
# if you solved it by hand already.

print(part1, part2)
