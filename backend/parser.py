from unstructured.partition.pdf import partition_pdf

def extract_chunks(pdf_path, chunk_size=1000):
    text = "".join([p.text for p in partition_pdf(pdf_path)])
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]