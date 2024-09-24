---
layout: post
title: Camera Calibration Matrix
excerpt: What is Camera Calibration Matrix
---

<div style="text-align: justify" markdown="1">
<h3>Definitions</h3>

<h4>Camera Calibration</h4>

- Process of determining the parameters of a lens+camera that allows you to accurately compute measurements and positions. 
-  Useful for
    - measuring a size of an object from an image in the world unit
    - Determining the location of the camera in the scene
    - Stiching images together
    - Un/distort an image

<h4>Extrinsic Matrix</h4>

- Represents the position and orientation of the camera in respect to the coordinate system it's in
- Includes rotation and translation values

$$ [R | T] = \begin{bmatrix} R_{00} & R_{01} & R_{02} & T_x \\ R_{10} & R_{11} & R_{12} & T_y \\ R_{20} & R_{21} & R_{22} & T_z \end{bmatrix} $$

- $$ R $$ - 3x3 rotation matrix

$$ R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos(\theta) & -\sin(\theta) \\ 0 & \sin(\theta) & \cos(\theta) \end{bmatrix} $$

$$ R_y(\theta) = \begin{bmatrix} \cos(\theta) & 0 & \sin(\theta) \\ 0 & 1 & 0 \\ -\sin(\theta) & 0 & \cos(\theta) \end{bmatrix} $$

$$ R_z(\theta) = \begin{bmatrix} \cos(\theta) & -\sin(\theta) & 0 \\ \sin(\theta) & \cos(\theta) & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

$$ R = R_z(\lambda) R_y(\beta) R_x(\alpha) $$

- Rotation matrix multiplication order matters

- $$ T $$ - 3x1 position of the camera

<h4>Intrinsic Matrix</h4>

- Represents the internal parameters of the camera
- Includes focal length, principal point and skew coefficient

$$ K = \begin{bmatrix} f_x & s & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{bmatrix} $$

$$ f_x = \dfrac{F}{p_x} $$

$$ f_y = \dfrac{F}{p_y} $$

- Focal length ($$ f_x, f_y $$) - Scale of the image measured in pixels.
    - $$ F $$ - focal length of lens in mm
    - $$ p_x, p_y $$ - size of pixel in world units

- Principal point ($$ c_x, c_y $$) - location on the camera's image in pixels where the lens's optical axis (the line going straight through the center of the lens) would hit the image sensor

- Skew coefficient ($$ s $$) - measure of how much the image axes (x and y) are not perfectly perpendicular to each other.

<h4>Radial Distortion</h4>

- Distortion that occurs from light bending near the edges of a lens which make straight lines appear warped

$$ x_{distorted} = x(1 + k_1 r^2 + k_2 r^4 + k_3 r^6 ...) $$

$$ y_{distorted} = y(1 + k_1 r^2 + k_2 r^4 + k_3 r^6 ...) $$

$$ r^2 = x^2 + y^2 $$

- $$ x,y $$ - undistored pixel location in the normalized image coordinate space. 
- $$ k_1, k_2, k_3 $$ - radial distortion coefficients of the lens



<h4>Tangential Distortion</h4>

- Distortion that occurs when the lens and imgage sensor are not parallel

$$ x_{distorted} = x + [2p_1xy + p_2(r^2+2x^2)] $$

$$ y_{distorted} = y + [p_1(r^2+2y^2) + 2p_2xy] $$

$$ r^2 = x^2 + y^2 $$

- $$ x,y $$ - undistored pixel location in the normalized image coordinate space.
- $$ p_1, p_2 $$ - tangential distortion coefficients of the lens

<h3>Example</h3>

<h4>Radial Positive</h4>

<div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/rad_0.05_0.0.png %}
<figcaption>$$ k_1 = 0.05, k_2 = 0.0 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_0.15_0.0.png %}
<figcaption>$$ k_1 = 0.15, k_2 = 0.0 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_0.2_0.0.png %}
<figcaption>$$ k_1 = 0.2, k_2 = 0.0 $$</figcaption>
</figure>
</div>

<div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/rad_0.0_0.05.png %}
<figcaption>$$ k_1 = 0.0, k_2 = 0.05 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_0.0_0.15.png %}
<figcaption>$$ k_1 = 0.0, k_2 = 0.15 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_0.0_0.2.png %}
<figcaption>$$ k_1 = 0.0, k_2 = 0.2 $$</figcaption>
</figure>
</div>

