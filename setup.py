import setuptools
from io import open


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
                 name="mgemu", # Replace with your own username
                 version="0.0.1",
                 author="Nesar Ramachandra",
                 author_email="nramachandra@anl.gov",
                 description="Gaussian Process Emulator for Modified Gravity power spectra",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/nesar/mgemu",
                 packages=setuptools.find_packages(),
                 classifiers=[
                              "Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent"
                              "Intended Audience :: Science/Research"
                              "Topic :: Scientific/Engineering :: Machine Learning",
                              "Topic :: Scientific/Engineering :: Physics",
                              ],
                 keywords="cosmology machine learning"
                 python_requires='>=3.6',
                 )
