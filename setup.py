from pathlib import Path

from setuptools import setup, find_packages

root = Path(__file__).parent

with open(root / "README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("cfpq_data/__init__.py") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.strip().split()[-1][1:-1]
            break

name = "cfpq_data"

description = (
    "Python package containing Graphs and Grammars "
    + "for experimental analysis of Context-Free Path Querying algorithms"
)

authors = {
    "vdshk": ("Vadim Abzalov", "vadim.i.abzalov@gmail.com"),
    "Yakonick": ("Nikita Kovalev", "Nikitoskova123@gmail.com"),
}

url = "https://jetbrains-research.github.io/CFPQ_Data/"

project_urls = {
    "Documentation": "https://jetbrains-research.github.io/CFPQ_Data",
    "Source Code": "https://github.com/JetBrains-Research/CFPQ_Data",
    "Bug Tracker": "https://github.com/JetBrains-Research/CFPQ_Data/issues",
}

platforms = ["Linux", "Mac OSX", "Unix", "Windows"]

keywords = ["graphs", "grammars", "context-free", "path-query", "cfpq-data"]

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Education",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS",
    "Operating System :: Unix",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Topic :: Scientific/Engineering :: Information Analysis",
]


def parse_requirements_file(filename):
    with open(filename) as fid:
        requires = [l.strip() for l in fid.readlines() if not l.startswith("#")]

    return requires


install_requires = parse_requirements_file("requirements/default.txt")
extras_require = {
    dep: parse_requirements_file("requirements/" + dep + ".txt")
    for dep in ["developer", "docs", "tests"]
}

if __name__ == "__main__":
    setup(
        name="cfpq_data",
        description=description,
        long_description=long_description,
        author=authors["vdshk"][0],
        author_email=authors["vdshk"][1],
        maintainer=authors["Yakonick"][0],
        maintainer_email=authors["Yakonick"][1],
        version=version,
        keywords=keywords,
        packages=find_packages(),
        platforms=platforms,
        url=url,
        project_urls=project_urls,
        classifiers=classifiers,
        install_requires=install_requires,
        extras_require=extras_require,
        python_requires=">=3.7",
        zip_safe=False,
    )
