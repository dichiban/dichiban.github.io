---
layout: post
title: Binary Operations
excerpt: Binary operation examples
---

<div style="text-align: justify" markdown="1">
<h3>Types</h3>

<h4>AND</h4>

```c++
#include <iostream>
#include <cstdint>

void bitwiseAnd() {
    uint8_t a = 10;    // 00001010
    uint8_t b = 6;     // 00000110
    uint8_t c = a & b; // 00000010 (2)
    std::cout << static_cast<int>(c) << std::endl;    
}
```

<h4>OR</h4>

```c++
void bitwiseOr() {
    uint8_t a = 10;    // 00001010
    uint8_t b = 6;     // 00000110
    uint8_t c = a | b; // 00001110 (14)
    std::cout << static_cast<int>(c) << std::endl;    
}
```

<h4>XOR</h4>

```c++
void bitwiseXOr() {
    uint8_t a = 10;    // 00001010
    uint8_t b = 6;     // 00000110
    uint8_t c = a ^ b; // 00001100 (12)
    std::cout << static_cast<int>(c) << std::endl;    
}
```

<h4>NOT</h4>

```c++
void bitwiseNot() {
    uint8_t a = 10;    // 00001010
    uint8_t b = ~a;    // 11110101 (245)
    std::cout << static_cast<int>(b) << std::endl;    
}
```

<h4>LEFT SHIFT</h4>

```c++
void bitwiseLeftShift() {
    uint8_t a = 10;    // 00001010
    uint8_t b = a << 2;// 00101000(40)
    std::cout << static_cast<int>(b) << std::endl;    
}
```

<h4>RIGHT SHIFT</h4>

```c++
void bitwiseRightShift() {
    uint8_t a = 10;    // 00001010
    uint8_t b = a >> 2;// 00000010 (2)
    std::cout << static_cast<int>(b) << std::endl;    
}
```

<h3>Applications</h3>

<h4>Parity Check</h4>

- A method that adds an extra bit to the least significant bit (LSB) that tells you if there's an even (or odd) amount of bits set.
- Depending on the system it will keep track if even or odd amount of bits were set.
- Used to check if the data recieved is not corrupt
- Limitation: only detects an odd number of errors in the number of bits set

```c++

bool parityCheck(uint8_t data) {
    bool parity = false;
    // Checks if each bit is set or not
    for (size_t i = 0b00000000; i < 8; i++) { 
        // ( data & ( left Shift 00000001 every loop by 1 ))
        // eg 
        // (00000101 & 00000100)
        // = 00000100 (3rd bit was set, return true) 
        if (data & (1 << i)) {
            parity = !parity;
        }
    }
    return parity;
}

void check() {
    // Correct data
    uint8_t correctData1 = 0b01101011;
    uint8_t correctData2 = 0b01001010;
    // Corrupt data where the parity bit doesn't match
    // the number of bits set
    uint8_t corruptData1 = 0b00101011;
    uint8_t corruptData2 = 0b00001010;

    std::cout << parityCheck(correctData1) << std::endl; // T
    std::cout << parityCheck(correctData2) << std::endl; // T
    std::cout << parityCheck(corruptData1) << std::endl; // F
    std::cout << parityCheck(corruptData2) << std::endl; // F
}
```

<h4>Boolean Algebra</h4>
- Useful to simplify expressions

<h5>AND</h5>

```
x & y = y & x
x & (y & z) = (x & y) & z
x & 0b11111111 = x
x & 0 = 0
x & x = x
```

<h5>OR</h5>

```
x | y = y | x
x | (y | z) = (x | y) | z
x | 0 = x
x | 0b11111111 = 0b11111111
x | x = x
```

<h5>XOR</h5>

```
x ^ y = y ^ x
x ^ (y ^ z) = (x ^ y) ^ z
x ^ 0 = x
x ^ y ^ y = x
x ^ x = 0
x ^ 0b11111111 = ~x
```

<h5>NOT</h5>

```
~(~x) = x
```

<h5>Mix</h5>

```
x | (x & y) = x
x & (x | y) = x
~(x | y) = ~x & ~y
~(x & y) = ~x | ~y
x | (y & z) = (x | y) & (x | z)
x & (y | z) = (x & y) | (x & z)
x & (y ^ z) = (x & y) ^ (x & z)
x + y = (x ^ y) + ((x & y) << 1)
x - y = ~(~x + y)
```

<h4>Cryptography</h4>

<h5>Circular shift</h5>

- Shifts and wraps bits around by n 
- Useful to encrypt and decrypt data by knowing how many shifts are needed

```
0100
circular left shift by 2
0001

0001
circular right shift by 3
0010
```

- Below code is useful to visualise how the shift works
- There are more efficient ways to do this without looping

```c++
uint8_t circularLeftShift(uint8_t data, size_t shift) { 
    for (size_t i = 0; i < shift; i++)
    {
        // see if any bits will overflow
        uint8_t left_over = data & 0b10000000;
        // left shift by 1
        data = data << 1;

        // if there were any overflows set them to the LSB
        if (left_over)
        {
            data = data | 0b00000001;
        }
    }
    return data;
}

uint8_t circularRightShift(uint8_t data, size_t shift) { 
    for (size_t i = 0; i < shift; i++)
    {
        // see if any bits will overflow
        uint8_t left_over = data & 0b00000001;
        // right shift by 1
        data = data >> 1;

        // if there were any overflows set them to the MSB
        if (left_over)
        {
            data = data | 0b10000000;
        }
    }
    return data;
}

void runEncryption() {
    uint8_t data = 0b10001001;
    size_t shift = 5;
    uint8_t encrypted = circularLeftShift(data, shift);
    uint8_t decrypted = circularRightShift(encrypted, shift);
    // 0b10001001 = 137
    std::cout << static_cast<int>(data)      << std::endl;
    // 0b00110001 = 49
    std::cout << static_cast<int>(encrypted) << std::endl;
    // 0b10001001 = 137
    std::cout << static_cast<int>(decrypted) << std::endl;
}

```

<h5>Steganography</h5>

- Hiding data within another non-secret data.
- Hiding a message in a image
- Good for hiding data discreetly

{% picture jpt-webp images/binary_operations/red_255.ppm %}

- Above picture represents a red 500 x 100 red image where every pixel is 255 0 0 (11111111 00000000 0000000)

{% picture jpt-webp images/binary_operations/red_255.ppm %}

- Above picture represents a red 500 x 100 red image where every pixel is between 248 0 0 (11111000 0000000 0000000) and 255 0 0 

- The 3 LSB in the image above can be used to add data to the image without affecting how the image looks to the human eye

<h3>FAQ</h3>

<h4>Why is there even and odd parity?</h4>

- Essentially because legacy and standards not being made back in the day.

<h3>Appendix</h3>

```python
# How to generate red 255 and red 248 images
import math
import random

MAGIC_NUMBER = "P3\n"
COMMENT = "# This is a rgb ppm\n"

MAX_VAL = 255
MAX_VAL_STR = f"{MAX_VAL}\n"

def write_color(filename, r_value):    
    image_x = 500
    image_y = 100
    dimension = f"{image_x} {image_y}\n"

    with open(filename, "w") as f:
        f.write(MAGIC_NUMBER)
        f.write(COMMENT)
        f.write(dimension)
        f.write(MAX_VAL_STR)
        for y in range(image_y):
            for x in range(image_x):
                f.write(f"{random.randint(r_value, 255)} 0 0 ")
            f.write("\n")

# 0b11111111 = 255
write_color("red_255.ppm", 255)
# 0b11111000 = 248
write_color("red_248.ppm", 248)
```
</div>
