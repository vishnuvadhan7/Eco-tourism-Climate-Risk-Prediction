"""
Lightweight model setup for Vercel deployment
This script generates minimal models suitable for deployment
"""
import pandas as pd
import numpy as np
import joblib
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
import warnings
warnings.filterwarnings('ignore')

def create_minimal_models():
    """Create minimal models for deployment"""
    print("Creating minimal models for Vercel deployment...")
    
    # Generate minimal synthetic data
    n_samples = 1000
    np.random.seed(42)
    
    data = {
        'Latitude': np.random.uniform(25, 45, n_samples),
        'Longitude': np.random.uniform(-125, -65, n_samples),
        'Country': np.random.choice(['USA', 'Canada', 'Mexico'], n_samples),
        'Biodiversity_Index': np.random.uniform(0.3, 0.9, n_samples),
        'Air_Quality_Index': np.random.uniform(30, 150, n_samples),
        'Elevation_m': np.random.uniform(0, 3000, n_samples),
        'Vegetation_Type': np.random.choice(['Forest', 'Mountain', 'Wetland', 'Grassland'], n_samples),
        'Flood_Risk_Index': np.random.uniform(0, 1, n_samples),
        'Drought_Risk_Index': np.random.uniform(0, 1, n_samples),
        'Temperature_C': np.random.uniform(10, 35, n_samples),
        'Annual_Rainfall_mm': np.random.uniform(400, 2500, n_samples),
        'Soil_Type': np.random.choice(['Clay', 'Sand', 'Loam', 'Rocky'], n_samples),
        'Soil_Erosion_Risk': np.random.uniform(0, 0.8, n_samples),
        'Tourist_Capacity_Limit': np.random.uniform(200, 3000, n_samples),
        'Current_Tourist_Count': np.random.uniform(100, 2500, n_samples),
        'Accessibility_Score': np.random.uniform(0.2, 0.9, n_samples),
        'Human_Activity_Index': np.random.uniform(0.1, 0.8, n_samples),
        'Protected_Area_Status': np.random.choice([True, False], n_samples),
        'Conservation_Investment_USD': np.random.uniform(50000, 300000, n_samples),
        'Climate_Risk_Score': np.random.uniform(0.2, 0.8, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Create target variables
    df['Vulnerability_Score'] = (
        0.3 * (1 - df['Biodiversity_Index']) +
        0.2 * (df['Air_Quality_Index'] / 150) +
        0.2 * df['Flood_Risk_Index'] +
        0.15 * df['Climate_Risk_Score'] +
        0.15 * df['Soil_Erosion_Risk']
    )
    df['Vulnerability_Score'] = np.clip(df['Vulnerability_Score'], 0, 1)
    
    df['Risk_Category'] = pd.cut(
        df['Vulnerability_Score'],
        bins=[0, 0.33, 0.67, 1.0],
        labels=['Low', 'Medium', 'High']
    )
    
    # Prepare features
    X = df.copy()
    
    # Encode categorical variables
    categorical_features = ['Vegetation_Type', 'Soil_Type', 'Country']
    encoders = {}
    
    for feature in categorical_features:
        le = LabelEncoder()
        X[feature] = le.fit_transform(X[feature])
        encoders[feature] = le
    
    # Handle boolean
    X['Protected_Area_Status'] = X['Protected_Area_Status'].astype(int)
    
    # Remove target and ID columns
    feature_columns = [col for col in X.columns if col not in 
                      ['Vulnerability_Score', 'Risk_Category']]
    X = X[feature_columns]
    
    print(f"Features: {list(X.columns)}")
    
    # Train regression model
    y_reg = df['Vulnerability_Score']
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
        X, y_reg, test_size=0.2, random_state=42
    )
    
    scaler_reg = StandardScaler()
    X_train_reg_scaled = scaler_reg.fit_transform(X_train_reg)
    X_test_reg_scaled = scaler_reg.transform(X_test_reg)
    
    reg_model = LinearRegression()
    reg_model.fit(X_train_reg_scaled, y_train_reg)
    
    print(f"Regression R² score: {reg_model.score(X_test_reg_scaled, y_test_reg):.4f}")
    
    # Train classification model
    y_clf = pd.Categorical(df['Risk_Category']).codes
    X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
        X, y_clf, test_size=0.2, random_state=42, stratify=y_clf
    )
    
    scaler_clf = StandardScaler()
    X_train_clf_scaled = scaler_clf.fit_transform(X_train_clf)
    X_test_clf_scaled = scaler_clf.transform(X_test_clf)
    
    clf_model = LogisticRegression(random_state=42, max_iter=1000)
    clf_model.fit(X_train_clf_scaled, y_train_clf)
    
    print(f"Classification accuracy: {clf_model.score(X_test_clf_scaled, y_test_clf):.4f}")
    
    # Save models (lightweight)
    joblib.dump(reg_model, 'best_regression_model_linear.pkl', compress=3)
    joblib.dump(clf_model, 'best_classification_model_logistic.pkl', compress=3)
    joblib.dump(scaler_reg, 'regression_scaler.pkl', compress=3)
    joblib.dump(scaler_clf, 'classification_scaler.pkl', compress=3)
    
    # Save encoders
    encoders_reg = encoders.copy()
    encoders_clf = encoders.copy()
    joblib.dump(encoders_reg, 'regression_encoders.pkl', compress=3)
    joblib.dump(encoders_clf, 'classification_encoders.pkl', compress=3)
    
    # Save feature names
    feature_names = {
        'regression_features': list(X.columns),
        'classification_features': list(X.columns)
    }
    
    with open('feature_names.json', 'w') as f:
        json.dump(feature_names, f, indent=2)
    
    print("Minimal models created successfully!")
    print("Files generated:")
    print("- best_regression_model_linear.pkl")
    print("- best_classification_model_logistic.pkl") 
    print("- regression_scaler.pkl")
    print("- classification_scaler.pkl")
    print("- regression_encoders.pkl")
    print("- classification_encoders.pkl")
    print("- feature_names.json")

if __name__ == "__main__":
    create_minimal_models()