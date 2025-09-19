import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import kurtosis, skew

st.set_page_config(page_title="Statistik Deskriptif", layout="centered")

# Simulasi logout
def logout():
    st.session_state['logged_out'] = True

# Tombol logout
if st.button("🔒 Logout"):
    logout()

if 'logged_out' in st.session_state and st.session_state['logged_out']:
    st.warning("Kamu telah logout dari aplikasi.")
    st.stop()

st.title("It's Your Descriptive Statistic")

# Upload file
uploaded_file = st.file_uploader("Unggah file Excel (.xlsx)", type=["xlsx"])

# Tombol clear
if st.button("🔄 Clear"):
    st.session_state.clear()
    st.rerun()

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

        if not numeric_cols:
            st.error("Tidak ada kolom numerik dalam file.")
        else:
            selected_col = st.selectbox("Pilih kolom data numerik", numeric_cols)
            data = df[selected_col].dropna()

            st.subheader(f"📈 Statistik untuk kolom: `{selected_col}`")

            mean = np.mean(data)
            std_err = stats.sem(data)
            median = np.median(data)
            mode = data.mode().iloc[0] if not data.mode().empty else "—"
            std_dev = np.std(data, ddof=1)
            kurt = kurtosis(data)
            skewness = skew(data)
            min_val = np.min(data)
            max_val = np.max(data)

            st.markdown(f"""
            - **Mean**: {mean:.4f}  
            - **Standard Error**: {std_err:.4f}  
            - **Median**: {median:.4f}  
            - **Mode**: {mode}  
            - **Standard Deviation**: {std_dev:.4f}  
            - **Kurtosis**: {kurt:.4f}  
            - **Skewness**: {skewness:.4f}  
            - **Minimum**: {min_val:.4f}  
            - **Maximum**: {max_val:.4f}
            """)
    except Exception as e:
        st.error(f"Gagal membaca file: {e}")
else:
    st.info("Silakan unggah file Excel untuk mulai analisis.")

st.markdown("<center><sub style='color:gray;'>✨ Made by YAY@2025 ✨</sub></center>", unsafe_allow_html=True)    
