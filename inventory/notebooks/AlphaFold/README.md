### Example AlphaFold model mmCIF parsing and attributes

~~~
parser = PDB.MMCIFParser()
structure = parser.get_structure("AF-1","./AF-P0ACR9-F1-model_v1.cif")
parsed_info = parser._mmcif_dict
parsed_info['_ma_qa_metric_local.metric_value']

for k in parsed_info:
    print(k,parsed_info[k])


for k in parsed_info:
    print(k,parsed_info[k])

    data_ AF-P0ACR9-F1
    _entry.id ['AF-P0ACR9-F1']
    _af_target_ref_db_details.gene ['mprA']
    _af_target_ref_db_details.seq_db_sequence_checksum ['BF4D3E34DAD0718A']
    _af_target_ref_db_details.seq_db_sequence_version_date ['2005-11-22']
    _atom_type.symbol ['C', 'N', 'O', 'S']
    _audit_author.name ['Jumper, John', 'Evans, Richard', 'Pritzel, Alexander', 'Green, Tim', 'Figurnov, Michael', 'Ronneberger, Olaf', 'Tunyasuvunakool, Kathryn', 'Bates, Russ', 'Zidek, Augustin', 'Potapenko, Anna', 'Bridgland, Alex', 'Meyer, Clemens', 'Kohl, Simon A. A.', 'Ballard, Andrew J.', 'Cowie, Andrew', 'Romera-Paredes, Bernardino', 'Nikolov, Stanislav', 'Jain, Rishub', 'Adler, Jonas', 'Back, Trevor', 'Petersen, Stig', 'Reiman, David', 'Clancy, Ellen', 'Zielinski, Michal', 'Steinegger, Martin', 'Pacholska, Michalina', 'Berghammer, Tamas', 'Silver, David', 'Vinyals, Oriol', 'Senior, Andrew W.', 'Kavukcuoglu, Koray', 'Kohli, Pushmeet', 'Hassabis, Demis']
    _audit_author.pdbx_ordinal ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']
    _audit_conform.dict_location ['http://mmcif.pdb.org/dictionaries/ascii/mmcif_pdbx.dic']
    _audit_conform.dict_name ['mmcif_pdbx.dic']
    _audit_conform.dict_version ['5.279']
    _chem_comp.formula ['C3 H7 N O2', 'C6 H15 N4 O2', 'C4 H8 N2 O3', 'C4 H7 N O4', 'C3 H7 N O2 S', 'C5 H10 N2 O3', 'C5 H9 N O4', 'C2 H5 N O2', 'C6 H10 N3 O2', 'C6 H13 N O2', 'C6 H13 N O2', 'C6 H15 N2 O2', 'C5 H11 N O2 S', 'C9 H11 N O2', 'C5 H9 N O2', 'C3 H7 N O3', 'C4 H9 N O3', 'C11 H12 N2 O2', 'C9 H11 N O3', 'C5 H11 N O2']
    _chem_comp.formula_weight ['89.093', '175.209', '132.118', '133.103', '121.158', '146.144', '147.129', '75.067', '156.162', '131.173', '131.173', '147.195', '149.211', '165.189', '115.130', '105.093', '119.119', '204.225', '181.189', '117.146']
    _chem_comp.id ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']
    _chem_comp.mon_nstd_flag ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
    _chem_comp.name ['ALANINE', 'ARGININE', 'ASPARAGINE', 'ASPARTIC ACID', 'CYSTEINE', 'GLUTAMINE', 'GLUTAMIC ACID', 'GLYCINE', 'HISTIDINE', 'ISOLEUCINE', 'LEUCINE', 'LYSINE', 'METHIONINE', 'PHENYLALANINE', 'PROLINE', 'SERINE', 'THREONINE', 'TRYPTOPHAN', 'TYROSINE', 'VALINE']
    _chem_comp.pdbx_synonyms ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
    _chem_comp.type ['L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING', 'L-PEPTIDE LINKING']
    _citation.book_publisher ['?']
    _citation.country ['UK']
    _citation.id ['1']
    _citation.journal_full ['Nature']
    _citation.journal_id_ASTM ['NATUAS']
    _citation.journal_id_CSD ['0006']
    _citation.journal_id_ISSN ['0028-0836']
    _citation.journal_volume ['?']
    _citation.page_first ['?']
    _citation.page_last ['?']
    _citation.pdbx_database_id_DOI ['?']
    _citation.pdbx_database_id_PubMed ['?']
    _citation.title ['Highly accurate protein structure prediction with AlphaFold']
    _citation.year ['2021']
    _citation_author.citation_id ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    _citation_author.name ['Jumper, John', 'Evans, Richard', 'Pritzel, Alexander', 'Green, Tim', 'Figurnov, Michael', 'Ronneberger, Olaf', 'Tunyasuvunakool, Kathryn', 'Bates, Russ', 'Zidek, Augustin', 'Potapenko, Anna', 'Bridgland, Alex', 'Meyer, Clemens', 'Kohl, Simon A. A.', 'Ballard, Andrew J.', 'Cowie, Andrew', 'Romera-Paredes, Bernardino', 'Nikolov, Stanislav', 'Jain, Rishub', 'Adler, Jonas', 'Back, Trevor', 'Petersen, Stig', 'Reiman, David', 'Clancy, Ellen', 'Zielinski, Michal', 'Steinegger, Martin', 'Pacholska, Michalina', 'Berghammer, Tamas', 'Silver, David', 'Vinyals, Oriol', 'Senior, Andrew W.', 'Kavukcuoglu, Koray', 'Kohli, Pushmeet', 'Hassabis, Demis']
    _citation_author.ordinal ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']
    _database_2.database_code ['AF-P0ACR9-F1']
    _database_2.database_id ['AF']
    _entity.details ['?']
    _entity.formula_weight ['?']
    _entity.id ['1']
    _entity.pdbx_description ['Transcriptional repressor MprA']
    _entity.pdbx_ec ['?']
    _entity.pdbx_fragment ['?']
    _entity.pdbx_mutation ['?']
    _entity.pdbx_number_of_molecules ['1']
    _entity.src_method ['man']
    _entity.type ['polymer']
    _entity_poly.entity_id ['1']
    _entity_poly.nstd_linkage ['no']
    _entity_poly.nstd_monomer ['no']
    _entity_poly.pdbx_seq_one_letter_code ['MDSSFTPIEQMLKFRASRHEDFPYQEILLTRLCMHMQSKLLENRNKMLKAQGINETLFMALITLESQENHSIQPSELSCA\nLGSSRTNATRIADELEKRGWIERRESDNDRRCLHLQLTEKGHEFLREVLPPQHNCLHQLWSALSTTEKDQLEQITRKLLS\nRLDQMEQDGVVLEAMS']
    _entity_poly.pdbx_seq_one_letter_code_can ['MDSSFTPIEQMLKFRASRHEDFPYQEILLTRLCMHMQSKLLENRNKMLKAQGINETLFMALITLESQENHSIQPSELSCA\nLGSSRTNATRIADELEKRGWIERRESDNDRRCLHLQLTEKGHEFLREVLPPQHNCLHQLWSALSTTEKDQLEQITRKLLS\nRLDQMEQDGVVLEAMS']
    _entity_poly.pdbx_strand_id ['A']
    _entity_poly.type ['polypeptide(L)']
    _entity_poly_seq.entity_id ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    _entity_poly_seq.hetero ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
    _entity_poly_seq.mon_id ['MET', 'ASP', 'SER', 'SER', 'PHE', 'THR', 'PRO', 'ILE', 'GLU', 'GLN', 'MET', 'LEU', 'LYS', 'PHE', 'ARG', 'ALA', 'SER', 'ARG', 'HIS', 'GLU', 'ASP', 'PHE', 'PRO', 'TYR', 'GLN', 'GLU', 'ILE', 'LEU', 'LEU', 'THR', 'ARG', 'LEU', 'CYS', 'MET', 'HIS', 'MET', 'GLN', 'SER', 'LYS', 'LEU', 'LEU', 'GLU', 'ASN', 'ARG', 'ASN', 'LYS', 'MET', 'LEU', 'LYS', 'ALA', 'GLN', 'GLY', 'ILE', 'ASN', 'GLU', 'THR', 'LEU', 'PHE', 'MET', 'ALA', 'LEU', 'ILE', 'THR', 'LEU', 'GLU', 'SER', 'GLN', 'GLU', 'ASN', 'HIS', 'SER', 'ILE', 'GLN', 'PRO', 'SER', 'GLU', 'LEU', 'SER', 'CYS', 'ALA', 'LEU', 'GLY', 'SER', 'SER', 'ARG', 'THR', 'ASN', 'ALA', 'THR', 'ARG', 'ILE', 'ALA', 'ASP', 'GLU', 'LEU', 'GLU', 'LYS', 'ARG', 'GLY', 'TRP', 'ILE', 'GLU', 'ARG', 'ARG', 'GLU', 'SER', 'ASP', 'ASN', 'ASP', 'ARG', 'ARG', 'CYS', 'LEU', 'HIS', 'LEU', 'GLN', 'LEU', 'THR', 'GLU', 'LYS', 'GLY', 'HIS', 'GLU', 'PHE', 'LEU', 'ARG', 'GLU', 'VAL', 'LEU', 'PRO', 'PRO', 'GLN', 'HIS', 'ASN', 'CYS', 'LEU', 'HIS', 'GLN', 'LEU', 'TRP', 'SER', 'ALA', 'LEU', 'SER', 'THR', 'THR', 'GLU', 'LYS', 'ASP', 'GLN', 'LEU', 'GLU', 'GLN', 'ILE', 'THR', 'ARG', 'LYS', 'LEU', 'LEU', 'SER', 'ARG', 'LEU', 'ASP', 'GLN', 'MET', 'GLU', 'GLN', 'ASP', 'GLY', 'VAL', 'VAL', 'LEU', 'GLU', 'ALA', 'MET', 'SER']
    _entity_poly_seq.num ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176']
    _ma_data.content_type ['model coordinates']
    _ma_data.content_type_other_details ['DISCLAIMERS\nALPHAFOLD DATA, COPYRIGHT (2021) DEEPMIND TECHNOLOGIES LIMITED. THE INFORMATION\nPROVIDED IS THEORETICAL MODELLING ONLY AND CAUTION SHOULD BE EXERCISED IN ITS\nUSE. IT IS PROVIDED "AS-IS" WITHOUT ANY WARRANTY OF ANY KIND, WHETHER EXPRESSED\nOR IMPLIED. NO WARRANTY IS GIVEN THAT USE OF THE INFORMATION SHALL NOT INFRINGE\nTHE RIGHTS OF ANY THIRD PARTY. THE INFORMATION IS NOT INTENDED TO BE A\nSUBSTITUTE FOR PROFESSIONAL MEDICAL ADVICE, DIAGNOSIS, OR TREATMENT, AND DOES\nNOT CONSTITUTE MEDICAL OR OTHER PROFESSIONAL ADVICE. IT IS AVAILABLE FOR\nACADEMIC AND COMMERCIAL PURPOSES, UNDER CC-BY 4.0 LICENCE.']
    _ma_data.id ['1']
    _ma_data.name ['Model']
    _ma_model_list.data_id ['1']
    _ma_model_list.model_group_id ['1']
    _ma_model_list.model_group_name ['AlphaFold model']
    _ma_model_list.model_id ['1']
    _ma_model_list.model_name ['Top ranked model']
    _ma_model_list.model_type ['Ab initio model']
    _ma_model_list.ordinal_id ['1']
    _ma_qa_metric.id ['1', '2']
    _ma_qa_metric.mode ['global', 'local']
    _ma_qa_metric.name ['pLDDT', 'pLDDT']
    _ma_qa_metric.software_group_id ['1', '1']
    _ma_qa_metric.type ['other', 'other']
    _ma_qa_metric_global.metric_id ['1']
    _ma_qa_metric_global.metric_value ['90.26']
    _ma_qa_metric_global.model_id ['1']
    _ma_qa_metric_global.ordinal_id ['1']
    _ma_qa_metric_local.label_asym_id ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
    _ma_qa_metric_local.label_comp_id ['MET', 'ASP', 'SER', 'SER', 'PHE', 'THR', 'PRO', 'ILE', 'GLU', 'GLN', 'MET', 'LEU', 'LYS', 'PHE', 'ARG', 'ALA', 'SER', 'ARG', 'HIS', 'GLU', 'ASP', 'PHE', 'PRO', 'TYR', 'GLN', 'GLU', 'ILE', 'LEU', 'LEU', 'THR', 'ARG', 'LEU', 'CYS', 'MET', 'HIS', 'MET', 'GLN', 'SER', 'LYS', 'LEU', 'LEU', 'GLU', 'ASN', 'ARG', 'ASN', 'LYS', 'MET', 'LEU', 'LYS', 'ALA', 'GLN', 'GLY', 'ILE', 'ASN', 'GLU', 'THR', 'LEU', 'PHE', 'MET', 'ALA', 'LEU', 'ILE', 'THR', 'LEU', 'GLU', 'SER', 'GLN', 'GLU', 'ASN', 'HIS', 'SER', 'ILE', 'GLN', 'PRO', 'SER', 'GLU', 'LEU', 'SER', 'CYS', 'ALA', 'LEU', 'GLY', 'SER', 'SER', 'ARG', 'THR', 'ASN', 'ALA', 'THR', 'ARG', 'ILE', 'ALA', 'ASP', 'GLU', 'LEU', 'GLU', 'LYS', 'ARG', 'GLY', 'TRP', 'ILE', 'GLU', 'ARG', 'ARG', 'GLU', 'SER', 'ASP', 'ASN', 'ASP', 'ARG', 'ARG', 'CYS', 'LEU', 'HIS', 'LEU', 'GLN', 'LEU', 'THR', 'GLU', 'LYS', 'GLY', 'HIS', 'GLU', 'PHE', 'LEU', 'ARG', 'GLU', 'VAL', 'LEU', 'PRO', 'PRO', 'GLN', 'HIS', 'ASN', 'CYS', 'LEU', 'HIS', 'GLN', 'LEU', 'TRP', 'SER', 'ALA', 'LEU', 'SER', 'THR', 'THR', 'GLU', 'LYS', 'ASP', 'GLN', 'LEU', 'GLU', 'GLN', 'ILE', 'THR', 'ARG', 'LYS', 'LEU', 'LEU', 'SER', 'ARG', 'LEU', 'ASP', 'GLN', 'MET', 'GLU', 'GLN', 'ASP', 'GLY', 'VAL', 'VAL', 'LEU', 'GLU', 'ALA', 'MET', 'SER']
    _ma_qa_metric_local.label_seq_id ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176']
    _ma_qa_metric_local.metric_id ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
    _ma_qa_metric_local.metric_value ['50.19', '68.78', '82.29', '88.22', '91.68', '91.28', '91.29', '91.45', '92.55', '93.21', '92.83', '93.93', '92.66', '92.66', '92.23', '92.92', '91.92', '92.74', '90.02', '83.80', '89.86', '91.54', '92.92', '94.28', '93.63', '94.69', '94.72', '95.60', '95.31', '94.82', '95.41', '94.50', '94.67', '94.34', '94.01', '93.80', '93.70', '93.90', '93.66', '93.12', '91.87', '93.00', '91.70', '91.04', '92.37', '92.98', '91.91', '93.45', '93.87', '92.91', '92.40', '93.31', '95.02', '93.40', '91.20', '92.76', '94.90', '94.92', '94.12', '95.52', '96.43', '95.70', '95.23', '94.97', '95.17', '93.41', '92.90', '87.57', '89.63', '92.59', '92.15', '92.26', '90.37', '89.59', '88.14', '89.85', '92.11', '90.78', '90.41', '90.66', '90.60', '87.16', '81.70', '82.04', '82.73', '86.65', '88.76', '89.06', '89.71', '92.75', '93.29', '93.77', '94.93', '95.61', '96.51', '96.80', '96.95', '96.45', '97.05', '97.34', '97.09', '96.16', '93.71', '89.12', '81.57', '68.72', '62.79', '63.37', '65.83', '57.97', '63.14', '70.45', '86.54', '91.44', '93.93', '95.39', '96.93', '97.59', '96.83', '97.41', '97.22', '96.41', '97.14', '96.77', '96.52', '95.94', '94.66', '93.95', '94.66', '94.81', '92.09', '91.36', '93.43', '93.94', '91.98', '92.80', '94.13', '94.48', '93.59', '95.28', '96.49', '95.79', '97.22', '97.61', '96.78', '98.15', '98.08', '97.66', '97.63', '97.96', '97.11', '97.52', '97.94', '97.49', '96.27', '96.87', '97.27', '95.66', '94.19', '95.73', '94.63', '92.41', '91.13', '92.05', '91.01', '84.38', '85.69', '86.70', '76.46', '63.78', '60.00', '52.62', '52.81', '59.89', '55.34', '41.04']
    _ma_qa_metric_local.model_id ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    _ma_qa_metric_local.ordinal_id ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    _ma_software_group.group_id ['1']
    _ma_software_group.ordinal_id ['1']
    _ma_software_group.software_id ['1']
    _ma_target_entity.data_id ['1']
    _ma_target_entity.entity_id ['1']
    ...


