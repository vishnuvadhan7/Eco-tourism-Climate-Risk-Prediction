"""
Simplified model training script for web interface demo
Creates the essential model files needed for the web application
"""
import pandas as pd
import numpy as np
import joblib
import json
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR, SVC
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

def generate_demo_data(n_samples=5000):
    """Generate synthetic eco-tourism data for demo"""
    print("Generating synthetic eco-tourism data...")
    
    data = {
        'Site_ID': range(1, n_samples + 1),
        'Site_Name': [f'EcoSite_{i}' for i in range(1, n_samples + 1)],
        'Latitude': np.random.uniform(10, 50, n_samples),
        'Longitude': np.random.uniform(-130, -60, n_samples),
        'Country': np.random.choice(['USA', 'Canada', 'Mexico', 'Costa Rica', 'Brazil'], n_samples),
        'Biodiversity_Index': np.random.uniform(0.2, 1.0, n_samples),
        'Air_Quality_Index': np.random.uniform(20, 200, n_samples),
        'Elevation_m': np.random.uniform(0, 4000, n_samples),
        'Vegetation_Type': np.random.choice(['Tropical_Forest', 'Temperate_Forest', 'Grassland',
                                           'Desert', 'Wetland', 'Mountain'], n_samples),
        'Flood_Risk_Index': np.random.uniform(0, 1, n_samples),
        'Drought_Risk_Index': np.random.uniform(0, 1, n_samples),
        'Temperature_C': np.random.uniform(5, 40, n_samples),
        'Annual_Rainfall_mm': np.random.uniform(200, 3000, n_samples),
        'Soil_Type': np.random.choice(['Clay', 'Sand', 'Loam', 'Rocky', 'Volcanic'], n_samples),
        'Soil_Erosion_Risk': np.random.uniform(0, 1, n_samples),
        'Tourist_Capacity_Limit': np.random.uniform(100, 5000, n_samples),
        'Current_Tourist_Count': np.random.uniform(50, 4000, n_samples),
        'Accessibility_Score': np.random.uniform(0.1, 1.0, n_samples),
        'Human_Activity_Index': np.random.uniform(0.05, 0.95, n_samples),
        'Protected_Area_Status': np.random.choice([True, False], n_samples),
        'Conservation_Investment_USD': np.random.uniform(10000, 500000, n_samples),
        'Climate_Risk_Score': np.random.uniform(0.1, 0.9, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Calculate Vulnerability Score (target variable)
    df['Vulnerability_Score'] = (
        0.25 * (1 - df['Biodiversity_Index']) +
        0.15 * (df['Air_Quality_Index'] / 200) +
        0.15 * df['Flood_Risk_Index'] +
        0.15 * df['Drought_Risk_Index'] +
        0.10 * df['Soil_Erosion_Risk'] +
        0.10 * (df['Temperature_C'] / 40) +
        0.10 * df['Climate_Risk_Score']
    )
    df['Vulnerability_Score'] += np.random.normal(0, 0.05, n_samples)
    df['Vulnerability_Score'] = np.clip(df['Vulnerability_Score'], 0, 1)
    
    # Create Risk Categories
    df['Risk_Category'] = pd.cut(
        df['Vulnerability_Score'],
        bins=[0, 0.33, 0.67, 1.0],
        labels=['Low', 'Medium', 'High']
    )
    
    print(f"Generated {len(df)} samples with {len(df.columns)} features")
    return df

def preprocess_data(df, target_column='Vulnerability_Score', task_type='regression'):
    """Preprocess data for ML models"""
    print(f"\nPreprocessing data for {task_type}...")
    
    processed_df = df.copy()
    
    # Handle missing values (shouldn't be any in synthetic data, but good practice)
    numeric_columns = processed_df.select_dtypes(include=[np.number]).columns
    categorical_columns = processed_df.select_dtypes(include=['object', 'category']).columns
    
    # Prepare feature matrix X
    X = processed_df.copy()
    
    # Encode categorical variables
    categorical_columns_to_encode = ['Vegetation_Type', 'Soil_Type', 'Country']
    label_encoders = {}
    
    for col in categorical_columns_to_encode:
        if col in X.columns:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))
            label_encoders[col] = le
            print(f"  Encoded {col}: {len(le.classes_)} categories")
    
    # Handle boolean columns
    if 'Protected_Area_Status' in X.columns:
        X['Protected_Area_Status'] = X['Protected_Area_Status'].astype(int)
    
    # Remove non-feature columns
    columns_to_remove = ['Site_ID', 'Site_Name', target_column]
    if task_type == 'classification' and 'Risk_Category' in X.columns:
        columns_to_remove.append('Risk_Category')
    elif task_type == 'regression' and 'Risk_Category' in X.columns:
        columns_to_remove.append('Risk_Category')
    
    for col in columns_to_remove:
        if col in X.columns:
            X = X.drop(col, axis=1)
    
    # Prepare target variable y
    if task_type == 'regression':
        y = processed_df[target_column]
        print(f"  Target variable: {target_column} (continuous)")
    else:  # classification
        if 'Risk_Category' in processed_df.columns:
            le_target = LabelEncoder()
            y = le_target.fit_transform(processed_df['Risk_Category'])
            print(f"  Target variable: Risk_Category (categorical)")
            print(f"  Classes: {le_target.classes_}")
        else:
            y = pd.cut(processed_df[target_column], bins=3, labels=[0, 1, 2])
            print(f"  Target variable: Created from {target_column} (3 categories)")
    
    print(f"  Features: {X.shape[1]}, Samples: {X.shape[0]}")
    return X, y, label_encoders

