
from imutils import paths
current_dir = 'RenaultKwidImages'
print("[INFO] loading images...")
imagePaths = list(paths.list_images(current_dir))
print(imagePaths)

# Percentage of images to be used for the test set
percentage_test = 10;
# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for imagepath in imagePaths:
	print("hello")

	if counter == index_test:
		counter = 1
		file_test.write(imagepath +"\n")
	else:
		file_train.write(imagepath +"\n")
		counter = counter + 1