All Keys:
    _entry.id
    _af_target_ref_db_details.gene
    _af_target_ref_db_details.seq_db_sequence_checksum
    _af_target_ref_db_details.seq_db_sequence_version_date
    _atom_type.symbol
    _audit_author.name
    _audit_author.pdbx_ordinal
    _audit_conform.dict_location
    _audit_conform.dict_name
    _audit_conform.dict_version
    _chem_comp.formula
    _chem_comp.formula_weight
    _chem_comp.id
    _chem_comp.mon_nstd_flag
    _chem_comp.name
    _chem_comp.pdbx_synonyms
    _chem_comp.type
    _citation.book_publisher
    _citation.country
    _citation.id
    _citation.journal_full
    _citation.journal_id_ASTM
    _citation.journal_id_CSD
    _citation.journal_id_ISSN
    _citation.journal_volume
    _citation.page_first
    _citation.page_last
    _citation.pdbx_database_id_DOI
    _citation.pdbx_database_id_PubMed
    _citation.title
    _citation.year
    _citation_author.citation_id
    _citation_author.name
    _citation_author.ordinal
    _database_2.database_code
    _database_2.database_id
    _entity.details
    _entity.formula_weight
    _entity.id
    _entity.pdbx_description
    _entity.pdbx_ec
    _entity.pdbx_fragment
    _entity.pdbx_mutation
    _entity.pdbx_number_of_molecules
    _entity.src_method
    _entity.type
    _entity_poly.entity_id
    _entity_poly.nstd_linkage
    _entity_poly.nstd_monomer
    _entity_poly.pdbx_seq_one_letter_code
    _entity_poly.pdbx_seq_one_letter_code_can
    _entity_poly.pdbx_strand_id
    _entity_poly.type
    _entity_poly_seq.entity_id
    _entity_poly_seq.hetero
    _entity_poly_seq.mon_id
    _entity_poly_seq.num
    _ma_data.content_type
    _ma_data.content_type_other_details
    _ma_data.id
    _ma_data.name
    _ma_model_list.data_id
    _ma_model_list.model_group_id
    _ma_model_list.model_group_name
    _ma_model_list.model_id
    _ma_model_list.model_name
    _ma_model_list.model_type
    _ma_model_list.ordinal_id
    _ma_qa_metric.id
    _ma_qa_metric.mode
    _ma_qa_metric.name
    _ma_qa_metric.software_group_id
    _ma_qa_metric.type
    _ma_qa_metric_global.metric_id
    _ma_qa_metric_global.metric_value
    _ma_qa_metric_global.model_id
    _ma_qa_metric_global.ordinal_id
    _ma_qa_metric_local.label_asym_id
    _ma_qa_metric_local.label_comp_id
    _ma_qa_metric_local.label_seq_id
    _ma_qa_metric_local.metric_id
    _ma_qa_metric_local.metric_value
    _ma_qa_metric_local.model_id
    _ma_qa_metric_local.ordinal_id
    _ma_software_group.group_id
    _ma_software_group.ordinal_id
    _ma_software_group.software_id
    _ma_target_entity.data_id
    _ma_target_entity.entity_id
    _ma_target_entity.origin
    _ma_target_entity_instance.asym_id
    _ma_target_entity_instance.details
    _ma_target_entity_instance.entity_id
    _ma_target_ref_db_details.db_accession
    _ma_target_ref_db_details.db_code
    _ma_target_ref_db_details.db_name
    _ma_target_ref_db_details.ncbi_taxonomy_id
    _ma_target_ref_db_details.organism_scientific
    _ma_target_ref_db_details.seq_db_align_begin
    _ma_target_ref_db_details.seq_db_align_end
    _ma_target_ref_db_details.seq_db_isoform
    _ma_target_ref_db_details.target_entity_id
    _pdbx_audit_revision_details.data_content_type
    _pdbx_audit_revision_details.description
    _pdbx_audit_revision_details.ordinal
    _pdbx_audit_revision_details.provider
    _pdbx_audit_revision_details.revision_ordinal
    _pdbx_audit_revision_details.type
    _pdbx_audit_revision_history.data_content_type
    _pdbx_audit_revision_history.major_revision
    _pdbx_audit_revision_history.minor_revision
    _pdbx_audit_revision_history.ordinal
    _pdbx_audit_revision_history.revision_date
    _pdbx_database_status.entry_id
    _pdbx_database_status.recvd_initial_deposition_date
    _pdbx_database_status.status_code
    _pdbx_poly_seq_scheme.asym_id
    _pdbx_poly_seq_scheme.auth_seq_num
    _pdbx_poly_seq_scheme.entity_id
    _pdbx_poly_seq_scheme.hetero
    _pdbx_poly_seq_scheme.mon_id
    _pdbx_poly_seq_scheme.pdb_ins_code
    _pdbx_poly_seq_scheme.pdb_strand_id
    _pdbx_poly_seq_scheme.seq_id
    _software.classification
    _software.date
    _software.description
    _software.name
    _software.pdbx_ordinal
    _software.type
    _software.version
    _struct_asym.entity_id
    _struct_asym.id
    _struct_conf.beg_auth_asym_id
    _struct_conf.beg_auth_comp_id
    _struct_conf.beg_auth_seq_id
    _struct_conf.beg_label_asym_id
    _struct_conf.beg_label_comp_id
    _struct_conf.beg_label_seq_id
    _struct_conf.conf_type_id
    _struct_conf.end_auth_asym_id
    _struct_conf.end_auth_comp_id
    _struct_conf.end_auth_seq_id
    _struct_conf.end_label_asym_id
    _struct_conf.end_label_comp_id
    _struct_conf.end_label_seq_id
    _struct_conf.id
    _struct_conf.pdbx_beg_PDB_ins_code
    _struct_conf.pdbx_end_PDB_ins_code
    _struct_conf_type.criteria
    _struct_conf_type.id
    _struct_ref.db_code
    _struct_ref.db_name
    _struct_ref.entity_id
    _struct_ref.id
    _struct_ref.pdbx_align_begin
    _struct_ref.pdbx_db_accession
    _struct_ref.pdbx_db_isoform
    _struct_ref.pdbx_seq_one_letter_code
    _struct_ref_seq.align_id
    _struct_ref_seq.db_align_beg
    _struct_ref_seq.db_align_end
    _struct_ref_seq.pdbx_PDB_id_code
    _struct_ref_seq.pdbx_auth_seq_align_beg
    _struct_ref_seq.pdbx_auth_seq_align_end
    _struct_ref_seq.pdbx_db_accession
    _struct_ref_seq.pdbx_db_align_beg_ins_code
    _struct_ref_seq.pdbx_db_align_end_ins_code
    _struct_ref_seq.pdbx_seq_align_beg_ins_code
    _struct_ref_seq.pdbx_seq_align_end_ins_code
    _struct_ref_seq.pdbx_strand_id
    _struct_ref_seq.ref_id
    _struct_ref_seq.seq_align_beg
    _struct_ref_seq.seq_align_end
    _atom_site.group_PDB
    _atom_site.id
    _atom_site.type_symbol
    _atom_site.label_atom_id
    _atom_site.label_alt_id
    _atom_site.label_comp_id
    _atom_site.label_asym_id
    _atom_site.label_entity_id
    _atom_site.label_seq_id
    _atom_site.pdbx_PDB_ins_code
    _atom_site.Cartn_x
    _atom_site.Cartn_y
    _atom_site.Cartn_z
    _atom_site.occupancy
    _atom_site.B_iso_or_equiv
    _atom_site.pdbx_formal_charge
    _atom_site.auth_seq_id
    _atom_site.auth_comp_id
    _atom_site.auth_asym_id
    _atom_site.auth_atom_id
    _atom_site.pdbx_PDB_model_num
    _atom_site.pdbx_sifts_xref_db_acc
    _atom_site.pdbx_sifts_xref_db_name
    _atom_site.pdbx_sifts_xref_db_num
    _atom_site.pdbx_sifts_xref_db_res

~~~
