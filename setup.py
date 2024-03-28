import os
import platform
import setuptools

__version__ = "0.1.0"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


requirements = []
setup_requirements = []
test_requirements = []

setuptools.setup(
    name="pdfBundle",
    version=__version__,
    author="Ozer Ozdal",
    author_email="ozerozdal@gmail.com",
    description="Package for Pdf Embeddings",
    url="https://github.com/oozdal/pdf-bundle",
    project_urls={
        "Bug Tracker": "https://github.com/oozdal/pdf-bundle/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires="==3.10.10",
    include_package_data=True,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
)