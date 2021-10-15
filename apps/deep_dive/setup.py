from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in deep_dive/__init__.py
from deep_dive import __version__ as version

setup(
	name="deep_dive",
	version=version,
	description="It\'s an app for exploring the doctype in details",
	author="Aasif Patel",
	author_email="patelasif52@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