<!-- <div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/rad_0.05_0.05.png %}
<figcaption>$$ k_1 = 0.05, k_2 = 0.05 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_0.15_0.15.png %}
<figcaption>$$ k_1 = 0.15, k_2 = 0.15 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_0.2_0.2.png %}
<figcaption>$$ k_1 = 0.2, k_2 = 0.2 $$</figcaption>
</figure>
</div> -->

<h4>Radial Negative</h4>

<div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/rad_-0.01_0.0.png %}
<figcaption>$$ k_1 = -0.01, k_2 = 0.0 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_-0.02_0.0.png %}
<figcaption>$$ k_1 = -0.02, k_2 = 0.0 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_-0.04_0.0.png %}
<figcaption>$$ k_1 = -0.04, k_2 = 0.0 $$</figcaption>
</figure>
</div>

<div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/rad_0.0_-0.01.png %}
<figcaption>$$ k_1 = 0.0, k_2 = -0.01 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_0.0_-0.02.png %}
<figcaption>$$ k_1 = 0.0, k_2 = -0.02 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_0.0_-0.04.png %}
<figcaption>$$ k_1 = 0.0, k_2 = -0.04 $$</figcaption>
</figure>
</div>

<!-- <div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/rad_-0.01_-0.01.png %}
<figcaption>$$ k_1 = -0.01, k_2 = -0.01 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_-0.02_-0.02.png %}
<figcaption>$$ k_1 = -0.02, k_2 = -0.02 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/rad_-0.04_-0.04.png %}
<figcaption>$$ k_1 = -0.04, k_2 = -0.04 $$</figcaption>
</figure>
</div> -->

<h4>Tangential Positive</h4>

<div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/tan_0.02_0.0.png %}
<figcaption>$$ k_1 = 0.02, k_2 = 0.0 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_0.04_0.0.png %}
<figcaption>$$ k_1 = 0.04, k_2 = 0.0 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_0.08_0.0.png %}
<figcaption>$$ k_1 = 0.08, k_2 = 0.0 $$</figcaption>
</figure>
</div>

<div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/tan_0.0_0.02.png %}
<figcaption>$$ k_1 = 0.0, k_2 = 0.02 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_0.0_0.04.png %}
<figcaption>$$ k_1 = 0.0, k_2 = 0.04 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_0.0_0.08.png %}
<figcaption>$$ k_1 = 0.0, k_2 = 0.08 $$</figcaption>
</figure>
</div>

<!-- <div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/tan_0.02_0.02.png %}
<figcaption>$$ k_1 = 0.02, k_2 = 0.02 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_0.04_0.04.png %}
<figcaption>$$ k_1 = 0.04, k_2 = 0.04 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_0.08_0.08.png %}
<figcaption>$$ k_1 = 0.08, k_2 = 0.08 $$</figcaption>
</figure>
</div> -->

<h4>Tangential Negative</h4>

<div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/tan_-0.02_0.0.png %}
<figcaption>$$ k_1 = -0.02, k_2 = 0.0 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_-0.04_0.0.png %}
<figcaption>$$ k_1 = -0.04, k_2 = 0.0 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_-0.08_0.0.png %}
<figcaption>$$ k_1 = -0.08, k_2 = 0.0 $$</figcaption>
</figure>
</div>

<div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/tan_0.0_-0.02.png %}
<figcaption>$$ k_1 = 0.0, k_2 = -0.02 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_0.0_-0.04.png %}
<figcaption>$$ k_1 = 0.0, k_2 = -0.04 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_0.0_-0.08.png %}
<figcaption>$$ k_1 = 0.0, k_2 = -0.08 $$</figcaption>
</figure>
</div>

<!-- <div class="image-container">
<figure class="triple">
{% picture images/camera_calibration/tan_-0.02_-0.02.png %}
<figcaption>$$ k_1 = -0.02, k_2 = -0.02 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_-0.04_-0.04.png %}
<figcaption>$$ k_1 = -0.04, k_2 = -0.04 $$</figcaption>
</figure>
<figure class="triple">
{% picture images/camera_calibration/tan_-0.08_-0.08.png %}
<figcaption>$$ k_1 = -0.08, k_2 = -0.08 $$</figcaption>
</figure>
</div> -->


<h4>Calculating Parameters</h4>

<!-- $$ x_{distorted} = x (1 + k_1 r^2 + k_2 r^4 + k_3 r^6) + [2p_1xy + p_2(r^2+2x^2)] $$

