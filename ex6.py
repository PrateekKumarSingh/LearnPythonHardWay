x = "there are %d type of people." % 10
binary = "binary"
do_not="don't"
y = "Those who know %s and those who %s" % (binary, do_not)
print(x)
print(y)

print("I said: %r" % x)
print("I also said :'%s'" % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "this is left side of a string | "
e = "I'm the right side of the string"
n = 1
print("Debug : %r" % (w+e+n))