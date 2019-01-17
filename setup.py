import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-brihome",
    version="0.0.2",
    author="Julius Hinze",
    author_email="juliusmh@web.de",
    description="A small package to control Brihome smart led bulbs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juliusmh/python-brihome",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pytuya==7.0.2"
    ]
)