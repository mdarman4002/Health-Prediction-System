# Health Prediction System (Diabetes Prediction)

## Project Overview
This is a comprehensive Health Prediction System focusing on Diabetes Prediction. The system is built using Django for the web interface, with HTML and CSS for the front-end design. It integrates various Machine Learning models for accurate diabetes prediction.

## Machine Learning Models and Accuracy
- **Logistic Regression:** 94.36%
- **LightGBM:** 98.16%
- **XGBoost:** 98.03%
- **Decision Tree:** 96.76%
- **Random Forest:** 98.12%

## Dataset Source
- **Dataset:** [Comprehensive Diabetes Clinical Dataset (100k rows)](https://www.kaggle.com/code/godoistvan/eda-and-98-accuracy)

## Project Setup
### Prerequisites
- Python installed (preferably 3.8+)
- Django installed
- Required Python packages (see below)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mdarman4002/Health-Prediction-System.git
   cd Health-Prediction-System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the server:
   ```bash
   python manage.py runserver
   ```

## Requirements
```
pandas
numpy
matplotlib
seaborn
plotly
scikit-learn
imbalanced-learn
xgboost
lightgbm
django
```

## Usage
- Access the website at `http://localhost:8000`.
- Input your health details to get diabetes predictions.

## Project Structure
WebProject/
├── healthCareWeb/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/
│   └── homePage/
│       └── homeImageHealthCare.jpg
├── templates/
│   ├── breast_cancer.html
│   ├── diabetes.html
│   ├── diabetesResult.html
│   ├── heart_fail.html
│   └── home.html
├── db.sqlite3
├── manage.py
├── diabetes.ipynb
└── diabetes_dataset.csv

## Installation

1. Clone the repository:
```Bash
git clone https://github.com/mdarman4002/Health-Prediction-System.git
cd Health-Prediction-System
```
2. Install dependencies:
 ```bash
   pip install -r requirements.txt
 ```
3.Run migrations:
```Bash
python manage.py makemigrations
python manage.py migrate
```
4. Start the server:
```Bash
python manage.py runserver
```
## Contributing
Feel free to fork this project, submit issues, or create pull requests.


