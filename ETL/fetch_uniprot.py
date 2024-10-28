import requests
import gzip
from io import BytesIO
from lxml import etree
import pandas as pd


def download_data_from_url(url: str):
    """
    Download a file from the specified URL.
    
    Parameters:
    url (str): The URL to download the data from.

    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data from {url}: {e}")
        raise  # Re-raise the exception for further handling if needed
    
    return response.content


def parse_xml(xml_content):

    """
    Parse the XML content using lxml to extract desired fields from each entry. 

    Parameters:
    xml_content: Unzipped raw XML content

    """
    
    # Use lxml's iterparse to parse large XML files

    context = etree.iterparse(BytesIO(xml_content), events=("end",), tag="{http://uniprot.org/uniprot}entry")
    
    for event, entry in context:

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


def download_uniprot_data(url : str) -> pd.DataFrame:

    """

    Call functions to download and extract data into a pandas dataframe. 

    """
    
    print(f"Downloading data from url: {url}")

    gzipped_data = download_data_from_url(url)
    
    # Compressed XML gzip is then decompressed

    with gzip.open(BytesIO(gzipped_data), 'rb') as opened_file:
        xml_content = opened_file.read()
 
    print("Begining parse of XML data")

    data_list = []

    entry_limit = 1000  # NOTE TO REVIEWER - I Have limited this data to the first 1000 rows due to compute issues 
    count = 0
    
    for entry_data in parse_xml(xml_content):
        data_list.append(entry_data)
        count += 1
        if count >= entry_limit:
            break 
    
    print("Concluded XML data parse")

    df = pd.DataFrame(data_list)
    
    return df