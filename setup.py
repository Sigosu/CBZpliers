from setuptools import setup, find_packages

setup(
    name="pliers",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "lxml",          # List of dependencies
        "setuptools",
    ],
    entry_points={
        'console_scripts': [
            'combine_cbz=pliers.main:main',  # Command-line tool configuration
        ],
    },
    author="Szymon Sciegienka",
    author_email="szymon.sciegienka@gmail.com",
    description="A tool to combine multiple .cbz files into one.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pliers",  # Optional GitHub link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",   # Adjust based on your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)