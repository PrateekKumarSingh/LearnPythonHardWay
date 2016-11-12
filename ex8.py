#formatter = "%s %s %s %s"
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % (True, False, False, True))
print(formatter % (
"My name is Prateek",
"I'm 26 year old",
"I live in new delhi",
"and am computer engineer by profession"
))