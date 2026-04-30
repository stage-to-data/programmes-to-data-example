from setuptools import setup
from setuptools import find_packages

long_description= """
"""

required = [
    "pymupdf",
    "pillow",
    "numpy",
    "opencv-python",
    "vllm"
]

setup(
    name="ptod",
    version="0.0.1",
    description="",
    long_description=long_description,
    author="Jacob Hart",
    author_email="jacob.dchart@gmail.com",
    url="https://github.com/stage-to-data/programmes-to-data-example",
    install_requires=required,
    packages=find_packages()
)