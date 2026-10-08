import streamlit as st
import os
import tempfile
import pandas as pd
from analysis_engine import predict_fraud

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide", initial_sidebar_state="expanded")

st.title("Bank Statement Fraud Detection")
st.markdown("Upload a bank statement to analyze for suspicious transactions.")

# Initialize directories
PLOTS_DIR = os.path.join("static", "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Upload Bank Statement (CSV, Excel, TSV, TXT)", type=["csv", "xlsx", "xls", "tsv", "txt"])

if uploaded_file is not None:
    # Save uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_filepath = tmp_file.name

    st.success("File uploaded successfully! Processing...")

    with st.spinner("Analyzing transactions..."):
        try:
            # Run prediction
            results = predict_fraud(tmp_filepath, PLOTS_DIR)
            
            # Overview Metrics
            st.header("Analysis Overview")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Transactions (Cleaned)", results["cleaned_transactions"])
            with col2:
                st.metric("Flagged as Suspicious", f"{results['flagged_count']} ({results['flagged_percent']}%)")
            with col3:
                st.metric("Total Suspicious Amount", results["total_suspicious_amount"])
            
            st.divider()

            # Plots
            st.header("Visual Insights")
            plot_col1, plot_col2 = st.columns(2)
            
            plot1_path = os.path.join(PLOTS_DIR, "plot1_overview.png")
            plot2_path = os.path.join(PLOTS_DIR, "plot2_location_risk.png")
            
            with plot_col1:
                if os.path.exists(plot1_path):
                    st.image(plot1_path, caption="Statement Risk Breakdown")
                else:
                    st.warning("Overview plot not available.")
                    
            with plot_col2:
                if os.path.exists(plot2_path):
                    st.image(plot2_path, caption="Category Breakdown")
                else:
                    st.warning("Category plot not available.")
            
            st.divider()

            # Top Suspicious Transactions
            st.header("Top Suspicious Transactions")
            if results["top_suspicious"]:
                # Convert list of dicts to dataframe for nicer display
                df_suspicious = pd.DataFrame(results["top_suspicious"])
                st.dataframe(df_suspicious, use_container_width=True)
            else:
                st.info("No highly suspicious transactions found.")
                
        except Exception as e:
            st.error(f"An error occurred during analysis: {str(e)}")
        finally:
            # Cleanup temporary file
            if os.path.exists(tmp_filepath):
                os.remove(tmp_filepath)
