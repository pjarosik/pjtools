import setuptools

version_namespace = {}
with open("pjtools/version.py") as f:
    exec(f.read(), version_namespace)


setuptools.setup(
    name="pjtools",
    version=version_namespace["__version__"],
    author="pjtools",
    author_email="jarosik.piotr@gmail.com",
    description="pjtools",
    long_description="pjtools",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=[]),
    classifiers=[
        "Development Status :: 1 - Planning",

        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",

        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps."
    ],
    install_requires=[
        "matplotlib>=3.3.0"
    ],
    python_requires='>=3.7'
)
