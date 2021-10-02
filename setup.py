import pathlib
from setuptools import setup, find_packages
HERE = pathlib.Path(__file__).parent
VERSION = '0.0.1'
PACKAGE_NAME = 'EDA'
AUTHOR = 'Sumayyah Taiwo'
AUTHOR_EMAIL = 'sumty4deen@gmail.com'
URL = 'https://github.com/Sumta4real/ExploratoryDataAnalysis'
LICENSE = 'MIT'
DESCRIPTION = 'A package that performs Exploratory Data Analysis'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = [
      'numpy',
      'pandas'
      'matplotlib'
      'seaborn'
      'scipy'
]
setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
