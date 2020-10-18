from PIL import Image


how_many_image = int(input("Enter a number between 1 and 5 : ")) # you can change the amount as you want

img_dir = " " # enter the image address here
file_list_img = [] 

for i in range(how_many_image):
    file_list_img.append(img_dir)
    img1 = Image.open(file_list_img[i])
    img1.show()
    print("image" + str(i))
