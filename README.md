# MiniFRC-Tags

MiniFRC-Tags is a small library that simplifies setup of AprilTags for MiniFRC. It is built upon OpenCV and pyAprilTags.
1/4 and 1/2 scale 36h11 tags are included in a printable PDF with IDs 1 through 16, the same standard that FRC uses.

## Dependencies
```pip3 install opencv-python```

```pip3 install pyapriltags```

```pip3 install numpy```

## Usage

- Plug in a video capture device
- Remove/Modify the example code at the end of `main.py`, or simply run it!
- The code will initially run a one-time camera calibration that requires you to print a special pattern. See the detailed explanation inside `calibrate.py`
- On subsequent runs, the example will search for FRC-style AprilTags and print their local coordinates relative to the camera
- Read through the code comments for detailed documentation on parameters

Once you have a camera.npy file generated, the intended usage is something like this:

```python
minifrc_tags = MiniTags()
minifrc_tags.calibrate()

...

while robot_loop:
  tags = minifrc_tags.get_tags()
  for tag in tags:
    print(tag.tag_id)
    print(tag.pose_R)
    print(tag.pose_T)
    # todo - orient my robot to the tag!
```






### The MIT License (MIT)
Copyright © 2024 ddthj

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
