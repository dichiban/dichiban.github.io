import math

# { 0: 0.0,
#   1: 0.0012,
#     ...
#   254: 252.805
#   255: 255.0 }
def make_gamma_lut(min=0, max=255, steps=1, gamma=2.2):
    gamma_lut = {}
    for x in range(min, max+1, steps):
        gamma_lut[x] = 255 * math.pow(x/max, gamma)
    return gamma_lut
