from reddit_functions import get_walls
from local_functions import need_new_walls, move, set_wall, usable_walls, delete_files
from os import listdir

folder_path = 'C:/Users/Abhinav/Pictures/Wallpapers/'
current_path = 'C:/Users/Abhinav/Pictures/Wallpapers/Current/'
refuse_path = 'C:/Users/Abhinav/Pictures/Wallpapers/Current/refuse.txt'

if len(listdir(folder_path)) > 3:
	delete_files(folder_path)

if need_new_walls(folder_path):
	get_walls(folder_path, refuse_path)

move(folder_path, current_path)
set_wall(current_path+usable_walls(current_path)[0])
