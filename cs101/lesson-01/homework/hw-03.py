# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

#part_one = s.find('u')
#part_two = t.find('dacious')
#word = s[:part_one+1] + t[part_two:]
#print word

print s[:1] + t[2:]
