<!DOCTYPE html>
<html>
<head>
    <title>Real-Time Face Detection using OpenCV</title>
</head>
<body>
    <h1>Real-Time Face Detection using OpenCV</h1>
    <p>
        This Python script demonstrates real-time face detection using OpenCV's DNN module and a pre-trained Single Shot Multibox Detector (SSD) model. The SSD model can detect faces in images and video streams with good accuracy.
    </p>

    <h2>Prerequisites</h2>
    <p>
        To run this script, you need to have the following libraries installed:
    </p>
    <ul>
        <li>OpenCV (<code>opencv-python</code>): Used for computer vision tasks, including face detection.</li>
        <li>NumPy (<code>numpy</code>): Required for numerical computations.</li>
    </ul>
    <p>
        You can install these libraries using <code>pip</code>:
    </p>
    <pre><code>pip install opencv-python numpy</code></pre>

    <h2>Getting Started</h2>
    <ol>
        <li>Clone this repository or download the Python script directly.</li>
        <li>Download the pre-trained face detection model files from the OpenCV repository:</li>
    </ol>
    <ul>
        <li><a href="https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/deploy.prototxt">deploy.prototxt</a></li>
        <li><a href="https://github.com/opencv/opencv_3rdparty/blob/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel">res10_300x300_ssd_iter_140000.caffemodel</a></li>
    </ul>
    <p>Place the downloaded "deploy.prototxt" and "res10_300x300_ssd_iter_140000.caffemodel" files in the same directory as the Python script.</p>

    <h2>How to Use</h2>
    <ul>
        <li>Run the script in your Python environment:</li>
    </ul>
    <pre><code>python face_detection.py</code></pre>
    <ul>
        <li>The script will access your webcam and start detecting faces in real-time.</li>
        <li>Detected faces will be highlighted with green rectangles.</li>
        <li>Press 'q' to exit the application.</li>
    </ul>

    <h2>Configuration</h2>
    <p>
        You can adjust the face detection threshold by modifying the <code>confidence</code> variable in the script. The confidence threshold determines the minimum confidence score required to consider a face detection as valid. For example, setting <code>confidence = 0.5</code> means only detections with a confidence score higher than 0.5 will be displayed.
    </p>

    <h2>Acknowledgments</h2>
    <p>This script uses a pre-trained face detection model from OpenCV.</p>
    <ul>
        <li>OpenCV GitHub Repository: <a href="https://github.com/opencv/opencv">https://github.com/opencv/opencv</a></li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
