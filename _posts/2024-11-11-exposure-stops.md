---
layout: post
title: Exposure Stops
excerpt: What are Exposure Stops
---

<div style="text-align: justify" markdown="1">
<h3>Definitions</h3>

<h4>Exposure Stops</h4>
A unit of measurement that represents the doubling or halving of the amount of light exposed to the camera sensor/film.

Stops can be controlled by the following 3 controls.

<h5>Aperture</h5>
The following defines the ratio at which light enters the lens

$$ N = \dfrac{f}{D}$$

Where $$ f $$ is the focal length and $$ D $$ is the diameter of the opening.

To double the light exposure from the aperture we need to double the size of the lens opening.

The lens opening can be calculated by using the area of circle formula.

$$ A = \pi r^2 $$

$$ A = \pi\bigg(\dfrac{D}{2}\bigg)^2 $$

$$ A = \dfrac{\pi D^2}{4} $$

$$ A $$ - Area

$$ r $$ - Radius

$$ D $$ - Diameter

Now let's double the area $$ A $$ and find the new diameter

$$ A^\prime = 2A $$

$$ A^\prime = \dfrac{\pi (D^\prime)^2}{4} $$

$$ A^\prime $$ - Double the area ($$ A $$)

$$ D^\prime $$ - New diameter in respect to A doubling

Therefore to find $$ D^\prime $$

$$ \dfrac{\pi (D^\prime)^2}{4} = 2\dfrac{\pi D^2}{4} $$

$$ (D^\prime)^2 = 2 D^2 $$

$$ D^\prime = D\sqrt{2} $$

Therefore the Diameter must be multiplied by $$ \sqrt{2} $$ to double the light intake.

| Diameter multiplier | Approximate Diameter | F stop |
| :-----------------: | :------------------: | :----: |
|  $$ \sqrt{2}^0 $$   |          1           | f/1.0  |
|  $$ \sqrt{2}^1 $$   |     1.414213562      | f/1.4  |
|  $$ \sqrt{2}^2 $$   |          2           | f/2.0  |
|  $$ \sqrt{2}^3 $$   |     2.828427125      | f/2.8  |
|  $$ \sqrt{2}^4 $$   |          4           | f/4.0  |
|  $$ \sqrt{2}^5 $$   |     5.656854249      | f/5.6  |
|  $$ \sqrt{2}^6 $$   |          8           | f/8.0  |

A lot of modern camera + lens also support going up in thirds.

| Diameter multiplier  | Approximate Diameter | F stop |
| :------------------: | :------------------: | :----: |
|   $$ \sqrt{2}^1 $$   |     1.414213562      | f/1.4  |
| $$ \sqrt{2}^{4/3} $$ |     1.587401052      | f/1.6  |
| $$ \sqrt{2}^{5/3} $$ |     1.781797436      | f/1.8  |
|   $$ \sqrt{2}^2 $$   |          2           | f/2.0  |

<h5>Shutter Speed</h5>

To double the exposure using shutter speed, double the amount of time the shutters are open for.

| ------------------ | ------------------ | ------------------ | ------------------- | ------------------- | ------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| **Shutter Speed** | $$ 1 $$ | $$ \dfrac{1}{2} $$ | $$ \dfrac{1}{4} $$ | $$ \dfrac{1}{8} $$ | $$ \dfrac{1}{15} $$ | $$ \dfrac{1}{30} $$ | $$ \dfrac{1}{60} $$ | $$ \dfrac{1}{125} $$ | $$ \dfrac{1}{250} $$ |

One thing to note is that it's not exactly double. This is due to historic reasons of wanting to simplify the usage and to accomodate mechanical limitations.

<h5>ISO</h5>

To double or halve the exposure using ISO the film or sensor needs to be double or half as sensitive to light.

| ---- | ---- | ---- | ---- | ---- |---- |
| **ISO Arithmetic** | 100 | 200 | 400 | 800 | 1600 |
| **ISO Logarithmic** | 21$^\circ$ | 24$^\circ$ | 27$^\circ$ | 30$^\circ$ | 33$^\circ$ |

ISO Arithmetic is based on ASA standards and the ISO Logarithmic is based on the DIN standards.

One interesting thing to note about the DIN system is that it's very easy to work out the $$ \dfrac{1}{3} $$ stops as they are just 1$^\circ$.

To convert ASA to DIN

$$ DIN = 10 \times \log_{10} ISO + 1 $$

<h3>Conclusion</h3>

The exposure to a scene with a constant light source can be maintained by balancing the stops made to the aperture, shutter speed, and ISO so that their cumulative effect results in a net zero change.

</div>
