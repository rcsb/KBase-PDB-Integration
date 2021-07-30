#!/usr/bin/python3

"""
# Install Python3 packages with:
    pip3 install biopython
    pip3 install elasticsearch

# References:
    - AlphaFold project: https://github.com/deepmind/alphafold

# Code Snippet Attributions:
    - https://stackoverflow.com/a/16696317/5420857
    - https://stackoverflow.com/a/3135079/5420857

# Questions:
    - What ES instance (and index) do we want to index documents to?
    - How should field names be named (and nested)?
"""

import requests
from Bio import PDB
from elasticsearch import Elasticsearch, helpers
import os
import json


def main():
    """
    Main function for extracting all the metadata from a given directory of AlphaFold mmCIF model files,
    and subsequently post that metadata to an Elasticsearch instance.
    """

    alpha_fold_model_directory = './example_model_files'
    # es = Elasticsearch(['localhost:9200'], timeout=1000)
    target_es_index = 'AlphaFold_Models'

    ## Index data using a bulk index request, but posting only a few hundred models at a time

    bulk_index = ""
    bulk_index_counter = 0

    for file in os.listdir(alpha_fold_model_directory):
        if (file.startswith('AF-') and file.endswith('.cif')):
            try:
                filepath = os.path.join(alpha_fold_model_directory, file)
                model_instance = AlphaFoldModel(filepath)
                bulk_index = append_doc_body_to_bulk_index_request(model_instance.mmcif_metadata, bulk_index, target_es_index)
                bulk_index_counter += 1
                if bulk_index_counter == 200:
                    # submit_bulk_index_request(es, bulk_index)
                    bulk_index_counter = 0
                    bulk_index = ""
            except Exception as err:
                print("!!! Exception:", err)

    ## Submit final bulk index register
    # submit_bulk_index_request(es, bulk_index)

    print(bulk_index)



class AlphaFoldModel:
    """
    Class to represent a valid AlphaFold model.

    By default, should be initialized with an AlphaFold model filename/filepath, but can be
    initialized with a Uniprot ID using the '.fromUniprotID()' method. Also can be done with
    a model filename using '.fromModelFile()' (but not necessary to call that method explicitly).
    """
    def __init__(self, alphafold_model_filepath, auto_download=True):
        """
        Initialize a new AlphaFold Model instance from a model's filename/path.

        By default, download the associated mmCIF model file. If you already have the mmCIF file locally,
        initialize with 'auto_download=False'.
        """

        self.alphafold_model_filepath = alphafold_model_filepath
        self.alphafold_model_filename = self.alphafold_model_filepath.split('/')[-1]

        if (self.alphafold_model_filename.startswith('AF-') and self.alphafold_model_filename.endswith('.cif')):
            self.uniprot_id = self.alphafold_model_filename.split('/')[-1].split('-')[1].upper()
        else:
            print("Provided AlphaFold file does not adhere to standard naming scheme--i.e., does not start with 'AF-' or end with '.cif'.")
            return None

        if not os.path.exists(self.alphafold_model_filepath):
            print("Provided AlphaFold filename and/or path does not exist.")

            if auto_download:
                print("Downloading model file automatically...")
                self.download_alphafold_model(self.alphafold_model_filename)
                self.mmcif_metadata = self.extract_alphafold_model_metadata_mmcif(self.alphafold_model_filename)
            else:
                print("Will NOT download model file automatically. Returning None.")
                return None

        else:
            self.mmcif_metadata = self.extract_alphafold_model_metadata_mmcif(self.alphafold_model_filepath)


    @classmethod
    def fromUniprotID(cls, uniprot_id):
        """
        Create an AlphaFoldModel instance from a given Uniprot ID.

        :params uniprot_id:         A UniProt ID as a string.

        :return AlphaFoldModel:     Instantiation of an AlphaFoldModel object.
        """
        uniprot_id_upper = str(uniprot_id).upper()

        ## Check if valid Uniprot ID
        url = "https://www.uniprot.org/uniprot/"+uniprot_id_upper
        response = requests.get(url)
        if response.status_code >= 400:
            print("Provided Uniprot ID '"+uniprot_id_upper+"' does not exist.")
            return None

        ## Check if corresponding AlphaFold entry exists for Uniprot ID
        url = "https://alphafold.ebi.ac.uk/entry/"+uniprot_id_upper
        response = requests.get(url)
        if response.status_code >= 400:
            print("Requested Uniprot ID entry '"+uniprot_id_upper+"' does not have an associated AlphaFold model.")
            return None

        ## If the Uniprot ID passes both above checks, proceed with initializing an instance with the filename
        alphafold_model_filename_mmcif = "AF-"+uniprot_id_upper+"-F1-model_v1.cif"

        return cls(alphafold_model_filename_mmcif)

    @classmethod
    def fromModelFile(cls, alphafold_model_filepath):
        """
        Create an AlphaFoldModel instance from a given mmCIF model file.

        Note that this class method doesn't actually need to be called explicitly, as the default behavior of instantiating a new
        AlphaFoldModel object is to accept the filepath/name in the base class--e.g., just call, AlphaFoldModel('modelfile.cif').

        :params alphafold_model_filepath:   Path to AlphaFold mmCIF model file.

        :return AlphaFoldModel:             Instantiation of an AlphaFoldModel object.
        """
        return cls(alphafold_model_filepath)


    def download_alphafold_model(self, filename):
        """
        Download an AlphaFold model file locally, from: https://alphafold.ebi.ac.uk/

        :params filename:       Filename of the AlphaFold model file to download.
        """
        url = "https://alphafold.ebi.ac.uk/files/"+filename
        # url = "https://alphafold.ebi.ac.uk/files/AF-P0ACR9-F1-model_v1.cif"

        ## Check if corresponding AlphaFold entry exists for Uniprot ID
        response = requests.get(url)
        if response.status_code >= 400:
            print("Requested AlphaFold model file '"+filename+"' does not exist.")
            return None

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        return

    def extract_alphafold_model_metadata_mmcif(self, filepath):
        """
        Return the metadata (or 'doc_body') from an AlphaFold mmCIF model file, which may be appended to a bulk index request.

        :params filepath:     File path of the AlphaFold mmCIF model file to extract metadata from.

        :return metadata:     Dictionary of metadata to index.
        """
        metadata={}

        # float_metadata_tokens_to_extract = ['_ma_qa_metric_local.metric_value']
        # string_metadata_tokens_to_extract = ['_entry.id', '_entity_poly.pdbx_seq_one_letter_code', '_entity_poly.pdbx_seq_one_letter_code_can']

        parser = PDB.MMCIFParser()
        structure = parser.get_structure("", filepath)
        parsed_info = parser._mmcif_dict

        for token in parsed_info:
            if not (token.startswith('_atom_site') or token == 'data_'):   # Exclude all "_atom_site" tokens as well as the first "data_" header that the parser thinks is a token  (e.g., "data_AF-P0ACR9-F1") and ends up splitting up the string into a list of individual characters
                # All token values are by default loaded by the parser as a list of strings, regardless of the actual data type
                # So first check if value can be represented as an integer
                if all(i.isdigit() for i in parsed_info[token]):
                    metadata.update({token: [int(value) for value in parsed_info[token]]})
                else:
                    # Next try to represent it as a float
                    try:
                        metadata.update({token: [float(value) for value in parsed_info[token]]})
                    # Last, it must just be a string
                    except ValueError:
                        metadata.update({token: [value.replace("\n","") for value in parsed_info[token]]})

        # for token in string_metadata_tokens_to_extract:
        #     metadata.update({token: [value.replace("\n","") for value in parsed_info[token]]})
        #
        # for token in float_metadata_tokens_to_extract:
        #     metadata.update({token: [float(value) for value in parsed_info[token]]})

        metadata.update({"Uniprot_ID": self.uniprot_id})

        return metadata


