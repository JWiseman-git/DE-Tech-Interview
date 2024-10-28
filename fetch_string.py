import requests
import gzip
from io import BytesIO
from lxml import etree

def download_file(url):
    """Download a file from the specified URL."""
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check if the request was successful
    return response.content

def parse_xml(xml_content):
    """Parse the XML content using lxml and yield each entry element."""
    # Create an XML pull parser to efficiently parse large XML files
    context = etree.iterparse(BytesIO(xml_content), events=("end",), tag="{http://uniprot.org/uniprot}entry")
    
    for event, entry in context:
        yield entry  # Yield the entry element to avoid memory buildup
        entry.clear()  # Clear the element after processing to free memory
        while entry.getprevious() is not None:
            del entry.getparent()[0]  # Remove previous siblings to keep memory usage low

def main():
    url = "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz"
    
    # Step 1: Download the gzipped XML file
    print("Downloading data...")
    gzipped_data = download_file(url)
    
    # Step 2: Decompress the gzipped file
    print("Decompressing data...")
    with gzip.open(BytesIO(gzipped_data), 'rb') as f:
        xml_content = f.read()
    
    # Step 3: Parse the XML and process entries
    print("Parsing XML data...")
    for entry in parse_xml(xml_content):
        # Example processing: print entry ID
        entry_id = entry.find("{http://uniprot.org/uniprot}name").text
        print(f"Entry ID: {entry_id}")
    
if __name__ == "__main__":
    main()
