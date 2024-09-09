from PIL import Image
im_file = 'screenshot_marked.png'
im = Image.open(im_file)

print(im)
im.show()
im.save("test.png")