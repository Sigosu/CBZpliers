# [CBZpliers](https://pypi.org/project/CBZpliers/)

Pliers is a Python tool that helps you combine multiple `.cbz` (comic book archive) files into a single file.

## Installation

You will be able to install Pliers directly from [PyPI](https://pypi.org/project/CBZpliers/):

```bash
pip install CBZpliers
```
## Usage

You can use the tool from command line

```bash
combine_cbz <cbz_dir> <volume_title> <series_title>
```

<cbz_dir> - path to the directory which contains the files you want to combine. It is necessary to have a separate directory, containing nothing BUT the .cbz files. This will also be the output directory.

<volume_title> - name of the final .cbz file. If using ```-m```, this will work more like a naming format, i.e. if you use "vol", then the output files will be called vol1, vol2, vol3... 

<series_title> - name of the series, only shows in the .xml file inside the .cbz archive, but might be useful for some applications

-m (optional flag) - run the script for multiple directories at once, i.e. create a directory, in that directory create a separate directory for every volume, then put the .cbz files respectively into those directories
