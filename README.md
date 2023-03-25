
# Youtube-Ambient-Effect

Parallel and Distributed Processing Project: Recreating Youtube's Ambient Effect

## The Process Involved

* Read Frames of the video using OpenCV
* Read the pixel values of each frame
* Designate values to the position and spread of the box-shadow according to luminance
* Designate values to the color of box-shadow according to chroma sampling
* Create the equivalent css

## How to Use the script

* Clone the project
* Run `python -m venv venv`
* Install all the requirements using

    ``` python
    pip install -r requirements.txt
    ```

* Upload your video in the TestData folder
* Include the video in index.html in a `video` or a `div` element with `id "video"`
* run python3 main.py
