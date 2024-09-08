import streamlit as st
import tempfile
import os
import traceback
from rfp_analyzer import analyze_rfp, generate_pdf_report

# Set up environment variables
os.environ["ANTHROPIC_API_KEY"] = "api key"

st.title("RFP Analyzer")

uploaded_file = st.file_uploader("Upload your SaaS project proposal", type=["doc", "docx", "pdf"])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        # Write the uploaded file to the temporary file
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    if st.button("Analyze RFP"):
        with st.spinner("Analyzing RFP..."):
            try:
                analysis_result = analyze_rfp(tmp_file_path)
                st.json(analysis_result)
            except Exception as e:
                st.error(f"Error during RFP analysis: {str(e)}")
                st.error("Traceback:")
                st.code(traceback.format_exc())
    
    if st.button("Generate PDF Report"):
        with st.spinner("Generating PDF report..."):
            try:
                analysis_result = analyze_rfp(tmp_file_path)
                pdf_path = generate_pdf_report(analysis_result)
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="Download PDF Report",
                        data=pdf_file,
                        file_name="rfp_analysis.pdf",
                        mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"Error generating PDF report: {str(e)}")
                st.error("Traceback:")
                st.code(traceback.format_exc())
    
    # Clean up the temporary file
    os.unlink(tmp_file_path)