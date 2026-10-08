from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
import traceback
from werkzeug.utils import secure_filename
from analysis_engine import predict_fraud, read_flexible_csv

app = Flask(__name__)
app.secret_key = "super_secret_fraud_key"
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB for large statements

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
PLOTS_DIR = os.path.join("static", "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/demo', methods=['GET'])
def demo():
    sample_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample_yearly_bank_statement.csv')
    if not os.path.exists(sample_path):
        sample_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'financial_data.csv')
    try:
        results = predict_fraud(sample_path, PLOTS_DIR)
        return render_template('dashboard.html', results=results)
    except Exception as e:
        traceback.print_exc()
        flash(f"Error loading demo statement: {str(e)}")
        return redirect(url_for('index'))


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file provided in the upload request.')
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        flash('No file was selected for upload.')
        return redirect(url_for('index'))

    # Accept any CSV, TSV, or TXT tabular export
    allowed_exts = ('.csv', '.tsv', '.txt', '.xlsx', '.xls')
    if file and any(file.filename.lower().endswith(ext) for ext in allowed_exts):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            results = predict_fraud(filepath, PLOTS_DIR)
            return render_template('dashboard.html', results=results)
        except Exception as e:
            traceback.print_exc()
            flash(f"Error processing statement: {str(e)}")
            return redirect(url_for('index'))
    else:
        flash("Please upload a valid CSV, TSV, TXT, or Excel (.xlsx/.xls) bank statement.")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
