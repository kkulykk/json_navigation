import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json_navigation",
    version="0.0.1",
    author="Roman Kulyk",
    author_email="roman.kulykk@ucu.edu.ua",
    description="lab 3 task 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkulykk/json_navigation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
