from re import split

def section_name(string):
	#split the folder name using - or _ as delimiters
	parts = split('[-_]', string)
	print parts
	capitalized_parts = []

	#capitalize each component
	for each_part in parts:
		capitalized_parts.append( each_part.capitalize() )

	#join it into our section name
	seperator = " "
	section_title = seperator.join(capitalized_parts)

	return section_title

def start_tex():
	body = '''\t\\documentclass{article}
	\\usepackage{amsmath, amsfonts}
	\\usepackage{physics}
	\\usepackage{graphicx}
	\\usepackage{siunitx}

	\\begin{document}

	''' 

	return body
def end_tex():
	body = '''
	\\end{document}
	'''
	return body
	pass

