# DBSCAN-Copy-Move-Foregry-Detection
#### Summary:
Copy move forgery detection using DBSCAN clustering algorithm.

#### Requirements
* Python3
* OpenCV (pip install opencv-python)
* OpenCV-contrib-python  https://stackoverflow.com/questions/60065707/cant-use-sift-in-opencv-v4-20?noredirect=1&lq=1
* Sklearn (pip install -U scikit-learn)

#### How To Run 
Type this command in the terminal. (See examples for complete idea)

`python main.py "path to the image" eps min_samples`
* (Mandatory) "path to the image" - this is the exact path to the image file (See examples).
* (Optional) eps - Eps value for DBSCAN algorithm. Increasing this will generate more clusters.(Value should be between 0-500)
* (Optional) min_samples - Min sample for DBSCAN algorithm. Increasing this will reduce clusters.(Value should be between 0-50).

After running press  **'S/s'** if you want to save the forgery detected image.
Press **'Q/q'** to exit.
(Make sure You have Selected the image window while pressing keys).
#### Examples
**Example 1**
![Example 1](https://github.com/Himj266/DBSCAN-Copy-Move-Foregry-Detection/blob/master/Example%201.png)

**Example 2**
![Example 2](https://github.com/Himj266/DBSCAN-Copy-Move-Foregry-Detection/blob/master/Example2.png)
