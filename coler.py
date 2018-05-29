# change 7 kind of color 

from PIL import Image

# Define variable
image = Image.open("image/bloom.jpg")
r, g, b = image.split()
change_image0 = Image.merge("RGB", (r, b, g)) #convert rgb_to_rbg
change_image1 = Image.merge("RGB", (g, b, r)) #convert rgb_to_gbr
change_image2 = Image.merge("RGB", (g, r, b)) #convert rgb_to_grb
change_image3 = Image.merge("RGB", (b, r, g)) #convert rgb_to_brg
change_image4 = Image.merge("RGB", (b, g, r)) #convert rgb_to_bgr
b_and_w = image.convert("1") #convert black and white color
gray = image.convert("L") #convert gray color

# output
image.show()
change_image0.show()
change_image1.show()
change_image2.show()
change_image3.show()
change_image4.show()
b_and_w.show()
gray.show()

#save image
change_image0.save("image/rgb_to_rbg.jpg")
change_image1.save("image/rgb_to_gbr.jpg")
change_image2.save("image/rgb_to_grb.jpg")
change_image3.save("image/rgb_to_brg.jpg")
change_image4.save("image/rgb_to_bgr.jpg")
b_and_w.save("image/b_and_w.jpg")
gray.save("image/gray.jpg")
