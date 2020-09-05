from glob import glob
from os.path import basename, splitext
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
        name="tx-functional",
        version="0.1.2",
        license="MIT",
        author="Hao Xu",
        author_email="xuhao@renci.org",
        description="A pickleable generic functional programming library",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/RENCI/tx-functional",
        packages=setuptools.find_namespace_packages("src", exclude=["tests", "tests.*"]),
        package_dir={
            "": "src"
        },
        py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
        install_requires=[
        ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )
    
