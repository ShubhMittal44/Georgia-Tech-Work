import os
import argparse
from tqdm import tqdm
import chromadb
from chromadb.utils import embedding_functions
import google.generativeai as genai
import sys

os.environ["GOOGLE_API_KEY"] = ""

def split_large_text(text, max_length=9500):
    """Divide large texts into smaller parts without exceeding max_length."""
    parts = []
    while len(text) > max_length:
        split_point = text.rfind(' ', 0, max_length)
        if split_point == -1:
            split_point = max_length
        parts.append(text[:split_point])
        text = text[split_point:].strip()
    parts.append(text)
    return parts


def load_documents(directory="documents", collection_name="documents_collection", persist_dir="."):
    """Load files into a persistent Chroma collection."""
    docs = []
    metadata = []
    files = os.listdir(directory)
    
    for filename in files:
        with open(f"{directory}/{filename}", "r", encoding='utf-8') as file:
            for line_num, line in enumerate(tqdm(file.readlines(), desc=f"Reading {filename}"), 1):
                line = line.strip()
                if sys.getsizeof(line) > 9500:
                    line = split_large_text(line)
                if not line:
                    continue
                docs.append(line)
                metadata.append({"filename": filename, "line_number": line_num})

    client = chromadb.PersistentClient(path=persist_dir)
    embedding_function = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=os.environ["GOOGLE_API_KEY"])
    collection = client.get_or_create_collection(name=collection_name, embedding_function=embedding_function)

    count = collection.count()
    print(f"Collection already has {count} documents.")
    ids = [str(i) for i in range(count, count + len(docs))]

    for i in tqdm(range(0, len(docs), 1), desc="Adding Documents", unit_scale=1):
        collection.add(ids=ids[i: i + 1], documents=docs[i: i + 1], metadatas=metadata[i: i + 1])

    new_count = collection.count()
    print(f"Added {new_count - count} documents.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add documents to a Chroma collection")
    parser.add_argument("--directory", type=str, default="documents", help="Directory containing the text files")
    parser.add_argument("--collection_name", type=str, default="documents_collection", help="Chroma collection name")
    parser.add_argument("--persist_dir", type=str, default="chroma_storage", help="Directory for storing Chroma collection")

    args = parser.parse_args()
    load_documents(directory=args.directory, collection_name=args.collection_name, persist_dir=args.persist_dir)
