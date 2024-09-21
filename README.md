# Pliers

Pliers is a Python tool that helps you combine multiple `.cbz` (comic book archive) files into a single file.
- **CBZ to ZIP Conversion**: Automatically converts `.cbz` files into `.zip` files for easier processing.
- **ZIP Extraction**: Extracts the content of each `.zip` file into an output directory.
- **JPG Renaming**: Renames `.jpg` or `.png` files inside the extracted directories to create a continuous numbering scheme across chapters.
- **XML Modification**: Edits the `ComicInfo.xml` file to update the title and series name as well as correct the page count.
- **Final CBZ Creation**: Recreates a `.cbz` file from the processed chapters and images.

## Installation

You will be able to install Pliers directly from PyPI:

```bash
pip install pliers