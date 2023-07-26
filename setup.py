from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in czech_exchange_rate/__init__.py
from czech_exchange_rate import __version__ as version

setup(
	name="czech_exchange_rate",
	version=version,
	description="Fetching Exchange Rate From Czech Bank",
	author="SDI Gifts",
	author_email="sdigifts@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
