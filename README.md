# CellDetectionAnalysis
A cell detection program that detects the presence of E.coli cells in a filter, the image analysis is conducted using a microscopic 10,000 um focus.
The image is firstly parsed from BGR to GRAYSCALE to detect lighter contours and mark areas of pixels lighter than Black, the process follows as:
-> Loading and displaying an image
-> Accessing individual pixels
-> Array Slicing and Cropping
-> Resizing Image
-> Rotating an image
-> Smoothing an image
-> Drawing/Marking the image

Following tools used: Python, OpenCV Libraries (cv2, imutils), NumPy, MatPlotLib
