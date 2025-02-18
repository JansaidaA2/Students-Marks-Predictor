# Students-Marks-Predictor App


This project is an end-to-end machine learning application that predicts student marks based on the number of study hours. The application is built using Python, Flask, and Scikit-Learn, and it provides a simple web interface for users to input their study hours and get a predicted mark.

## Features
- *Machine Learning Model*: Uses Linear Regression to predict student marks based on study hours.
- *Web Interface*: Built with Flask, allowing users to interact with the model through a web browser.
- *Data Visualization*: Includes scatter plots to visualize the relationship between study hours and marks.
- *Data Cleaning*: Handles missing data by filling NaN values with the mean of the column.
- *Model Persistence*: The trained model is saved using joblib for future use.
- *CSV Logging*: Saves user inputs and predictions to a CSV file for further analysis.

## Technologies Used
- *Python*: Primary programming language.
- *Flask*: Web framework for building the application.
- *Scikit-Learn*: Machine learning library for building and training the Linear Regression model.
- *Pandas*: Data manipulation and analysis.
- *Matplotlib*: Data visualization.
- *Joblib*: Model persistence.

## Usage
1. Enter the number of study hours in the input field.
2. Click the "Predict" button to see the predicted marks.
3. The application will display the predicted marks and save the input and prediction to a CSV file.

## Dataset
The dataset used for training the model contains two columns:
- *study_hours*: Number of hours studied by the student.
- *student_marks*: Marks obtained by the student.

## Model Performance
The Linear Regression model achieved an accuracy of *95.14%* on the test dataset.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## Acknowledgments
- Thanks to [IndianAllProduction](https://indianallproduction.com) for the project tutorial and inspiration.
- Special thanks to the open-source community for providing the tools and libraries used in this project.
