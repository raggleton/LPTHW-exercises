my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %r." % my_name
print "He's %r inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age+my_height+my_weight)

