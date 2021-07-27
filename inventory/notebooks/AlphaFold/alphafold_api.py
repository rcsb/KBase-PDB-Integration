#!/usr/local/bin/python3

"""
On server use:
#!/usr/bin/python3

# Install package with:
pip3 install biopython

# References:

Code based on source code here: https://github.com/deepmind/alphafold/blob/main/alphafold/data/mmcif_parsing.py
     from: https://github.com/deepmind/alphafold
"""

import requests
from Bio import PDB

class AlphaFoldModel:
    """
    Class to represent a valid Uniprot entry that has an associated AlphaFold model.

    Initialize an instance with a Uniprot ID.
    """
    def __init__(self, uniprot_id):
        self.uniprot_id = str(uniprot_id).upper()
        self.valid_uniprot_id = self.check_uniprot_id()
        self.alphafold_model_exists = self.check_alphafold_entry()
        self.alphafold_model_filename_mmcif = "AF-"+self.uniprot_id+"-F1-model_v1.cif"
        self.alphafold_model_filename_pdb = "AF-"+self.uniprot_id+"-F1-model_v1.pdb"

        if not self.valid_uniprot_id:
            print("Provided Uniprot ID '"+self.uniprot_id+"' does not exist.")
            return None

        if not self.alphafold_model_exists:
            print("Requested Uniprot ID entry '"+self.uniprot_id+"' does not have an associated AlphaFold model.")
            return None

        # Download mmCIF model file
        self.download_alphafold_model(self.alphafold_model_filename_mmcif)
        self.mmcif_metadata = self.extract_alphafold_model_metadata_mmcif(self.alphafold_model_filename_mmcif)

        # Download PDB model file
        self.download_alphafold_model(self.alphafold_model_filename_pdb)



    def check_uniprot_id(self):
        url = "https://www.uniprot.org/uniprot/"+self.uniprot_id
        response = requests.get(url)

        if response.status_code >= 400:
            return False
        return True

    def check_alphafold_entry(self):
        url = "https://alphafold.ebi.ac.uk/entry/"+self.uniprot_id
        response = requests.get(url)

        if response.status_code >= 400:
            return False
        return True

    def download_alphafold_model(self, filename):
        """
        Code help reference: https://stackoverflow.com/a/16696317/5420857
        """
        url = "https://alphafold.ebi.ac.uk/files/"+filename
        # url = "https://alphafold.ebi.ac.uk/files/AF-P0ACR9-F1-model_v1.cif"
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return filename

    def extract_alphafold_model_metadata_mmcif(self, filename):
        metadata={}
        metadata_attributes_to_extract = ['_entry.id', '_entity_poly.pdbx_seq_one_letter_code', '_entity_poly.pdbx_seq_one_letter_code_can', '_ma_qa_metric_local.metric_value']
        parser = PDB.MMCIFParser()
        structure = parser.get_structure("", filename)
        parsed_info = parser._mmcif_dict

        for attribute in metadata_attributes_to_extract:
            metadata.update({attribute: parsed_info[attribute]})

        return metadata


    def index_alphafold_entry_metadata(self, es, metadata):
        """
        :params es:           ElasticSearch instance/object to connect to.
        :params metadata:     Dictionary of metadata to index.
        """
        
        return
