from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import Anthropic
from llama_index.node_parser import SimpleNodeParser

def process_document(file_path):
    # Load the document
    documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
    
    # Parse the document into nodes
    parser = SimpleNodeParser()
    nodes = parser.get_nodes_from_documents(documents)
    
    # Create a service context with Claude as the LLM
    llm = Anthropic(model="claude-3-opus-20240229")
    service_context = ServiceContext.from_defaults(llm=llm)
    
    # Create and return the index
    index = VectorStoreIndex(nodes, service_context=service_context)
    return index

def query_index(index, query):
    response = index.as_query_engine().query(query)
    return response.response