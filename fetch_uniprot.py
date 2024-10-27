import requests
import gzip
from io import BytesIO
from lxml import etree
import pandas as pd

def download_file(url):
    """Download a file from the specified URL."""
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check if the request was successful
    return response.content

def parse_xml(xml_content):
    """Parse the XML content using lxml and yield selected fields for each entry."""
    # Use lxml's iterparse to parse large XML files
    context = etree.iterparse(BytesIO(xml_content), events=("end",), tag="{http://uniprot.org/uniprot}entry")
    
    for event, entry in context:
        # Extract required fields
        data = {}
        
        # Primary Accession
        accession = entry.find("{http://uniprot.org/uniprot}accession")
        if accession is not None:
            data["Primary Accession"] = accession.text

        # Recommended Protein Name
        protein = entry.find(".//{http://uniprot.org/uniprot}recommendedName/{http://uniprot.org/uniprot}fullName")
        if protein is not None:
            data["Recommended Protein Name"] = protein.text

        # Primary Gene Name
        gene = entry.find(".//{http://uniprot.org/uniprot}gene/{http://uniprot.org/uniprot}name[@type='primary']")
        if gene is not None:
            data["Primary Gene Name"] = gene.text

        # Species Common Name
        organism = entry.find(".//{http://uniprot.org/uniprot}organism/{http://uniprot.org/uniprot}name[@type='common']")
        if organism is not None:
            data["Species Common Name"] = organism.text

        # STRING dbReference
        string_ref = entry.find(".//{http://uniprot.org/uniprot}dbReference[@type='STRING']")
        if string_ref is not None:
            data["STRING dbReference"] = string_ref.get("id")

        # OpenTargets dbReference
        opentargets_ref = entry.find(".//{http://uniprot.org/uniprot}dbReference[@type='OpenTargets']")
        if opentargets_ref is not None:
            data["OpenTargets dbReference"] = opentargets_ref.get("id")

        # Sequence Length and Mass
        sequence = entry.find("{http://uniprot.org/uniprot}sequence")
        if sequence is not None:
            data["Sequence Length"] = sequence.get("length")
            data["Sequence Mass"] = sequence.get("mass")

        # Yield the collected data
        yield data

        # Clear element to save memory
        entry.clear()
        while entry.getprevious() is not None:
            del entry.getparent()[0]

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
    data_list = []
    entry_limit = 5  # Limit to the first 5 entries for testing
    count = 0
    
    for entry_data in parse_xml(xml_content):
        data_list.append(entry_data)
        count += 1
        if count >= entry_limit:
            break  # Stop after the first 5 entries
    
    # Convert the data to a pandas DataFrame and display it in tabular format
    df = pd.DataFrame(data_list)
    print(df)

if __name__ == "__main__":
    main()
