# TrolleyDetection

## Overview

This project is to estimate the difference of the number of beverages in trolley between on and off. To implement this, 
it is necessary to detect the beverages in the web camera capture screen. The pre-trained model, faster_rcnn_resnet_50, 
is trained with the data set of beverages.

## Structure

- src

    The source code to detect the beverages in the image using the trained model

- utils

    * The trained model to detect the beverages
    * The source code to manage the folder and files in this project
    
- app

    The main execution file
    
- requirements

    All the dependencies for this project
    
- settings

    The settings concerned with the path of several files

## Installation

- Environment

    Ubuntu 18.04, Windows 10, Python 3.6

- Dependency Installation

    Please go ahead this project directory and run the following command
    ```
        pip3 install -r requirements.txt
    ```

- Please download the trained model from https://drive.google.com/file/d/1UQ8tFZkGvC1IVNzLSMhsnCg9w5ByY9Lj/view?usp=sharing
and copy it to utils/model.

## Execution

- Please connect the web camera to your pc.

- Please go ahead this project directory and run the following command.

    ```
        python3 app.py
    ```
