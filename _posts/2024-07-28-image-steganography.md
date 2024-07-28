---
layout: post
title: Image Steganography
excerpt: What is image steganography
---

<div style="text-align: justify" markdown="1">
<h3>Definitions</h3>

<h4>Steganography</h4>

- Hiding data within another data 

<h3>Demo</h3>
<h4>Greyscale & Greyscale</h4>

- Hiding greyscale inside greyscale
- Use the 4 MSB of the right image (barbara) into the 4 LSB of the left image (lenna) 

<div class="image-container">
{% picture images/steganography/lenna.png class="triple" %}
{% picture images/steganography/barbara.png class="triple" %}
</div>
<div class="center">Cover image (167.5KiB) and secret image (198.1 KiB)</div>
<br>

<div class="image-container">
{% picture images/steganography/mixed.png class="triple" %}
</div>
<div class="center">Steganographed image (128.0 KiB)</div>
<br>

<div class="image-container">
{% picture images/steganography/lenna_re.png class="triple" %}
{% picture images/steganography/barbara_re.png class="triple" %}
</div>
<div class="center">Recovered images (57.4 KiB and 77.7 KiB)</div>
<br>

<div class="center">Number of Bits Set in Original</div>

|   |   |   |
|---|---|---|
|         | 4 MSB    | 4 LSB    |
| Lenna   | 508627 | 524192 |
| Barbara | 501361 | 526439 |

- Slight artifact in the steganographed image
- Recovered image show slight degredation in quality
- Recovered images are much smaller than the original due to losing 4 bits of data per pixel
- Steganographed image much smaller than the original two inputs due to the fact that MSB bit data doesn't get set as much compared to the LSB

{% picture images/steganography/bits_set_graph.png %}

- Graph above shows that the 7th bit (64) gets set significantly less compared to the other bits. 
- The 7th bit gets set between the digits 64 - 127 and 192 - 255
- Makes sense why it gets set less since 192 - 255 range bracket is very bright and the images above are portraits in moderate lighting

<div class="centerbold">-----------------</div>

<h4>Greyscale & QR Code</h4>

- Hiding QR code inside greyscale
- Only requires 1 bit per pixel

<div class="image-container">
{% picture images/steganography/lenna.png class="triple" %}
{% picture images/steganography/qrcode.png class="triple" %}
</div>
<div class="center">Cover image (167.5KiB) and secret image (6.7 KiB)</div>
<br>

<div class="image-container">
{% picture images/steganography/mixed_qr.png class="triple" %}
</div>
<div class="center">Steganographed image (152.9 KiB)</div>
<br>

<div class="image-container">
{% picture images/steganography/lenna_re_7.png class="triple" %}
{% picture images/steganography/qrcode_re.png class="triple" %}
</div>
<div class="center">Recovered images (135.8 KiB and 4.0 KiB)</div>

- hardly any difference in the steganographed and recovered images
- only the LSB was modified, which can only change the value of the pixel by 1
- Reconstructed QR code smaller than the original due to the fact that the original is written in RGBA compared to the reconstructed written in greyscale + png compression 

<div class="centerbold">-----------------</div>

<h4>RGB & RGB</h4>

- Hiding RGB inside RGB
- Use the 4 MSB of the right image (barbara) into the 4 LSB of the left image (lenna)

<div class="image-container">
{% picture images/steganography/lenna_rgb.png class="triple" %}
{% picture images/steganography/barbara_rgb.png class="triple" %}
</div>
<div class="center">Cover image (521.1 KiB) and secret image (602.3 KiB)</div>
<br>

<div class="image-container">
{% picture images/steganography/mixed_rgb.png class="triple" %}
</div>
<div class="center">Steganographed image (400.8 KiB)</div>
<br>

<div class="image-container">
{% picture images/steganography/lenna_rgb_re.png class="triple" %}
{% picture images/steganography/barbara_rgb_re.png class="triple" %}
</div>
<div class="center">Recovered images (185.2 KiB and 238.3 KiB)</div>
<br>
<div class="image-container">
{% picture images/steganography/mixed_tl.png class="triple" %}
{% picture images/steganography/mixed_tl_rgb.png class="triple" %}
</div>
<div class="center">TL corner of the greyscale steganographed and RGB steganographed image</div>

- Both the greyscale and rgb steganographed image shows artifacts but it is clearer in the rgb image the mix from the secret image. If you look close enough you can spot the stacked books from the secret image
- A lot more data lost when extracted compared to the greyscale as there are now 3 channels to deal with per pixel 

<div class="centerbold">-----------------</div>

<h4>RGB & RGB randomised</h4>

- Hiding RGB inside RGB randomly
- Use the 4 MSB of the right image (barbara) into the 4 LSB of the left image (lenna)

<div class="image-container">
{% picture images/steganography/lenna_rgb.png class="triple" %}
{% picture images/steganography/barbara_rgb.png class="triple" %}
</div>
<div class="center">Cover image (521.1 KiB) and secret image (602.3 KiB)</div>
<br>

