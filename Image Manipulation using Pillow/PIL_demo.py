from PIL import Image,ImageShow
import os
# displaying an image to the screen
image1=Image.open('pic.png')
image1.rotate(90).save('pic_rotated.png')
image1.convert(mode='L').save('pic_b&w.png')
# image1.show()
# ImageShow.show(image1)

# saving image with a different extension
# image1.save('pic.jpg')


# Converting all the jpgs into pngs
cwd=os.getcwd()
print(cwd)
# os.chdir('E:/corey-python/Image Manipulation using Pillow/jpgs/')
# for img in os.listdir():
# 	i=Image.open(img)
# 	fn,fext=os.path.splitext(img)
# 	i.save(f'E:/corey-python/Image Manipulation using Pillow/pngs/{fn}.png')
# os.chdir(cwd)


# Converting the size of all images to 300x300
# cwd=os.getcwd()
# os.chdir('E:/corey-python/Image Manipulation using Pillow/pngs/')
# size=(300,300)
# for img in os.listdir():
# 	i=Image.open(img)
# 	fn,fext=os.path.splitext(img)
# 	i.thumbnail(size)
# 	i.save(f"E:/corey-python/Image Manipulation using Pillow/300's/{fn}_300.{fext}")
# os.chdir(cwd)