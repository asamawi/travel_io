from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in travel_io/__init__.py
from travel_io import __version__ as version

setup(
	name="travel_io",
	version=version,
	description="Travel and Tourism Managment ",
	author="Ahmad Samawi",
	author_email="asamawi@n4s-solutions.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
