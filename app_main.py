import argparse
import os
from typing import List
import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions

os.environ["GOOGLE_API_KEY"] = ""
gemini_model = genai.GenerativeModel("gemini-pro")


def build_query_prompt(query: str, context: List[str]) -> str:
    """Create a prompt combining system and user data."""
    base_prompt = {
        "content": "I am going to ask you a question, which I would like you to answer"
        " based mostly on the provided context and  external knowledge if no direct context is there."
        "Only provide response in text form as analyis or json format only [for json response instructions : with proper string headers/columns(with  metric like %, billion etc) and all numerical values/records/rows (dont put billion, dollor sign etc) (if table is there)] not both, no the reponse format"
        'json format : { "X title": ["x1", "x2", "x3", ...], "Y title": ["y1", "y2", "y3", ...] }'
    }
    user_prompt = {
        "content": f" The question is '{query}'. Here is the context you have but incase no direct context is there get help of other external knowledge:"
        f'{(" ").join(context)}',
    }
    return f"{base_prompt['content']} {user_prompt['content']}"


def get_gemini_answer(query: str, context: List[str]) -> str:
    """Obtain a response from the Gemini API."""
    response = gemini_model.generate_content(build_query_prompt(query, context))
    return response.text


def main(collection_name: str = "documents_collection", persist_dir: str = ".") -> None:
    """Run the main program for interactive user queries."""
    if "GOOGLE_API_KEY" not in os.environ:
        api_key = input("Please enter your Google API Key: ")
        genai.configure(api_key=api_key)
    else:
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    chroma_client = chromadb.PersistentClient(path=persist_dir)
    embedding_function = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=os.environ["GOOGLE_API_KEY"])

    collection_ref = chroma_client.get_collection(name=collection_name, embedding_function=embedding_function)

    while True:
        query = input("Enter your query: ").strip()
        if not query:
            print("Please provide a question. Press Ctrl+C to quit.")
            continue

        print("Processing...")
        results = collection_ref.query(query_texts=[query], n_results=5, include=["documents", "metadatas"])

        sources = "\n".join([f"{result['filename']}: Line {result['line_number']}" for result in results["metadatas"][0]])

        response = get_gemini_answer(query, results["documents"][0])
        print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Handle documents with a Chroma collection")
    parser.add_argument("--persist_directory", type=str, default="chroma_storage", help="Directory for Chroma storage")
    parser.add_argument("--collection_name", type=str, default="documents_collection", help="Chroma collection name")

    args = parser.parse_args()
    main(collection_name=args.collection_name, persist_dir=args.persist_directory)
