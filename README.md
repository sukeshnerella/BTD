# Brain Tumor Detection System

Welcome to the Brain Tumor Detection System repository! This project aims to detect the presence of a brain tumor and predict its type using machine learning techniques. The system is capable of handling multiple input images concurrently and can be run both on the web and on Android devices.

## Features

- Detects the presence of a brain tumor.
- Predicts the type of tumor if present.
- Handles multiple input images concurrently.
- Runs on the web and Android platforms.

## Dataset

### Used for Testing

- Glioma: 300 items
- Meningioma: 306 items
- Pituitary: 300 items
- No tumor: 405 items

**Total MRI images used for testing: 1311 items**

### Used for Training

- Glioma: 1321 items
- Meningioma: 1339 items
- Pituitary: 1457 items
- No tumor: 1595 items

**Total MRI images used for training: 5712**

## Application Usage

### Web Application

To access the web application:

1. Open the command prompt.
2. Navigate to the project directory.
3. Run the following command: `streamlit run streamlit_app.py`
4. Once the process is complete, the web app will open. You can select MRI reports from your device.

### Command Line Application

To run the application via the command line:

1. Open the command prompt.
2. Navigate to the project directory.
3. Run the following command: `python app.py`

## Demo Dataset

The demo dataset is provided in the `demo` folder of this project. Feel free to use these images to test the system.

For any queries or issues, please raise them in the "Issues" section of this repository.

Thank you for using our Brain Tumor Detection System!