# This is a python script designed to make one book for each main folder,
# Containing ONLY the questions!


import os
from os.path import join
#here is our library
from prereqs import *

walker = os.walk('.')

toptuple = walker.next()

chapters = toptuple[1]	#get all the main problem types,

#but we need to remove hidden folders.
chapters = [x for x in chapters if x[0] != '.']
# print chapters

#Walk through each chapter to make the book.
for each_chapter in chapters:
	#our tex file to be compiled
	fname = each_chapter + "_qs_only.tex"
	maintex = file(each_chapter + "_qs_only.tex", "w")

	#Start off the tex with the goodies
	maintex.write(start_tex())

	#Get a list of all the sections
	ch_walker = os.walk(join('.', each_chapter));
	toptuple = ch_walker.next()
	subjects = toptuple[1];

	#print each section
	for each_subject in subjects:
		line = "\section{" + section_name(each_subject) + "}\n"
		maintex.write(line)

		#for loop for adding each question

	#finish it all off
	maintex.write(end_tex())
	maintex.close()