$$ y_{distorted} = y (1 + k_1 r^2 + k_2 r^4 + k_3 r^6) + [p_1(r^2+2y^2) + 2p_2xy] $$

- Combining the two distortion model formula -->
- Using OpenCV you can calculate the intrinsic + extrinsic matrix and the distortion coefficients
- [for more information](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
- tldr
    - Use 10 images or so with some known points in 3D space (object points) and corresponding 2D space (image points)
    - Feed images into cv.calibrateCamera

```python
import numpy as np
import cv2 as cv
import glob

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 
            30,
            0.001)
 
# prepare object points, like (0,0,0), (1,0,0), ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
 
# Arrays to store object points and image points 
# from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
 
images = glob.glob('*.jpg')
 
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
 
    # If found, add object points, image points (
    # after refining them)
    if ret == True:
        objpoints.append(objp)
 
        corners2 = cv.cornerSubPix(gray,corners, 
                                   (11,11), 
                                   (-1,-1), 
                                   criteria)
        imgpoints.append(corners2)

# calculate the camera/intrinsic matrix, 
# distortion coefficients, 
# rotation and translation vectors
result = cv.calibrateCamera(objpoints, 
                            imgpoints, 
                            gray.shape[::-1], 
                            None, 
                            None)
ret, int_mtx, dist, rvecs, tvecs = result

```

<h5>Intrinsic Matrix</h5>

$$ \begin{bmatrix} 534.07088364 & 0 & 341.53407554 \\ 0 & 534.11914595 & 232.94565259 \\ 0 & 0 & 1 \end{bmatrix} $$

<h5>Radial Distortion Coefficients</h5>

$$ k_1 = -2.92971637e^{-1} $$

$$ k_2 = 1.07706962e^{-1} $$

$$ k_3 = 4.34798110e^{-2} $$

<h5>Tangential Distortion Coefficients</h5>

$$ p_1 = 1.31038376e^{-3} $$

$$ p_2 = -3.11018780e^{-5} $$

```python
img = cv.imread('left12.jpg')

# undistort
dst = cv.undistort(img, mtx, dist)
 
# save the image
cv.imwrite('calibresult.png', dst)

```

<div class="image-container">
<figure class="double">
{% picture images/camera_calibration/left12.jpg %}<figcaption>Original</figcaption>
</figure>
<figure class="double">
{% picture images/camera_calibration/calibresult.png %}
<figcaption>Undistorted</figcaption>
</figure>
</div>

<h3>FAQ</h3>

<h4>Why isn't the principal point always 0,0?</h4>
- In an ideal world with no manufacturing issues or lens alignment issues the principal point could be 0,0. But we do not live in an ideal world. 
- Small imperfections and tolerances are everywhere and even the slightest shift can result in a non 0,0 principal point.

<h4>Why isn't the skewer coefficient always 0,0?</h4>
- Same reason as the principal point.

<h3>Appendix</h3>

```python
# Distort an image based on the distortion coeffs
import numpy as np

def distort_point(x, y, width, height, r_coeffs, t_coeffs):
    k1, k2 = r_coeffs[:2]
    p1, p2 = t_coeffs[:2]
    
    x_c = width/2
    y_c = height/2

    x = (x - x_c) / x_c
    y = (y - y_c) / y_c

    # Radial distortion
    r2 = x**2 + y**2
    rad_dist = 1 + k1 * r2 + k2 * r2**2
    
    # Tangential distortion
    tang_dist_x = 2 * p1 * x * y + p2 * (r2 + 2 * x**2)
    tang_dist_y = (p1 * (r2 + 2 * y**2) + 2 * p2 * x * y)

    x_distorted = x * rad_dist + tang_dist_x
    y_distorted = y * rad_dist + tang_dist_y
    
    x_distorted = x_distorted * x_c + x_c
    y_distorted = y_distorted * y_c + y_c

    return x_distorted, y_distorted

def distort_image(image, r_coeffs, t_coeffs):
    """ Distort an entire image. """
    h, w = image.shape[:2]
    d_image = np.full_like(image, 255)

    for y in range(h):
        for x in range(w):
            x_d, y_d = distort_point(x, y, 
                        w, h, r_coeffs, t_coeffs)
            if 0 <= int(x_d) < w and 0 <= int(y_d) < h:
                d_image[y, x] = image[int(y_d), int(x_d)]

    return d_image


```

</div>
