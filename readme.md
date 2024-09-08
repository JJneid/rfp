# RFP Analyzer

## Overview

RFP Analyzer is a Streamlit-based web application that automates the analysis of Request for Proposal (RFP) documents. It uses advanced natural language processing techniques to extract key information, summarize content, and generate insightful reports from uploaded RFP documents.

## Features

- **Document Upload**: Supports various document formats including PDF, DOC, and DOCX.
- **Automated Analysis**: Extracts and summarizes key information from RFPs.
- **Key Metrics Extraction**: Identifies and extracts important numbers and metrics.
- **Objective Identification**: Determines the main objectives of the RFP.
- **Target Audience Analysis**: Identifies the intended audience or beneficiaries of the project.
- **Chart Generation**: Creates visual representations of key data points.
- **PDF Report Generation**: Compiles analysis results into a downloadable PDF report.

## Technologies Used

- Python
- Streamlit
- LlamaIndex
- Anthropic's Claude AI model
- Langchain
- HuggingFace Transformers

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/rfp-analyzer.git
   cd rfp-analyzer
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Anthropic API key:
   - Option 1: Set it as an environment variable:
     ```
     export ANTHROPIC_API_KEY=your_api_key_here
     ```
   - Option 2: You'll be prompted to enter it when you run the application.

## Usage

1. Start the Streamlit app:
   ```
   streamlit run streamlit-ui.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload an RFP document using the file uploader.

4. Click on "Analyze RFP" to process the document and view the results.

5. Click on "Generate PDF Report" to create and download a comprehensive PDF report of the analysis.

## Project Structure

- `streamlit-ui.py`: The main Streamlit application file.
- `rfp_analyzer.py`: Contains the core logic for RFP analysis.
- `pdf_generator.py`: Handles the generation of PDF reports.
- `chart_generator.py`: Creates charts and visualizations from extracted data.
- `requirements.txt`: Lists all Python dependencies.

## Contributing

Contributions to improve RFP Analyzer are welcome. Please feel free to submit a Pull Request.

