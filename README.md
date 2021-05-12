# KBase-PDB-Integration


A python codebase for developing data and software infrastructure needed to bridge KBase and PDB together, enabling bidirectional exchange of data between PDB and KBase.


## Installations

- **Anaconda**
-[Follow guidelines for installations here](https://www.anaconda.com/products/individual).
-Verify installation by typing: `conda --version`
-Installation is successful if you get a version number (specific number doesn't matter). If you get an error like command not found, you will need some additional configurations.

- **Python**
-Python is automatically installed with anaconda.
-Verify the version by typing: `python --version`

- **Virtual Environment**
- Create a virtual environment: `conda create -n <env_name> python=<latest_version>`
- To activate environment: `conda activate <env_name>`

- **Libraries/modules**
Activate your environment and install the following on your CLI: `conda install -c anaconda nb_conda_kernels`
Type y when prompted.
Your installation is successful if you see "done" at the end of log.
`pip install pandas, json, requests, beautifulsoup4`

- **Jupyter notebook**
Open Anaconda navigator and install jupyter notebook

- **To run notebooks locally**
Clone the repo
Navigate to the directory where it is cloned
In the terminal run `jupyter notebook` to launch notebook
Set your kernel to the virtual environment you created 
Now you should be able to run jupyter notebooks above