def append_doc_body_to_bulk_index_request(doc_body, bulk_index_request, target_index):
    """
    Append a metadata dictionary (or any "document body") to a growing bulk index request string.

    :params doc_body:             Metadta document body to append to bulk index request, as a dictionary.
    :params bulk_index_request:   Growing bulk index request, as a string of JSONs sepearated by newline characters.
    :params target_index:         ElasticSearch index to post documents to.

    :return bulk_index_request:   The extended bulk index request string.
    """

    doc_target={ "index" : { "_index" : target_index } }

    bulk_index_request += json.dumps(doc_target)+'\n'+json.dumps(doc_body)+'\n'

    return bulk_index_request


def submit_bulk_index_request(es, bulk_index_request):
    """
    Submit a bulk index request string to an Elasticsearch instance.

    :params es:                   ElasticSearch instance/object to connect to.
    :params bulk_index_request:   Bulk index request to submit.
    """

    es.bulk( body=bulk_index_request )

    return


# def compare_one_letter_aa_codes():
#     """
#     Test function to check if any of the AF models have different sequences provided for the "pdbx_seq_one_letter_code" vs the "pdbx_seq_one_letter_code_can".
#     """
#
#     alpha_fold_model_directory = '/Users/dennis/Box/Projects/KBase/AlphaFold_Data/all_data'
#
#     for file in os.listdir(alpha_fold_model_directory):
#         if (file.startswith('AF-') and file.endswith('.cif')):
#             filepath = os.path.join(alpha_fold_model_directory, file)
#             model_instance = AlphaFoldModel(filepath)
#             if model_instance.mmcif_metadata['_entity_poly.pdbx_seq_one_letter_code'] != model_instance.mmcif_metadata['_entity_poly.pdbx_seq_one_letter_code_can']:
#                 print("non-matching one-letter codes for file,", file)



if __name__ == "__main__":
    main()
