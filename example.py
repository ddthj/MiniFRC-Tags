from main import MiniTags

# Example usage
minitags = MiniTags()
minitags.calibrate()  # Loads/Creates camera parameters to correct for lens distortion
while True:
    # retrieve a list of tags currently in view
    tags = minitags.get_tags()

    if len(tags) > 0:
        # We will print some data from the first tag we see
        t = tags[0]
        # convert translation to millimeters
        p = (t.pose_t).round(4) * 1000
        # print the current translation relative to the camera...
        # note that these are in a coordinate system relative to the camera, so
        # rotating the camera will still change the translation of the tag
        print("\rTag %s detected! X: %s Y: %s Z: %s" % (t.tag_id, p[0], p[1], p[2]), end="")