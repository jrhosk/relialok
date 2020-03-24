import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="relialok",
    version="0.1.1",
    author="Joshua Hoskins",
    author_email="jhoskins@jlab.org",
    description="A front-end GUI for the Relialok interlocking system in use at Fermi National Accelerator Laboratory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jrhosk/relialok",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)