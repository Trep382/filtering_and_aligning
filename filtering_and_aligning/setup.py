import os

from setuptools import find_packages, setup

with open(os.path.join("version.txt"), "r") as file_handler:
    __version__ = file_handler.read().strip()

long_description = """

# MPC Baselines

This repository has the code for bag filtering

## Links

Repository:
https://github.com/Trep382/bag_filtering


"""
setup(
    name="filtering_and_aligning",
    packages=[
        package
        for package in find_packages()
        if package.startswith("filtering_and_aligning")
    ],
    package_data={"filtering_and_aligning": ["py.typed", "version.txt"]},
    install_requires=[
        "numpy",
        # For reading logs
        "pandas",
        # Plotting learning curves
        "matplotlib",
        # for reading rosbags
        "rosbag2_py",
        "nav_msgs",
        "people_msgs",
        "tf2_msgs",
        "sensor_msgs",
        "rliable",
    ],
    extras_require={
        "tests": [
            # Run tests and coverage
            "pytest",
            "pytest-cov",
            "pytest-env",
            "pytest-xdist",
            # Type check
            "mypy",
            # Lint code and sort imports (flake8 and isort replacement)
            "ruff>=0.3.1",
            # Reformat
            "black>=24.2.0,<25",
        ],
        # "docs": [
        #     "sphinx>=5,<8",
        #     "sphinx-autobuild",
        #     "sphinx-rtd-theme>=1.3.0",
        #     # For spelling
        #     "sphinxcontrib.spelling",
        #     # Copy button for code snippets
        #     "sphinx_copybutton",
        # ],
    },
    description="Filtering and aligning data bags",
    author="Stefano Trepella",
    url="https://github.com/Trep382/filtering_and_aligning_data_bags",
    author_email="stefano.trepella@polito.it",
    keywords="filtering ros2 data-alignment",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,
    python_requires=">=3.8",
    # PyPI package information.
    project_urls={
        "Code": "https://github.com/Trep382/filtering_and_aligning_data_bags",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)

# python setup.py sdist
# python setup.py bdist_wheel
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# twine upload dist/*
