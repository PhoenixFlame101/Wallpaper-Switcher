""" Changes wallpapers """

import os
from ctypes import windll

def file_extension(file, *args):
	""" Returns the file extension of a given file """
	char = args[0] if args else '.'
	try:
		return file[-(list(file[::-1]).index(char)+1):]
	except:
		return '.png'

def usable_walls(path):
	""" Returns all the usable wallpapers """
	usable_walls = []
	for file in os.listdir(path):
		if file not in ('Current', 'refuse.txt') and file[:4] != 'used' and file[-3:] != 'lnk':
			usable_walls.append(file)
	return usable_walls

def need_new_walls(path):
	""" Checks if there are less than 2 usable walls """
	return (True if len(usable_walls(path)) == 0 else False)

def move(root, cur):
	""" Moves the wallpaper from the root dir to the 'Current' dir """
	new_wall = usable_walls(root)[0]
	try:
		current_wall = usable_walls(cur)[0]
	except IndexError:
		open(root+'Current/current.png','x')
		current_wall = usable_walls(cur)[0]
	if current_wall[-4:] != '.txt':
		os.rename(cur+current_wall, root+'used'+new_wall[:-len(file_extension(new_wall))]+file_extension(current_wall))
	else:
		pass
	os.rename(root+new_wall, cur+'current'+file_extension(new_wall))

def set_wall(file):
	""" Sets the wall in 'Current' as wallpaper """
	windll.user32.SystemParametersInfoW(20, 0, file, 0)

def delete_files(path):
	""" Deletes all wallpapers that were used """
	flagged = []
	for file in os.listdir(path):
		if file[:4] == 'used':
			flagged.append(file)
	for file in flagged[::-1]:
		os.remove(path+'/'+file)
