"""A setuptools based setup module.
"""

from pathlib import Path
from setuptools import find_packages, setup

here = Path(__file__).parent.absolute()

# Get the long description from the README file
with open(here.joinpath('README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pinar',

    version='3.3.1',

    description='PINAR in Python',

    long_description=long_description,
    long_description_content_type="text/markdown",

    url='https://github.com/MamarezaAlipour/pinar_python',

    author='Mohammadreza Alipour',
    author_email='mamarezaalipour@gmail.com',

    license='OSI Approved :: GNU Lesser General Public License v3 (GPLv3)',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],

    keywords='Pinar',

    packages=find_packages() + ['data'],

    install_requires=[
        'bottleneck',
        'cartopy',
        'cfgrib',
        'contextily',
        'dask',
        'deprecation',
        'geopandas',
        'h5py',
        'haversine',
        'matplotlib',
        'netcdf4',
        'numba',
        'overpy',
        'pandas',
        'pandas-datareader',
        'pathos',
        'peewee',
        'pillow',
        'pint',
        'pybufrkit',
        'pycountry',
        'rasterio',
        'salib',
        'scikit-learn',
        'statsmodels',
        'sparse',
        'tables',
        'tabulate',
        'tqdm',
        'xarray',
        'xlrd',
        'xlsxwriter',
        'xmlrunner'
    ],

    include_package_data=True
)
