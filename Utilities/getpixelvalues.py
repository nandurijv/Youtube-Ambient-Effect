from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from Utilities.writeoutput import write_to_file
def get_pixel_matrix(img_path, frame,n_frames):
    # Open image file
    img = Image.open(img_path+'.jpg', 'r')

    # Get image dimensions
    width, height = img.size

    # Iterate over each pixel and print its RGB value
    avg_lum = 0
    avg_r = 0
    avg_b = 0
    avg_g = 0
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            avg_lum += r*0.299+g*0.587+b*0.114
            avg_r += r
            avg_g += g
            avg_b += b
    print("Done for frame: " , img_path)
    print([{"luminance":avg_lum/(height*width)},{"rgb": [avg_r/(height*width),avg_g/(height*width),avg_b/(height*width)]}])

    #write to output css:
    write_to_file(f'{int((frame/n_frames)*100)}% {{ box-shadow:0px 0px {int(avg_lum/(height*width))}px {int(avg_lum/(height*width))}px rgb({avg_r/(height*width)},{avg_g/(height*width)},{avg_b/(height*width)})}}\n\t')
    return [{"luminance":avg_lum/(height*width)},{"rgb": [avg_r/(height*width),avg_g/(height*width),avg_b/(height*width)]}]