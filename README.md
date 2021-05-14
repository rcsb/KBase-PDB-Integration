# KBase-PDB-Integration

A python codebase for developing data and software infrastructure needed to bridge KBase and PDB together, enabling bidirectional exchange of data between PDB and KBase. This repo has files related to data access protocols in resources serving structural data. To run the files locally, follow the installation instructions to set up the required environment, clone the repo and run the jupyter notebook in the inventory/notebook directory. Each notebook corresponds to data access protocols in different resource. The resources that have been documented here are: The Swiss Model Repository (SMR), ModBase, Interactome3D, ModelArchive. 

## Installations

1. **Anaconda**
- [Follow guidelines for installations here](https://www.anaconda.com/products/individual).
- Verify installation by typing: `conda --version`
- Installation is successful if you get a version number (specific number doesn't matter). If you get an error like command not found, you will need some additional configurations.

2. **Python**
- Python is automatically installed with anaconda.
- Verify the version by typing: `python --version`

3. **Virtual Environment**
- Create a virtual environment: `conda create -n <env_name> python=<latest_version>`
- To activate environment: `conda activate <env_name>`

4. **Libraries/modules**
- Activate your environment and install the following on your CLI: `conda install -c anaconda nb_conda_kernels`
- Type y when prompted.Installation is successful if you see "done" at the end of log.
- `pip install pandas, json, requests, beautifulsoup4, biopython`

5. **Jupyter notebook**
Open Anaconda navigator and install jupyter notebook 

6. **To run notebooks locally**
- Clone the repo
- Navigate to the directory where it is cloned
- In the terminal run `jupyter notebook` to launch notebook
- Set your kernel to the virtual environment you created. Now you should be able to run jupyter notebooks above

