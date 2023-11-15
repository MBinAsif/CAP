# Car Acceptability Predictor (CAP)

CAP (Car-Acceptability-Predictor) is an application that predicts the acceptability of cars based on various features using machine learning techniques. This application has two versions: one with a simple interface developed using the Tkinter library and another with a more user-friendly UI created with Flask.

## Dataset

The dataset used for training the model was obtained from Kaggle: [Car Acceptability Classification Dataset](https://www.kaggle.com/datasets/subhajeetdas/car-acceptability-classification-dataset).

This dataset contains various features such as Buying_Price, Maintenance_Price, No_of_Doors, Person_Capacity, Size_of_Luggage, Safety, and Car_Acceptability, which were used to train the predictive model.

## Model

The machine learning model was trained using the spaCy library, a powerful natural language processing library in Python. The spaCy library was used to preprocess the dataset and train a text categorization model to predict car acceptability based on the provided features.

The code for training the model can be found in the Google Colab notebook:
[Google Colab - Model Training](https://colab.research.google.com/drive/1_UaBq6DsfgbzcDb9_OBJc9Lxrc6xyh9z#scrollTo=oIA70r5Rps1G)

## Versions

### 1. Tkinter Version

The Tkinter version of the Car Acceptability Predictor requires the user to manually input the car features in a graphical user interface built using the Tkinter library. To run this version, execute the script named `tkinter_version.py`.

### 2. Flask Version

The Flask version offers a more user-friendly interface with dropdown menus and input fields for the car features. Users can interact with a web interface to input car features and receive predictions about car acceptability. To run this version, execute the Flask application by running `app.py`.

## Usage

### Tkinter Version

1. Make sure you have Tkinter installed (`sudo apt-get install python3-tk` for Linux).
2. Run `tkinter_version.py`.
3. Enter the car features in the graphical interface.
4. Click on the "Predict" button to get the prediction.

### Flask Version

1. Install the necessary dependencies (`pip install flask`).
2. Run `app.py`.
3. Access the application via a web browser (usually at `http://localhost:5000`).
4. Input the car features in the provided form fields.
5. Click on the "Predict" button to get the prediction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
