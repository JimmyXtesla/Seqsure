import os
from flask import request, jsonify, current_app
from werkzeug.utils import secure_filename

@current_app.route('/uploads', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200


from .pipeline_handler import run_nextflow_pipeline

@current_app.route('/run_pipeline', methods=['POST'])
def run_pipeline():
    data = request.json
    input_file = os.path.join(current_app.config['UPLOAD_FOLDER'], data.get('filename'))
    output_dir = current_app.config['OUTPUT_FOLDER']
    
    if not os.path.exists(input_file):
        return jsonify({'error': 'Input file not found'}), 400
    
    result = run_nextflow_pipeline(input_file, output_dir)
    
    if result['success']:
        return jsonify({'message': 'Pipeline executed successfully', 'output': result['stdout']}), 200
    else:
        return jsonify({'error': 'Pipeline execution failed', 'stderr': result['stderr']}), 500
