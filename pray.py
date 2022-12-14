import numpy as np

box_width = int(np.ceil(1/scale_x))
box_height = int(np.ceil(1/scale_y))

image_array = np.array(image)

for y in range(new_height):
    for x in range(new_width):
        # Coordinates in old image
        x_ = int(np.floor(x/scale_x))
        y_ = int(np.floor(y/scale_y))
        
        # min() is used to assure that coordinates aren't out of bounds
        x_end = min(x_ + box_width, width-1)
        y_end = min(y_ + box_height, height-1)

        # We average the colors in the box
        pixel = image_array[y_:y_end,x_:x_end].mean(axis=(0,1))
        
        # We convert results to a tuple of ints
        pixel = np.round(pixel)
        pixel = tuple(pixel.astype(int))
        
        scaled_image.putpixel((x, y),  pixel)