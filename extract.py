def transform(oldtext):
	oldtext = oldtext.strip().split(' ', 1)
	k,v = oldtext[0], oldtext[1].strip()
	newtext = '\t"' + k + '" : " ' + v + ' ", \n'
	return newtext

with open('dict6', 'r') as source:
	with open('dict6.json', 'w') as sink:
		sink.write('{\n')
		for line in source:
			sink.write(transform(line))
		sink.write('}')

