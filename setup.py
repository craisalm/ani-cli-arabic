"""Setup configuration for ani-cli-arabic package."""

from setuptools import setup, find_packages
import os

# Read the long description from README if it exists
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

# Read requirements from requirements.txt if it exists
requirements = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt", "r", encoding="utf-8") as f:
        requirements = [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

setup(
    name="ani-cli-arabic",
    version="1.0.0",
    # Forked from np4abdou1/ani-cli-arabic for personal use
    author="np4abdou1",
    author_email="",
    description="A CLI tool to browse and watch Arabic-dubbed anime from the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/np4abdou1/ani-cli-arabic",
    project_urls={
        "Bug Tracker": "https://github.com/np4abdou1/ani-cli-arabic/issues",
        "Contributing": "https://github.com/np4abdou1/ani-cli-arabic/blob/main/.github/CONTRIBUTING.md",
    },
    packages=find_packages(exclude=["tests*", "docs*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Multimedia :: Video",
        "Natural Language :: Arabic",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ani-cli-arabic=ani_cli_arabic.__main__:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
