'''
lab 18 image manipulation
'''

# # 01 - convert to greyscale and test pixelate (even number rows)
#
# from PIL import Image
# img = Image.open("lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()
#
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#
#         # pixelate greyscale
#         px = j // 64 + ( 8 * ( i // 64))
#         if i % 2 == 0:
#             if px % 2 == 0:
#                 determine y value, convert to int, set rgb to y value
#                 y = int(0.299 * r + 0.587 * g + 0.114 * b)
#                 (r, g, b) = (y, y, y)
#
#         else:
#             if px % 2 != 0:
#                 determine y value, convert to int, set rgb to y value
#                 y = int(0.299 * r + 0.587 * g + 0.114 * b)
#                 (r, g, b) = (y, y, y)
#
#         pixels[i, j] = (r, g, b)
#
# img.show()
#
# # # 02 - colorsys change hue/saturation/value
#
# import colorsys
#
# # colorsys uses colors in the range [0, 1]
#
# hdelta = float(input('Enter desired change for hue as float (1 is no change):'))
# sdelta = float(input('Enter desired change for saturation as float (1 is no change):'))
# vdelta = float(input('Enter desired change for value as a float (1 is no change):'))
#
# for i in range(width):
#     for j in range(height):
#         # receive rgb value for each pixel
#         r, g, b = pixels[i, j]
#         # convert rgb to hsv
#         h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
#
#         # alter hsv values according to user input
#         h *= hdelta
#         s *= sdelta
#         v *= vdelta
#
#         # convert back to rgb, show image
#         r, g, b = colorsys.hsv_to_rgb(h, s, v)
#         r = int(r * 255)
#         g = int(g * 255)
#         b = int(b * 255)
#         pixels[i, j] = (r, g, b)
# img.show()
#
#
# # turtles, pillows, and stick figures: oh my!
#

from PIL import Image, ImageDraw

# take input image, choose output scaling, output pixelated image
def pixelate_img ():
    # locate and read size of input file
    file = input('What is your file named?(no path needed if in the same folder):')
    img = Image.open(file)
    width, height = img.size
    pixels = img.load()

    # choose proper sizing for output file (build in border function to compensate for extra pixels at desired output size)
    print('New pixel sizes must be an equal divisor of the original(for now).')
    print('Original image width: ' + str(width))
    print('Original image height: ' + str(height))
    wf = width + 1
    while width % wf != 0:    # check for proper sizing, until fixer/border function added
        wf = int(input('How many pixels would you like for your final image width?:'))
        if width % wf != 0:
            print('Size incompatible, enter new size.')
    hf = height + 1
    while height % hf != 0:    # check for proper sizing until fixer/border function added
        hf = int(input('How many pixels would you like for your final image height?:'))
        if height % hf != 0:
            print('Size incompatible, enter new size.')


    # create list to store final pixel information
    px = []
    pxtot = wf * hf
    i = 0
    while i < pxtot:
        px.append([0, 0, 0])
        i += 1

    ppw = width // wf    # original width / final width pixels = original width pixels per final pixel
    pph = height // hf    # original height / final height pixels = original height pixels per final pixel
    ppp = ppw * pph    # original pixels contained in each final pixel

    # build indexed list of pixel info and average each final pixel
    for i in range(width):
        for j in range(height):
            loc = j // pph + hf * (i // ppw)  # index for storage in px list
            ro, go, bo = pixels[i, j]
            rs, gs, bs = px[loc]
            px[loc] = ro + rs, go + gs, bo + bs    # add current pixel data to total pixel
            if i % ppw == (ppw - 1) and j % pph == (pph - 1):    # check for final original pixel in new pixel, average pixel data if True
                rs, gs, bs = px[loc]
                px[loc] = rs // ppp, gs // ppp, bs // ppp

    # decide final pixel size, allow user to choose new size if picture size isn't desired
    finalize = ''
    while finalize != 'next':
        fpw = int(input('What would you like your final pixel width to be?'))
        fph = int(input('What would you like your final pixel height to be?:'))
        fwidth = wf * fpw
        fheight = hf * fph
        print('Final image size will be ' + str(fwidth) + ' x ' + str(fheight) + ' pixels.')
        finalize = input('If this size is good, enter "next", otherwise press enter and choose new pixel size.').lower()

    # create new image of proper size
    img = Image.new('RGB', (fwidth, fheight))
    draw = ImageDraw.Draw(img)

    # draw rectangles using px list: element values determine rgb color, index determines position (i = index)
    count = 0
    for i in px:
        color = i
        y = fph * (count % hf)
        x = fpw * (count // hf)
        draw.rectangle(((x, y), (x + fpw, y + fph)), fill=color)
        count += 1

    img.show()

pixelate_img()



# from PIL import Image, ImageDraw
#
# width = 500
# height = 500
#
# img = Image.new('RGB', (width, height))
#
# draw = ImageDraw.Draw(img)
#
#
# # the origin (0, 0) is at the top-left corner
#
# draw.rectangle(((0, 0), (width, height)), fill="white")
#
# # draw a rectangle from x0, y0 to x1, y1
# draw.rectangle(((100, 100), (300, 300)), fill="lightblue")
#
# # draw a line from x0, y0, x1, y1
# # using the color pink
# color = (256, 128, 128)  # pink
# draw.line((0, 0, width, height), fill=color)
# draw.line((0, height, width, 0), fill=color)
#
#
# circle_x = width/2
# circle_y = height/2
# circle_radius = 100
# draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')
#
# img.show()