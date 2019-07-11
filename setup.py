from setuptools import setup

requirements = ['pandas', 'numpy', 'geopandas', 'shapely', 'matplotlib', 'urllib', 'zipfile']

setup(
    name='electopy',
    version='0.1dev',
    packages=['electopy',],
    license='GNU General Public License v3.0',
    long_description=open('README.txt').read(),
    install_requires=requirements,
)
