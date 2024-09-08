import os
import re
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.anthropic import Anthropic
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index.core.settings import Settings
from langchain.embeddings import HuggingFaceEmbeddings
from pdf_generator import generate_pdf
from chart_generator import generate_chart

os.environ["ANTHROPIC_API_KEY"] = "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"

def process_document(file_path):
    # Configure global settings
    Settings.llm = Anthropic(model="claude-3-opus-20240229")
    Settings.embed_model = LangchainEmbedding(
        HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    )
    Settings.node_parser = SimpleNodeParser()

    # Load and process the document
    documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
    nodes = Settings.node_parser.get_nodes_from_documents(documents)
    
    # Create and return the index
    index = VectorStoreIndex(nodes)
    return index

def parse_numbers(numbers_string):
    # Split the string into lines
    lines = numbers_string.split('\n')
    numbers_dict = {}
    for line in lines:
        # Use regex to find key-value pairs
        match = re.match(r'(.+?):\s*(.+)', line.strip())
        if match:
            key, value = match.groups()
            # Try to convert value to float if possible
            try:
                value = float(value.replace('$', '').replace(',', ''))
            except ValueError:
                pass  # Keep as string if not a number
            numbers_dict[key.strip()] = value
    return numbers_dict

def analyze_rfp(file_path):
    # Process the document
    index = process_document(file_path)
    
    # Query the index for required information
    summary = index.as_query_engine().query("Provide a brief summary of the RFP").response
    numbers = index.as_query_engine().query("Extract key numbers and metrics from the RFP. Format each as 'Key: Value' on separate lines.").response
    objective = index.as_query_engine().query("What is the main objective of this RFP?").response
    target = index.as_query_engine().query("Who is the target audience or beneficiary of this project?").response
    
    # Parse numbers and metrics
    numbers_dict = parse_numbers(numbers)
    
    # Generate charts
    chart_buf = generate_chart(numbers_dict)
    
    # Compile results
    analysis_result = {
        "summary": summary,
        "numbers": numbers_dict,
        "objective": objective,
        "target": target,
        "chart": chart_buf
    }
    
    return analysis_result

def generate_pdf_report(analysis_result):
    return generate_pdf(analysis_result)

# Example usage
if __name__ == "__main__":
    file_path = "path_to_your_rfp_document.pdf"
    result = analyze_rfp(file_path)
    pdf_path = generate_pdf_report(result)
    print(f"PDF report generated: {pdf_path}")