<div class="image-container">
{% picture images/steganography/mixed_rgb_rand.png class="triple" %}
</div>
<div class="center">Steganographed image (567.6 KiB)</div>
<br>

<div class="image-container">
{% picture images/steganography/lenna_rgb_rand_re.png class="triple" %}
{% picture images/steganography/barbara_rgb_rand_re.png class="triple" %}
</div>
<div class="center">Recovered images (185.2 KiB and 238.3 KiB)</div>
<br>
<div class="image-container">
{% picture images/steganography/mixed_tl_rgb.png class="triple" %}
{% picture images/steganography/mixed_tl_rgb_rand.png class="triple" %}
</div>
<div class="center">TL corner of the RGB steganographed and RGB random steganographed image</div>

- The steganographed image avoids traceable artifacts by randomising the secret image into the cover image
- The artifact books found in the rgb steganographed image is absent in the rgb randomised steganographed image  
- Image is randomised by setting the seed
- Need the seed number to extract the image
- Steganographed random image is noticeably larger than the normally steganographed image due to inefficient png compression due to the random nature of the 4 LSB secret data

<h3>Appendix</h3>

```python
# Basic example of greyscale steganography
import math
import cv2
import numpy as np

MSB_4 = 0b11110000
LSB_4 = 0b00001111
lenna   = cv2.imread("lenna.png",   cv2.IMREAD_GRAYSCALE)
barbara = cv2.imread("barbara.png", cv2.IMREAD_GRAYSCALE)

row, col = lenna.shape

mixed = np.zeros([row, col, 1])
# hide barbaras 4 MSB in lennas 4 LSB
for i in range(row):
    for j in range(col):
        mixed[i, j, 0] = (lenna[i,j] & MSB_4) | \
                         (barbara[i,j] >> 4)

# write the steganographed image 
cv2.imwrite("mixed.png", mixed)

lenna_re   = np.zeros([row, col, 1])
barbara_re = np.zeros([row, col, 1])

for i in range(row):
    for j in range(col):
        lenna_re[i,j,0]   =  int(mixed[i,j,0]) & MSB_4
        barbara_re[i,j,0] = (int(mixed[i,j,0]) & LSB_4) << 4

cv2.imwrite("lenna_re.png",   lenna_re)
cv2.imwrite("barbara_re.png", barbara_re)

```

```python
# Example of randomly hiding the secret image into
# the cover image
import math
import cv2
import numpy as np
import random

MSB_4 = 0b11110000
LSB_4 = 0b00001111
SEED = 10

lenna   = cv2.imread("lenna_rgb.png")
barbara = cv2.imread("barbara_rgb.png")

row, col, dep = lenna.shape

mixed = np.zeros([row, col, dep])

random.seed(SEED)
numbers = list(range(0, row*col))

# Mappings for the sercet image
index_pixel = random.sample(numbers, len(numbers))
pixel_index = {v: i for i, v in enumerate(index_pixel)}

b, g, r = cv2.split(barbara)
b = b.reshape(row*col)
g = g.reshape(row*col)
r = r.reshape(row*col)

index = 0
# hide barbaras 4 MSB in lennas 4 LSB
for i in range(row):
    for j in range(col):
        mixed[i, j, 0] = (lenna[i,j,0] & MSB_4) | \
                         (b[index_pixel[index]] >> 4)
        mixed[i, j, 1] = (lenna[i,j,1] & MSB_4) | \
                         (g[index_pixel[index]] >> 4)
        mixed[i, j, 2] = (lenna[i,j,2] & MSB_4) | \
                         (r[index_pixel[index]] >> 4)
        index += 1

# write the steganographed image 
cv2.imwrite("mixed_rgb_rand.png", mixed)

lenna_re = np.zeros([row, col, dep])
barb_re  = np.zeros([row, col, dep])

b, g, r = cv2.split(mixed)
b = b.reshape(row*col)
g = g.reshape(row*col)
r = r.reshape(row*col)

index = 0
for i in range(row):
    for j in range(col):
        lenna_re[i,j,0]   =  int(mixed[i,j,0]) & MSB_4
        lenna_re[i,j,1]   =  int(mixed[i,j,1]) & MSB_4
        lenna_re[i,j,2]   =  int(mixed[i,j,2]) & MSB_4
        barb_re[i,j,0] = (int(b[pixel_index[index]]) & LSB_4) \
                             << 4
        barb_re[i,j,1] = (int(g[pixel_index[index]]) & LSB_4) \
                             << 4
        barb_re[i,j,2] = (int(r[pixel_index[index]]) & LSB_4) \
                             << 4
        index += 1

cv2.imwrite("lenna_rgb_rand_re.png",   lenna_re)
cv2.imwrite("barbara_rgb_rand_re.png", barb_re)

```
</div>
