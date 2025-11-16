"""
Setup script for Handwritten Text to Digital Text Converter
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r") as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return requirements

setup(
    name="handwritten-text-converter",
    version="1.0.0",
    author="Raiyan",
    author_email="",
    description="Convert handwritten text images to digital text using ML techniques",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/handwritten-to-digital-text",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "handwritten-converter=main:main",
        ],
    },
    keywords="ocr, handwriting, computer-vision, machine-learning, text-recognition",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/handwritten-to-digital-text/issues",
        "Source": "https://github.com/yourusername/handwritten-to-digital-text",
        "Documentation": "https://github.com/yourusername/handwritten-to-digital-text#readme",
    },
)