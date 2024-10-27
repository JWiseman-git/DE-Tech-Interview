import urllib.request
# urllib.request.urlretrieve('https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml', 'Uniprot.xml')

def report_hook(block_num, block_size, total_size):
    downloaded = block_num * block_size
    percentage = downloaded / total_size * 100
    print(f'Downloaded {downloaded} of {total_size} bytes ({percentage:.2f}%)', end='\r')

# Retrieve the file with progress reporting
urllib.request.urlretrieve('https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml', 'Uniprot.xml', reporthook=report_hook)
print() 