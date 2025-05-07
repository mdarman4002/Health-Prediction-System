from django.shortcuts import render
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMClassifier

# Create instances for label encoding
le_gender = LabelEncoder()
le_smoking = LabelEncoder()

def home(request):
    return render(request, 'home.html')



#---------------------------------------DIABETES-------------------------------------------------------
# ------------------------------------------------------------------------------------------
def diabetes(request):
    return render(request, 'diabetes.html')

def diabetesResult(request):
    # Load and preprocess the dataset
    df = pd.read_csv("D:/HealthCare Project/diabetes_dataset.csv")
    
    # Encode categorical variables
    df['gender'] = le_gender.fit_transform(df['gender'])
    df['smoking_history'] = le_smoking.fit_transform(df['smoking_history'])
    
    # Rename race columns for better accessibility
    df.rename(columns={
        'race:AfricanAmerican': 'africanamerican', 
        'race:Caucasian': 'caucasian', 
        'race:Hispanic': 'hispanic', 
        'race:Asian': 'asian', 
        'race:Other': 'other'
    }, inplace=True)

    # Drop unnecessary columns like 'year' and 'location'
    df = df.drop(['year', 'location'], axis=1)
    
    # Handle class imbalance using SMOTE
    smote = SMOTE()
    X = df.drop('diabetes', axis=1)
    y = df['diabetes']
    X, y = smote.fit_resample(X, y)
    
    # Split the data for training and testing
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a LightGBM model
    lgbm = LGBMClassifier()
    lgbm.fit(x_train, y_train)

    # Handle form submission for predictions
    if request.method == 'POST':
        try:
            # Get input values from the form
            val1 = request.POST.get('n1')  # gender
            val2 = float(request.POST.get('n2'))  # age
            val3 = request.POST.get('n3')  # race
            val4 = float(request.POST.get('n4'))  # hypertension
            val5 = float(request.POST.get('n5'))  # heart_disease
            val6 = request.POST.get('n6')  # smoking_history
            val7 = float(request.POST.get('n7'))  # bmi
            val8 = float(request.POST.get('n8'))  # hbA1c_level
            val9 = float(request.POST.get('n9'))  # blood_glucose_level

            # Encode gender and smoking history
            val1 = le_gender.transform([val1])[0] # gender
            val6 = le_smoking.transform([val6])[0] # smoking 
            
            # Map race to binary flags
            race_mapping = {
                'africanamerican': (1, 0, 0, 0, 0),
                'asian': (0, 1, 0, 0, 0),
                'caucasian': (0, 0, 1, 0, 0),
                'hispanic': (0, 0, 0, 1, 0),
                'other': (0, 0, 0, 0, 1)
            }
            val31, val32, val33, val34, val35 = race_mapping.get(val3, (0, 0, 0, 0, 0))

            # Make a prediction using the trained model
            pred = lgbm.predict([[val1, val2, val31, val32, val33, val34, val35, val4, val5, val6, val7, val8, val9]])

            # Determine the result for display
            #result = "Positive" if pred[0] == 1 else "Negative"
            if pred[0] == 1:
                result = "Positive"
            else:
                result = "Negative"
            return render(request, 'diabetesResult.html', {"result": result})
        
        except ValueError:
            return render(request, 'diabetesResult.html', {"result": "Error: Invalid input data."})

    # Render the template if not a POST request
    return render(request, 'diabetesResult.html')



#-------------------------------------------BREAST CANCER ---------------------------------------------------
# ------------------------------------------------------------------------------------------
def breast_cancer(request):
    return render(request, 'breast_cancer.html')




#---------------------------------------------HEART FAIL-------------------------------------------------
# ------------------------------------------------------------------------------------------
def heart_fail(request):
    return render(request, 'heart_fail.html')
