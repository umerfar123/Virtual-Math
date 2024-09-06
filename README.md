# Gesture Math

## Description

Gesture Math is a unique application that leverages machine learning and computer vision to enable users to solve mathematical problems by simply drawing them with their hands. 
The project uses Streamlit for a user-friendly interface and the Gemini model for powerful problem-solving capabilities.

## Features


* Intuitive Interface: A visually appealing Streamlit interface that guides users through the drawing process.
* Hand Gesture Recognition: Uses computer vision techniques to accurately recognize hand gestures for drawing and inputting commands.
* Real-time Drawing: Allows users to draw directly on the screen using their index finger.
* Problem Solving: Sends drawn images to the Gemini model for analysis and solution generation.
* Clear and Send Commands: Simple hand gestures for clearing the drawing area and submitting the image for processing.

  ![Draw](https://github.com/user-attachments/assets/1093f057-0a13-46a7-85d2-bfe3bf9a5cfd)

## Usage

1. Clone this repo using

   ```
     git clone https://github.com/umerfar123/Virtual-Math.git
   ```
2. Install required libraries using

   ```python
    pip install -r requirements.txt
   ```
3. Create your own api key for gemini model and paste it in [api.py](https://github.com/umerfar123/Virtual-Math/blob/main/api.py) file.

   ```
     apk = 'your api key'
   ```
4. Run the main file

   ```python
    Streamlit run gestureMath.py
   ```

## Contributions
Contributions to this project are welcome! Feel free to fork the repository, make changes, and submit a pull request.
