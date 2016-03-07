import os

walker = os.walk('.')

toptuple = walker.next()

chapters = toptuple[1]	#get all the main problem types,

#but we need to remove hidden folders.
chapters = [x for x in chapters if x[0] != '.']
print chapters

# for eachchapter in chapters:
