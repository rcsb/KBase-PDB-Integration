#!/usr/bin/python3

"""
# Install Python3 packages with:
    pip3 install biopython
    pip3 install elasticsearch

# References:
    - AlphaFold project: https://github.com/deepmind/alphafold

"""

import requests
from Bio import PDB
from elasticsearch import Elasticsearch, helpers
import os
import json

def main():

    alpha_fold_model_directory = './example_model_files'

    # es = Elasticsearch(['localhost:9200'], timeout=1000)

    bulk_index = ""
    for file in os.listdir(alpha_fold_model_directory):
        if (file.startswith('AF-') and file.endswith('.cif')):
            filepath = os.path.join(alpha_fold_model_directory, file)
            model_instance = AlphaFoldModel(filepath)
            # print(model_instance.mmcif_metadata)
            bulk_index = append_doc_body_to_bulk_index_request(model_instance.mmcif_metadata, bulk_index, "AlphaFold_Models")

    print(bulk_index)


class AlphaFoldModel:
    """
    Class to represent a valid AlphaFold model.

    By default, should be initialized with an AlphaFold model filename/filepath, but can be
    initialized with a Uniprot ID using the '.fromUniprotID()' method. Also can be done with
    a model filename using '.fromModelFile()' (but not necessary to call that method explicitly).

    Code help from: https://stackoverflow.com/a/3135079/5420857
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
        Create an AlphaFold Model instance from a given Uniprot ID.
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
        return cls(alphafold_model_filepath)


    def download_alphafold_model(self, filename):
        """
        Code help reference: https://stackoverflow.com/a/16696317/5420857
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
        return filename

    def extract_alphafold_model_metadata_mmcif(self, filepath):
        """
        Return the metadata (or 'doc_body') for the AlphaFold entry to append to a bulk index request.

        :return metadata:     Dictionary of metadata to index.
        """
        metadata={}
        # string_metadata_attributes_to_extract = ['_entry.id', '_entity_poly.pdbx_seq_one_letter_code', '_entity_poly.pdbx_seq_one_letter_code_can']
        string_metadata_attributes_to_extract = [
                '_entry.id',
                '_af_target_ref_db_details.gene',
                '_af_target_ref_db_details.seq_db_sequence_checksum',
                '_af_target_ref_db_details.seq_db_sequence_version_date',
                '_atom_type.symbol',
                '_audit_author.name',
                '_audit_author.pdbx_ordinal',
                '_audit_conform.dict_location',
                '_audit_conform.dict_name',
                '_audit_conform.dict_version',
                '_chem_comp.formula',
                '_chem_comp.formula_weight',
                '_chem_comp.id',
                '_chem_comp.mon_nstd_flag',
                '_chem_comp.name',
                '_chem_comp.pdbx_synonyms',
                '_chem_comp.type',
                '_citation.book_publisher',
                '_citation.country',
                '_citation.id',
                '_citation.journal_full',
                '_citation.journal_id_ASTM',
                '_citation.journal_id_CSD',
                '_citation.journal_id_ISSN',
                '_citation.journal_volume',
                '_citation.page_first',
                '_citation.page_last',
                '_citation.pdbx_database_id_DOI',
                '_citation.pdbx_database_id_PubMed',
                '_citation.title',
                '_citation.year',
                '_citation_author.citation_id',
                '_citation_author.name',
                '_citation_author.ordinal',
                '_database_2.database_code',
                '_database_2.database_id',
                '_entity.details',
                '_entity.formula_weight',
                '_entity.id',
                '_entity.pdbx_description',
                '_entity.pdbx_ec',
                '_entity.pdbx_fragment',
                '_entity.pdbx_mutation',
                '_entity.pdbx_number_of_molecules',
                '_entity.src_method',
                '_entity.type',
                '_entity_poly.entity_id',
                '_entity_poly.nstd_linkage',
                '_entity_poly.nstd_monomer',
                '_entity_poly.pdbx_seq_one_letter_code',
                '_entity_poly.pdbx_seq_one_letter_code_can',
                '_entity_poly.pdbx_strand_id',
                '_entity_poly.type',
                '_entity_poly_seq.entity_id',
                '_entity_poly_seq.hetero',
                '_entity_poly_seq.mon_id',
                '_entity_poly_seq.num',
                '_ma_data.content_type',
                '_ma_data.content_type_other_details',
                '_ma_data.id',
                '_ma_data.name',
                '_ma_model_list.data_id',
                '_ma_model_list.model_group_id',
                '_ma_model_list.model_group_name',
                '_ma_model_list.model_id',
                '_ma_model_list.model_name',
                '_ma_model_list.model_type',
                '_ma_model_list.ordinal_id',
                '_ma_qa_metric.id',
                '_ma_qa_metric.mode',
                '_ma_qa_metric.name',
                '_ma_qa_metric.software_group_id',
                '_ma_qa_metric.type',
                '_ma_qa_metric_global.metric_id',
                '_ma_qa_metric_global.metric_value',
                '_ma_qa_metric_global.model_id',
                '_ma_qa_metric_global.ordinal_id',
                '_ma_qa_metric_local.label_asym_id',
                '_ma_qa_metric_local.label_comp_id',
                '_ma_qa_metric_local.label_seq_id',
                '_ma_qa_metric_local.metric_id',
                '_ma_qa_metric_local.model_id',
                '_ma_qa_metric_local.ordinal_id',
                '_ma_software_group.group_id',
                '_ma_software_group.ordinal_id',
                '_ma_software_group.software_id',
                '_ma_target_entity.data_id',
                '_ma_target_entity.entity_id',
                '_ma_target_entity.origin',
                '_ma_target_entity_instance.asym_id',
                '_ma_target_entity_instance.details',
                '_ma_target_entity_instance.entity_id',
                '_ma_target_ref_db_details.db_accession',
                '_ma_target_ref_db_details.db_code',
                '_ma_target_ref_db_details.db_name',
                '_ma_target_ref_db_details.ncbi_taxonomy_id',
                '_ma_target_ref_db_details.organism_scientific',
                '_ma_target_ref_db_details.seq_db_align_begin',
                '_ma_target_ref_db_details.seq_db_align_end',
                '_ma_target_ref_db_details.seq_db_isoform',
                '_ma_target_ref_db_details.target_entity_id',
                '_pdbx_audit_revision_details.data_content_type',
                '_pdbx_audit_revision_details.description',
                '_pdbx_audit_revision_details.ordinal',
                '_pdbx_audit_revision_details.provider',
                '_pdbx_audit_revision_details.revision_ordinal',
                '_pdbx_audit_revision_details.type',
                '_pdbx_audit_revision_history.data_content_type',
                '_pdbx_audit_revision_history.major_revision',
                '_pdbx_audit_revision_history.minor_revision',
                '_pdbx_audit_revision_history.ordinal',
                '_pdbx_audit_revision_history.revision_date',
                '_pdbx_database_status.entry_id',
                '_pdbx_database_status.recvd_initial_deposition_date',
                '_pdbx_database_status.status_code',
                '_pdbx_poly_seq_scheme.asym_id',
                '_pdbx_poly_seq_scheme.auth_seq_num',
                '_pdbx_poly_seq_scheme.entity_id',
                '_pdbx_poly_seq_scheme.hetero',
                '_pdbx_poly_seq_scheme.mon_id',
                '_pdbx_poly_seq_scheme.pdb_ins_code',
                '_pdbx_poly_seq_scheme.pdb_strand_id',
                '_pdbx_poly_seq_scheme.seq_id',
                '_software.classification',
                '_software.date',
                '_software.description',
                '_software.name',
                '_software.pdbx_ordinal',
                '_software.type',
                '_software.version',
                '_struct_asym.entity_id',
                '_struct_asym.id',
                '_struct_conf.beg_auth_asym_id',
                '_struct_conf.beg_auth_comp_id',
                '_struct_conf.beg_auth_seq_id',
                '_struct_conf.beg_label_asym_id',
                '_struct_conf.beg_label_comp_id',
                '_struct_conf.beg_label_seq_id',
                '_struct_conf.conf_type_id',
                '_struct_conf.end_auth_asym_id',
                '_struct_conf.end_auth_comp_id',
                '_struct_conf.end_auth_seq_id',
                '_struct_conf.end_label_asym_id',
                '_struct_conf.end_label_comp_id',
                '_struct_conf.end_label_seq_id',
                '_struct_conf.id',
                '_struct_conf.pdbx_beg_PDB_ins_code',
                '_struct_conf.pdbx_end_PDB_ins_code',
                '_struct_conf_type.criteria',
                '_struct_conf_type.id',
                '_struct_ref.db_code',
                '_struct_ref.db_name',
                '_struct_ref.entity_id',
                '_struct_ref.id',
                '_struct_ref.pdbx_align_begin',
                '_struct_ref.pdbx_db_accession',
                '_struct_ref.pdbx_db_isoform',
                '_struct_ref.pdbx_seq_one_letter_code',
                '_struct_ref_seq.align_id',
                '_struct_ref_seq.db_align_beg',
                '_struct_ref_seq.db_align_end',
                '_struct_ref_seq.pdbx_PDB_id_code',
                '_struct_ref_seq.pdbx_auth_seq_align_beg',
                '_struct_ref_seq.pdbx_auth_seq_align_end',
                '_struct_ref_seq.pdbx_db_accession',
                '_struct_ref_seq.pdbx_db_align_beg_ins_code',
                '_struct_ref_seq.pdbx_db_align_end_ins_code',
                '_struct_ref_seq.pdbx_seq_align_beg_ins_code',
                '_struct_ref_seq.pdbx_seq_align_end_ins_code',
                '_struct_ref_seq.pdbx_strand_id',
                '_struct_ref_seq.ref_id',
                '_struct_ref_seq.seq_align_beg',
                '_struct_ref_seq.seq_align_end'
        ]

        float_metadata_attributes_to_extract = ['_ma_qa_metric_local.metric_value']

        parser = PDB.MMCIFParser()
        structure = parser.get_structure("", filepath)
        parsed_info = parser._mmcif_dict

        for attribute in string_metadata_attributes_to_extract:
            metadata.update({attribute: [value.replace("\n","") for value in parsed_info[attribute]]})

        for attribute in float_metadata_attributes_to_extract:
            metadata.update({attribute: [float(value) for value in parsed_info[attribute]]})

        metadata.update({"Uniprot_ID": self.uniprot_id})

        return metadata


def append_doc_body_to_bulk_index_request(doc_body, bulk_index_request, target_index):
    """
    :params doc_body:             Document body to append to bulk index request, as a dictionary.
    :params bulk_index_request:   Growing bulk index request, as a string of JSONs sepearated by newline characters.
    :params target_index:         ElasticSearch index to post documents to.
    """

    doc_target={ "index" : { "_index" : target_index } }

    bulk_index_request += json.dumps(doc_target)+'\n'+json.dumps(doc_body)+'\n'

    return bulk_index_request


def submit_bulk_index_request(es, bulk_index_request):
    """
    :params es:                   ElasticSearch instance/object to connect to.
    :params bulk_index_request:   Bulk index request to submit.
    """

    es.bulk( body=bulk_index_request )

    return


if __name__ == "__main__":
    main()
