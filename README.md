# MiniFRC-Tags

MiniFRC-Tags is a small library that simplifies setup of AprilTags for MiniFRC. It is built upon OpenCV and pyAprilTags.
1/4 and 1/2 scale 36h11 tags are included in a printable PDF with IDs 1 through 16, the same standard that FRC uses.

## Dependencies
```opencv-python```

```pyapriltags```

```picamera2``` - Required only when using Raspberry Pi cameras

I have gotten away with using pip3 to install these on Linux, however on Raspberry Pi it is recommended to use `apt install python-<library>`

## Usage

- Plug in a video capture device
- Read and modify the `__init__` code in `main.py` as desired to change parameters such as image resolution, processing threads, etc.
- On the first run, the code will only calibrate your camera. Read `calibrate.py` for details on how this works.
- See example below to start your own solution, or run `example.py`

```python
minifrc_tags = MiniTags()
# On first run this generates camera.npy
# On subsequent runs it reads from camra.npy
minifrc_tags.calibrate()  

...

while True:
  tags = minifrc_tags.get_tags()
  for tag in tags:
    print(tag.tag_id)
    print(tag.pose_R)
    print(tag.pose_T)
    # todo - orient my robot to the tag!
```






### The MIT License (MIT)
Copyright © 2025 ddthj

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
