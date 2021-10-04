import os, sys, shutil

#!----------Files and folders----------!#
# Rename a file
os.rename(old_file, new_file)

# Copy a file
shutil.copy(old_file, new_file)

# Get a list containing all files and folders (not including sub-folders) in 'PATH'
os.listdir('PATH')

# Add to PATH
sys.path.append('PATH')

# Write a file
with open('PATH_to_the_file', 'a') as f:
	print('contents', file=f)

# Current working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Get the home directory
# Option 1
os.getenv("HOME")
# Option 2
os.path.expanduser("~")
""" 在linux下面，一般如果你自己使用系统的时候，是可以用~来代表＂/home/你的名字/＂这个路径的.
    但是python是不认识~这个符号的，如果你写路径的时候直接写＂~/balabala＂，程序是跑不动的.
    所以如果你要用~，你就应该用这个os.path.expanduser把~展开 """

#?----------Files and folders----------?#

# Pre-set a length for variables printed in a string
print('%-10f: %10f' % (a, b))
string = '{:5s}{:5s}{:>5s}'.format('a', 'b', 'c')
print(string)

# create lists for in-list elements
list1 = ['A', 'B', 'C', 'D']
for i in list1:
	exec(f"{i} = []")

# Separate the string according to contained spaces to fill a list
value = string.split()

# Pass max(a, b) to c
c = (a>b and [a] or [b])[0]

# Create a copy of a list
list_copy = list_name[:]
