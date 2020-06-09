# Image processing using Pillow library

from PIL import Image, ImageFilter

# open image in to pillow object
img = Image.open('./images/squirtle.jpg')

print(img.size) # size of the image (x, y) in pixels
print(img.format) # image format (PNG, JPEG)

# Filter image
# Smooth
smoothImage = img.filter(ImageFilter.SMOOTH)
smoothImage.save('./images/squirtle_smooth.png', 'png')

# greyscale
greyScaleImage = img.convert('L')
greyScaleImage.save('./images/squirtle_greyscale.png', 'png')
# show image
greyScaleImage.show()

# rotate
rotatedImage = img.rotate(180)
rotatedImage.save('./images/squirtle_rotated.png', 'png')

# resize
resizedImage = img.resize((309, 320))
resizedImage.save('./images/squirtle_resized.png', 'png')

# crop
boxToResize = (100, 100, 400, 400)
croppedImage = img.crop(boxToResize)
croppedImage.save('./images/squirtle_cropped.png', 'png')

# create thumbnail maintaining the aspect ratio of the original image
img.thumbnail((400, 400)) # (x, y) max sizes for thumbnail
img.save('./images/squirtle_thumbnail.png', 'png')
print(img.size) # (386, 400)
# by this method it maintains the aspect ration and doesn't resize the image exactly with given size parameters
