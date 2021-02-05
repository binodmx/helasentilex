import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helasentilex",
    version="0.1.1",
    author="Binod Karunanayake",
    author_email="binod.16@cse.mrt.ac.lk",
    description="Python API for Sinhala Sentiment Lexicon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/binodmx/helasentilex",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
