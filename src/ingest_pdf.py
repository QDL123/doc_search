from langchain_community.document_loaders import PyPDFLoader




def main():
    print("Ingesting PDFs")

    # Get text content from PDF
    loader = PyPDFLoader("../example_data/agi-house-invoice.pdf")
    pages = loader.load_and_split()

    print(pages[0].page_content)


    # Create embeddings using OpenAI
    



if __name__ == "__main__":
    main()