# Bank Statement Fraud Detection 🔍

Protect your finances with this Bank Statement Fraud Detection tool. Simply upload your transaction history (CSV/Excel/TSV/TXT) and our analysis engine will scan for anomalies, flagging suspicious behavior and generating clear visual reports to help you spot potential fraud instantly.

## 🚀 Features
- **Upload Flexibility:** Supports `.csv`, `.xlsx`, `.xls`, `.tsv`, and `.txt` bank statements.
- **Intelligent Analysis:** Uses statistical profiling and predictive models to identify risky transactions based on patterns and locations.
- **Visual Insights:** Automatically generates beautiful charts showing your statement risk breakdown and category distribution.
- **Detailed Reporting:** Get a tabular breakdown of the top most suspicious transactions, including exact amounts and flags.

## 🛠️ Built With
- **Backend/Frontend:** Streamlit, Python
- **Data & ML:** Pandas, NumPy, Scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Frontend:** HTML, CSS (Vanilla)

## 💻 Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/UnawareStrom/Fraude-detection.git
cd Fraude-detection
```

### 2. Create a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Application
```bash
streamlit run streamlit_app.py
```
Then, navigate to the local URL provided in your terminal (usually `http://localhost:8501`).

## 🌐 Deployment (Streamlit Community Cloud or Render)
To deploy this application:
1. Make sure `streamlit` is in your `requirements.txt`.
2. Connect your GitHub repository to Streamlit Community Cloud (easiest) or Render as a "Web Service".
3. Use the start command: `streamlit run streamlit_app.py`

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
