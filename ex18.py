# like argv scripts
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1,arg2)

# ok that *args is pointless we can jsut do
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" %(arg1,arg2)

# takes 1 arg
def print_one(arg1):
	print "arg1: %r" % arg1

# no args
def print_none():
	print "I got nothin"

print_two("Zed","shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()