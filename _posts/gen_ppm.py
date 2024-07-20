import math

MAGIC_NUMBER = "P2\n"
COMMENT = "# This is a greyscale ppm\n"

MAX_VAL = 255
MAX_VAL_STR = f"{MAX_VAL}\n"

def write_color(filename, exponent, bucket=11):    
    image_x = bucket*100
    image_y = 100
    x_per_bucket = int(image_x/bucket)
    dimension = f"{image_x} {image_y}\n"

    with open(filename, "w") as f:
        f.write(MAGIC_NUMBER)
        f.write(COMMENT)
        f.write(dimension)
        f.write(MAX_VAL_STR)
        for y in range(image_y):
            for x in range(bucket):
                for xi in range(x_per_bucket):
                    f.write("%d "%(round(
                        math.pow(x/(bucket-1), exponent)*MAX_VAL
                    )))
            f.write("\n")

write_color("greyscale_linear.ppm", 1)
write_color("greyscale_gamma_encoded.ppm", 1/2.2)
write_color("greyscale_gamma_decoded.ppm", 2.2)