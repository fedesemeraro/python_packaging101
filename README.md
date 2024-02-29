# Python Packaging 101
[![Documentation Status](https://readthedocs.org/projects/packaging101/badge/?version=latest)](https://packaging101.readthedocs.io/en/latest/?badge=latest)

A brief tutorial about tips and tricks for packaging a python gui linked to cpp code, 
and how to release it through conda-forge.


## IDE setup for remote dev on NAS

- Install Visual Studio Code SSH, Python, C++ extensions
- Setup passthrough [HECC Knowledgebase](https://www.nas.nasa.gov/hecc/support/kb/setting-up-ssh-passthrough_232.html) and enable multiplexing
- Connect using: `ssh -XY pfe` and add function to `pfe:$~/.bashrc`:

```bash
gpu() {qsub -X -I -q v100@pbspl4 -l walltime=$2:00:00,select=1:model=sky_gpu:ncpus=16:ngpus=$1:mem=180g,place=vscatter:shared -W group_list=[ADD_GROUP]}
```

- Request node using `gpu 1 24` and add the following in local:$~/.ssh/config

```bash
Host pfe-intgpu
HostName                r101i0n1
ProxyJump               pfe
ForwardAgent            yes
ForwardX11              yes
ControlMaster           auto
ServerAliveInterval     120
ServerAliveCountMax     2
User                    ADD_USERNAME
```

- Connect to node from VS Code (N.B. no internet connection!)
- Request access to [Anaconda Nucleus](https://www.nas.nasa.gov/hecc/support/kb/managing-and-installing-python-packages-in-conda-environments_627.html) to create conda environments on NAS


## Quick Start with: git

Git is a powerful tool for keeping a version control of your package. To create a new repository:

```bash
mkdir python_packaging101
cd python_packaging101
git init
# create necessary files ...
git remote add origin https://github.com/fsemerar/python_packaging101.git
git branch -M main
git status
git add -A
git commit -m 'Initial commit'
git push origin main
```

To clone an existing repository use: `git clone https://github.com/fsemerar/python_packaging101.git`


## Quick Start with: conda

Conda is a package manager that allows you to create independent environments on your system and 
install the dependencies you need (not only python!).

Add the following to your `pfe:$~/.bashrc`: 

```bash
module use -a /swbuild/analytix/tools/modulefiles
module load miniconda3/v4
export CONDA_ENVS_PATH=/nobackup/$USER/.conda/envs
export CONDA_PKGS_DIRS=/nobackup/$USER/.conda/pkgs
conda config --append envs_dirs /nobackup/$USER/.conda/envs
source activate
```

Then you can run this to create and activate the environment:

```bash
conda env create --file environment.yaml 
conda activate packaging101
```

Use `cmd+shift+p` to select the interpreter on VS Code. 


## Python Packaging

### Project file structure:
```
└── 📁packaging101
    └── __init__.py
    └── 📁gui
        └── __init__.py
        └── main.py
        └── main_window.py
    └── 📁utils
        └── __init__.py
        └── fastfactorial.cpp
        └── slowfactorial.py
    setup.py
    environment.yaml
    README.md
    LICENSE
    .gitignore
```

### Installation

We can install the package using: 

```bash
conda activate packaging101
cd packaging101
pip install .
```

We can now use `packaging101` both calling the gui from the terminal directly or by importing it as a python package.
To test the code we can use the test.ipynb notebook from within VS Code.

### Documentation

Here is the docs (sphinx) file structure to be built on [readthedocs](https://readthedocs.org/):
```
└── 📁docs
    └── Makefile
    └── 📁source
        └── conf.py
        └── index.md
        └── 📁placeholders
        └── 📁template
    └── sphinx_env.yml
    .readthedocs.yml
```

## Release on conda-forge

- Fork [staged-recipes](https://github.com/conda-forge/staged-recipes) repo
- Create recipe by create a [new folder](https://github.com/fsemerar/staged-recipes/tree/packaging101/recipes)
- Create a tag to your package and update the url field in the meta.yaml (need a link to the .tar.gz)
- Update sha256 field in meta.yaml (run: `curl -sL https://github.com/username/reponame/archive/vX.X.X.tar.gz | openssl sha256`)
- Open Pull Request (PR) between your fork and conda-forge's staged-recipes --> builds package on Azure Pipelines
- Once build successfull, ping the conda-forge developers for a review
