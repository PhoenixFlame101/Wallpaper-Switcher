def get_refused_links(file):
	with open(file, 'r+') as f:
		return f.readline().split()

def add_to_refuse(url, file):
	if url not in get_refused_links(file):
		with open(file, 'a') as f:
			f.write(url + ' ')
