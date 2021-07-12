# Marks Predictor

## Overview

A web application which predicts the marks of a student based off the number of hours of study using machine learning. The application assumes that a student can study between 0 and 12 hours, and the marks scored lies between 0 and 100. The web app is based on the [MarksPredictor](https://github.com/nipunchamikara/MarksPredictor) repository.

The [student_scores.csv](https://raw.githubusercontent.com/nipunchamikara/marks-predictor-app/main/student_scores.csv) file is used as the dataset on which the model is trained.

## Usage

Before running the program for the first time, the packages mentioned in the [requirements.txt](https://raw.githubusercontent.com/nipunchamikara/marks-predictor-app/main/requirements.txt) file are to be installed using
```
 pip install -r requirements.txt
```

The development server can be run either by executing
```
flask run
```
which can be accessed by visiting [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or by directly executing the [app.py](https://raw.githubusercontent.com/nipunchamikara/marks-predictor-app/main/app.py) file.
```
py app.py
```
