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
- `diabetes/` - Django application folder
- `static/` - HTML, CSS, JavaScript, and image files
- `templates/` - HTML templates for the web pages
- `ml_models/` - Python scripts for ML model training

## Contributing
Feel free to fork this project, submit issues, or create pull requests.


