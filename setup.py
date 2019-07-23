#!/usr/bin/python3
import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='winterboot',  
     version='0.6',
     author="Arpad Magosanyi",
     author_email="mag@kodekonveyor.com",
     description="Winterboot is not SpringBoot",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/kode-konveyor/winterboot",
     package_dir = {'': 'src'},
     packages=['winterboot'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
         "Operating System :: OS Independent",
     ],

 )
