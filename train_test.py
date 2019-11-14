from imutils import paths
import os
current_dir = 'RenaultKwidImages'
print("[INFO] loading images...")
imagePaths = list(paths.list_images(current_dir))
print(imagePaths)
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')
percentage_test = 10

counter = 1  
index_test = round(100 / percentage_test)  


for image in imagePaths:
	path = os.path.dirname(image)+'/'+os.path.basename(image)
	file_train.write(path+'\n')
	if counter == index_test:
		counter = 1
		print(path)
		file_test.write(path + "\n")
	else:
		file_train.write(path + "\n")
		counter = counter + 1