def train_models(X, y, task_type='regression'):
    """Train ML models"""
    print(f"\nTraining {task_type} models...")
    
    # Split data
    if task_type == 'classification':
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
    else:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"  Training set: {X_train.shape}, Test set: {X_test.shape}")
    
    # Define models
    if task_type == 'regression':
        models = {
            'XGBoost': RandomForestRegressor(n_estimators=100, random_state=42),  # Using RF as XGBoost placeholder
            'Linear': LinearRegression(),
            'SVR': SVR(kernel='rbf', C=1.0)
        }
    else:
        models = {
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'Logistic': LogisticRegression(random_state=42, max_iter=1000),
            'SVC': SVC(kernel='rbf', C=1.0, probability=True, random_state=42)
        }
    
    best_model = None
    best_score = -float('inf') if task_type == 'regression' else 0
    best_name = ''
    
    for name, model in models.items():
        print(f"  Training {name}...")
        try:
            # Train model
            model.fit(X_train_scaled, y_train)
            
            # Make predictions
            train_pred = model.predict(X_train_scaled)
            test_pred = model.predict(X_test_scaled)
            
            # Calculate metrics
            if task_type == 'regression':
                train_score = r2_score(y_train, train_pred)
                test_score = r2_score(y_test, test_pred)
                rmse = np.sqrt(mean_squared_error(y_test, test_pred))
                print(f"    R² (train/test): {train_score:.4f}/{test_score:.4f}, RMSE: {rmse:.4f}")
                
                if test_score > best_score:
                    best_score = test_score
                    best_model = model
                    best_name = name
            else:
                train_score = accuracy_score(y_train, train_pred)
                test_score = accuracy_score(y_test, test_pred)
                print(f"    Accuracy (train/test): {train_score:.4f}/{test_score:.4f}")
                
                if test_score > best_score:
                    best_score = test_score
                    best_model = model
                    best_name = name
                    
        except Exception as e:
            print(f"    Error training {name}: {str(e)}")
            continue
    
    print(f"  Best model: {best_name} (score: {best_score:.4f})")
    return best_model, scaler, best_name

def main():
    """Main function to generate models for web interface"""
    print("="*60)
    print("SIMPLIFIED ECO-TOURISM CLIMATE RISK MODEL GENERATION")
    print("="*60)
    
    # Generate demo data
    df = generate_demo_data()
    
    # Train regression model
    X_reg, y_reg, encoders_reg = preprocess_data(df, task_type='regression')
    regression_model, scaler_reg, reg_name = train_models(X_reg, y_reg, task_type='regression')
    
    # Train classification model  
    X_clf, y_clf, encoders_clf = preprocess_data(df, task_type='classification')
    classification_model, scaler_clf, clf_name = train_models(X_clf, y_clf, task_type='classification')
    
    # Save models and processors
    print("\nSaving models and processors...")
    
    # Save models
    reg_filename = f'best_regression_model_{reg_name.lower().replace(" ", "_")}.pkl'
    clf_filename = f'best_classification_model_{clf_name.lower().replace(" ", "_")}.pkl'
    
    joblib.dump(regression_model, reg_filename)
    joblib.dump(classification_model, clf_filename)
    print(f"  Saved: {reg_filename}")
    print(f"  Saved: {clf_filename}")
    
    # Save scalers
    joblib.dump(scaler_reg, 'regression_scaler.pkl')
    joblib.dump(scaler_clf, 'classification_scaler.pkl')
    print("  Saved: regression_scaler.pkl")
    print("  Saved: classification_scaler.pkl")
    
    # Save encoders
    joblib.dump(encoders_reg, 'regression_encoders.pkl')
    joblib.dump(encoders_clf, 'classification_encoders.pkl')
    print("  Saved: regression_encoders.pkl")
    print("  Saved: classification_encoders.pkl")
    
    # Save feature names
    feature_names = {
        'regression_features': list(X_reg.columns),
        'classification_features': list(X_clf.columns)
    }
    
    with open('feature_names.json', 'w') as f:
        json.dump(feature_names, f, indent=2)
    print("  Saved: feature_names.json")
    
    # Save sample data for testing
    sample_data = df.head().to_dict('records')
    with open('sample_data.json', 'w') as f:
        json.dump(sample_data, f, indent=2)
    print("  Saved: sample_data.json")
    
    print("\n" + "="*60)
    print("MODEL GENERATION COMPLETE!")
    print("="*60)
    print("All required files have been generated for the web interface:")
    print(f"- Regression model: {reg_filename}")
    print(f"- Classification model: {clf_filename}")
    print("- Scalers: regression_scaler.pkl, classification_scaler.pkl")
    print("- Encoders: regression_encoders.pkl, classification_encoders.pkl")
    print("- Feature names: feature_names.json")
    print("- Sample data: sample_data.json")
    print("\nYou can now run the web application with: python app.py")

if __name__ == "__main__":
    main()