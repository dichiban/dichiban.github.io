---
layout: post
title: Dynamic Memory
excerpt: What is dynamic memory
---

<div style="text-align: justify" markdown="1">
<h3>Definitions</h3>

<h4>Dynamic Memory</h4>

- Size is unkown and allocated at run time
- Uses the heap
- Can be assigned using **new** operator or using containers like **std::vector** in C++

<h4>Static Memory</h4>

- Size is known and allocated at compile time
- Uses the stack

<h4>Pointer</h4>

- Variable that stores memory addresses to another variable / data structures

```c++
void pointer() {
    int a  = 10;
    // asterisk to define b as a pointer
    // ampersand to retrieve the memory address of a variable
    int *b = &a;
    std::cout << b << std::endl;
    // outputs the memory address to the int
    // e.g 0x7ffe97a64604
}
```
<h4>Reference</h4>

- An alias for another variable

```c++
void reference() {
    int a = 10;
    // NOT TO BE CONFUSED WITH MEMORY ADDRESS OPERATOR
    // when ampersand used in variable declaration 
    // it is a reference
    int &b = a;

    // outputs 10
    std::cout << b << std::endl;

    b = 5;
    // outputs 5
    std::cout << a << std::endl;
}
```

<h4>Dereference</h4>

- Get the value from the pointer

```c++
void dereference() {
    int  a = 10;
    int *b = &a;

    // NOT TO BE CONFUSED WITH POINTER DECLARATION
    // asterisk denotes the dereference operation 
    // when used in the expression 
    int c = *b;
    // outputs 10
    std::cout << c << std::endl;
}
```

<h4>Stack</h4>

- Fast memory but limited size
- Memory managed automatically
- LIFO structure
- Good for managing temporary data with limited scope/life
- located on the RAM

<h4>Heap</h4>

- Large but slower memory
- Manual memory management (often obstructed from you)
- Garbage collectors can make this an automatic process
- Good for managing persistant data that goes beyond it's scope
- located on the RAM

<h4>Allocate/Deallocate Memory</h4>

- Reserving a block of heap memory 
- Releasing memory that was allocated
- Efficient memory management compared to garbage collectors

```c++
void heapMemoryManagement() {
    // new keyword used to allocate to heap
    // returns the memory location of the
    // dynamically allocated block
    int *a = new int;
    *a = 5;
    // output 5
    std::cout << *a << std::endl;
    // delete keyworse used to deallocate memory
    // must do in C++ otherwise it is a
    // memory leak
    delete a;
}
```

<h4>Smart Pointers</h4>

- Pointers that have managementment built in

    <h5>Unique Pointers</h5>
    
    - Smart pointer that ensures that the ownership of a dynamically allocated object is unique

    ```c++
    void uniquePtr() {
        std::unique_ptr<int> a(new int(5));
        // cannot 
        // std::unique_ptr<int> b = a;

        std::cout << *a << std::endl;
        // no need to delete as it'll automatically
        // get deleted after it goes out of scope
    }
    ```

    <h5>Shared Pointers</h5>

    - Smart pointer that allows multiple ownership of a dynamically allocated object

    ```c++
    void sharedPtr() {
        std::shared_ptr<int> a(new int(5));
        std::shared_ptr<int> b = a;

        // Both a and b point to the same address
        // outputs 5
        std::cout << a << std::endl;
        std::cout << b << std::endl;
        // outputs 2
        std::cout << a.use_count() << std::endl;
    }
    ```

<h3>Demo</h3>

<h4>Speed</h4>

- Speed-wise you will technically get faster memory allocation when
    1. Static memory
    2. Dynamic memory managed by yourself
    3. Dynamic memory managed by the container
- Negligable unless working in HPC environment 

```c++
void benchmarkMemoryAllocationTimes() {
    size_t size = 100000;
    using namespace std::chrono;
    
    duration<double> elapsed;
    using namespace std::chrono;
    time_point<high_resolution_clock> start;
// Static C Style Arrays
// 0.00115266 seconds
// ----------

    uint8_t a[size];
    start = high_resolution_clock::now();
    for (size_t i = 0; i < size; i++) {
        a[i] = static_cast<uint8_t>(i % 256);
    }
    elapsed = high_resolution_clock::now() - start;

    std::cout << elapsed.count() << std::endl;

// Dynamic C Style Arrays
// 0.00157149 seconds
// ----------

    uint8_t* b = new uint8_t[size];
    start = high_resolution_clock::now();
    for (size_t i = 0; i < size; i++) {
        b[i] = static_cast<uint8_t>(i % 256);
    }
    elapsed = high_resolution_clock::now() - start;

    std::cout << elapsed.count() << std::endl;

    delete[] b;

// Standary Library Vector
// 0.00227632 seconds
// ----------

    std::vector<uint8_t> v(size);
    start = high_resolution_clock::now();
    for (size_t i = 0; i < size; i++) {
        v[i] = static_cast<uint8_t>(i % 256);
    }
    elapsed = high_resolution_clock::now() - start;

    std::cout << elapsed.count() << std::endl;
}

```

