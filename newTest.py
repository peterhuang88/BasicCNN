import os

def perform_move():
	source = '/home/peter/Programming/all/train_new'
	dest = '/home/peter/Programming/all/test_new'

	train_list = os.listdir(source)

	dog_count = 0
	cat_count = 0

	for index in range(len(train_list)):
		img_path = source + "/" + train_list[index]
		dest_path = dest + "/" + train_list[index]

		if ("cat" in img_path) or ("dog" in img_path):
			if ("cat" in img_path):
				if (cat_count < 125):
					os.rename(img_path, dest_path)
					cat_count = cat_count + 1
				else:
					continue

			if ("dog" in img_path):
				if (dog_count < 125):
					os.rename(img_path, dest_path)
					dog_count = dog_count + 1
				else:
					continue

		if (dog_count == 125) or (cat_count == 125):
			break

	print("done")

def check_move():
	source = '/home/peter/Programming/all/train_new'
	dest = '/home/peter/Programming/all/test_new'

	dest_list = os.listdir(dest)
	source_list = os.listdir(source)

	print(len(dest_list))
	print(len(source_list))

	dog = 0
	cat = 0

	for file_name in dest_list:
		if "cat" in file_name:
			cat = cat + 1

		if "dog" in file_name:
			dog = dog + 1

	print(cat)
	print(dog)

check_move()
