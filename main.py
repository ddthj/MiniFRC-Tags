import cv2
import pyapriltags as apt
import calibrate
import camera


class MiniTags:
    """
    The MiniTags class was designed to be fairly portable and simple to use.
    It handles camera calibration and tag detection with the OpenCV and pyAprilTags libraries

    get_tag() returns a list of tags currently in frame. You will care most about the following properties:
    tag.tag_id: int, The ID of the tag. FRC tags are numbered 1 thru 16
    center: numpy.ndarray, The center of the tag measured in pixel coordinates
    pose_R: Optional[numpy.ndarray], The orientation matrix of the tag
    pose_t: Optional[numpy.ndarray], Vector from the camera to the tag, in meters

    ...For simpler/faster solutions, you may want to estimate_tag_pose = False and only use pixel coordinates

    """
    def __init__(self):
        # Camera resolution to use for calibration, distortion correction, and tag detection
        # Higher resolution takes more processing power but is more accurate
        # You should delete camera.npy after changing resolution to re-calibrate your camera
        self.camera_resolution = (480, 240)

        # You can set manual camera parameters if you are unhappy with the auto-calibration
        # [focal length x in pixels, y, camera center x, y] - see AprilTags documentation
        # self.camera_matrix = (350,350,CAMERA_RESOLUTION[0] / 2,CAMERA_RESOLUTION[1] / 2)
        self.camera_matrix = None

        # This is exclusively set by calibration code
        self.raw_matrix = None
        self.camera_distortion = None
        self.camera_optimizer = None

        # The edge length of your checkerboard squares used for camera calibration
        # Measured in meters, but not critical
        self.checker_size = 0.02261

        # The size of the apriltags in meters
        # I recommend looking at the documentation at https://github.com/AprilRobotics/apriltag
        self.tag_size = 0.0405  # For 1/4 scale 36h11 tags
        # self.tag_size = 0.0807  # For 1/2 scale 36h11 tags

        # What type of tags to detect
        # refer to the pyAprilTags documentation for tag standard names
        self.tag_standard = "tag36h11"

        # set up video capture with desired resolution
        # Use OPENCV for USB cameras and PICAMERA for the raspberry pi camera (attached via ribbon cable)
        self.camera = camera.Camera(self.camera_resolution, camera.OPENCV)

        # See https://github.com/WillB97/pyapriltags
        # And https://github.com/WillB97/pyapriltags/blob/master/test/test.py
        # This single line can greatly impact performance. Read the docs!
        self.detector = apt.Detector(families=self.tag_standard, nthreads=4, quad_decimate=1.0)

    def calibrate(self) -> bool:
        """
        calibrate() attempts to load 'camera.npy' or generate it if it doesn't exist.
        There are a couple levels of calibration available depending on what you need:

        1. Manual
        - Simply make a manual entry to self.camera_matrix instead of None
        - Good solution if you don't have a wide-angle camera lense (little distortion)
        - See comment where self.camera_matrix is defined on details

        2. Automatic
        - Takes some more setup: see the comment in calibrate_camera within calibrate.py
        - Great for correcting distortion in fisheye/wide-angle lenses
        - Only needs to be done once, a camera.npy file is created to store the settings
        """
        ret, matrix, distortion = calibrate.load_camera_properties()
        if not ret:
            print("Running Camera Calibration to generate camera.npy... Please Read calibrate.py for more info...")
            ret = calibrate.calibrate_camera(self.camera, self.checker_size)
            if ret:
                self.calibrate()
        else:
            self.raw_matrix = matrix
            self.camera_matrix = (matrix[0][0], matrix[1][1], matrix[0][2], matrix[1][2])
            self.camera_distortion = distortion
            self.camera_optimizer, roi = cv2.getOptimalNewCameraMatrix(matrix,
                                                                       distortion,
                                                                       self.camera_resolution,
                                                                       1,
                                                                       self.camera_resolution)
            return True

    def get_tags(self) -> list[apt.Detection]:
        ret, color_image = self.camera.read()
        if self.camera_optimizer is not None:
            color_image = cv2.undistort(color_image,
                                        self.raw_matrix,
                                        self.camera_distortion,
                                        None,
                                        self.camera_optimizer)
        gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        if self.camera_matrix is not None:
            detections = self.detector.detect(gray_image,
                                        estimate_tag_pose=True,
                                        camera_params=self.camera_matrix,
                                        tag_size=self.tag_size)
        else:
            detections = []
            print("No camera matrix! Set manually or call calibrate() before detecting tags!")
        return detections