<h4>Size</h4>

- If you have some data that can get large or is unknown till run time it is prefered to use dynamic memory to allocate some memory in the heap
- Below is an example of an image class with an arbitary width and heigh dimension that can contain a lot of data

```c++
class Image {
public:

    Image(size_t width, size_t height, uint8_t def = 0) {
        m_width  = width;
        m_height = height;
        // Dynamic memory
        m_data = new uint8_t[width * height];
        
        for (size_t i = 0; i < width * height; i++)
        {
            m_data[i] = def;
        }
    }

    ~Image() {
        // Only deallocate in the destrctor to ensure
        // no double deletion which leads to undefined
        // behaviour in C++
        delete[] m_data;
    }

    uint8_t getPixel(size_t x, size_t y) {
        return m_data[m_width*x + y];
    }

    void setPixel(size_t x, size_t y, uint8_t value) {
        m_data[m_width*x + y] = value;
    }

private:
    
    uint8_t* m_data;
    size_t m_width;
    size_t m_height;
};

```

<h4>Memory Pool</h4>

- Allocates a block of dynamic memory once
- Resolves the issue of memory fragmentation
- Removes the small overhead of constantly allocating dynamic memory 
- Predictable memory allocation time and size
- Below example creates a pool of bullets to allocate and use

```c++
class Bullet {
public:
    Bullet(){}

    void setSpeed(float speed) {
        m_speed = speed;
    }

    void update(float deltaTime) {
        m_x += m_speed * deltaTime;
        m_y += m_speed * deltaTime;
    }

    void reset() {
        m_speed = 0;
        m_x     = 0;
        m_y     = 0;
    }

    friend std::ostream& operator<<(std::ostream& os, 
                                    const Bullet& b) {
        os << b.m_x << ", " << b.m_y << ", " << b.m_speed;
        return os;
    }

private:
    float m_speed = 0;
    float m_x     = 0;
    float m_y     = 0;
};

class BulletPool {
public:
    BulletPool(size_t totalBullets) {
        // Allocate memory once to all the bullets
        m_pool = std::vector<Bullet>(totalBullets); 
        
        for (size_t i = 0; i < totalBullets; i++) {
            m_free.push_back(&m_pool[i]);
        }
    }

    ~BulletPool() {
        // No need to delete m_free as the memory
        // is managed by the std::vector m_pool
    }

    Bullet* allocate() {
        // Return a bullet to use from the pool of bullets
        if (m_free.empty()) {
            throw std::runtime_error("No bullets available");
        }
        Bullet* bullet = m_free.back();
        m_free.pop_back();
        return bullet;
    }

    void deallocate(Bullet* bullet) {
        // Reset and return a bullet to the pool
        bullet->reset();
        m_free.push_back(bullet);
    }

private:
    std::vector<Bullet>  m_pool;
    std::vector<Bullet*> m_free;
};

int main() {
    BulletPool bp = BulletPool(100);

    Bullet* b1 = bp.allocate();
    Bullet* b2 = bp.allocate();
    b1->setSpeed(5);
    b1->update(10);
    // prints 50, 50, 5
    std::cout << *b1 << std::endl;
    bp.deallocate(b1);
    bp.deallocate(b2);
}
```

<h3>Closing Thoughts</h3>
Although it's worth knowing the importance of dynamic memory and different ways to allocate and deallocate memory it's crucial to keep in the back of your mind the context of your application. 

"Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%". - Donald Knuth

<h3>FAQ</h3>

<h4>Why is ampersand used for both reference decleration and memory address operator?</h4>

- Originally '&' was used for memory address operation in C
- C++ decided to reuse the symbol to declare a reference
- '&' was chosen for both operations as they both deal with location of data
- Designed to reduce syntax bloat but also prone to causes confusion 
</div>
