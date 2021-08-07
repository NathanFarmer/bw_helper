import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitwarden-helper",
    version="0.0.1",
    author="Nathan Farmer",
    author_email="jnathanfarmer@gmail.com",
    description="A simple Python package for interacting with the Bitwarden CLI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NathanFarmer/bw_helper",
    project_urls={
        "Bug Tracker": "https://github.com/NathanFarmer/bw_helper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
