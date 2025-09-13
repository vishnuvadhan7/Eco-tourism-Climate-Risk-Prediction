"""
Vercel serverless function for health check
"""
import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        # Check if model files exist
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        
        model_files = [
            'best_regression_model_linear.pkl',
            'best_classification_model_logistic.pkl',
            'regression_scaler.pkl',
            'classification_scaler.pkl',
            'regression_encoders.pkl',
            'classification_encoders.pkl',
            'feature_names.json'
        ]
        
        missing_files = []
        for file in model_files:
            if not os.path.exists(os.path.join(parent_dir, file)):
                missing_files.append(file)
        
        models_loaded = len(missing_files) == 0
        
        return jsonify({
            'status': 'healthy' if models_loaded else 'partial',
            'models_loaded': models_loaded,
            'available_models': ['regression', 'classification'] if models_loaded else [],
            'missing_files': missing_files if missing_files else None
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'models_loaded': False,
            'error': str(e)
        }), 500

# For Vercel deployment
def handler(request):
    """Vercel serverless function handler"""
    with app.test_request_context(request.url, method=request.method, headers=dict(request.headers)):
        try:
            response = app.full_dispatch_request()
            return response
        except Exception as e:
            return jsonify({'error': str(e)}), 500