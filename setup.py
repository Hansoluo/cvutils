'''
Author: shy
Description: 
LastEditTime: 2020-12-11 17:23:43
'''
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="just_utils",
	version="0.1",
	author="Hansoluo",
	author_email="hansoluo757@gmail.com",
	description="A series of convenience functions to help training large image dataset with CNN",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Hansoluo/cvutils.git",
	packages=['just_utils'],
	install_requires=['pathlib', 'numpy'],
	classifiers=(
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
	),
)