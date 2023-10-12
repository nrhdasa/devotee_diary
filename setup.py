from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in devotee_diary/__init__.py
from devotee_diary import __version__ as version

setup(
	name="devotee_diary",
	version=version,
	description="Maintains all round information of a Temple Devotee",
	author="Narahari Dasa",
	author_email="nrhdasa@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
