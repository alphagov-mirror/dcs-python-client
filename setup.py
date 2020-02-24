import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dcs-client",
    version="0.0.1",
    author="Government Digital Service",
    description="A worked example of how to check passport validity with the Document Checking Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alphagov/dcs-python-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'dcs-client=client.client:main',
            'check-jose=client.check_jose:main'
        ],
    },
    install_requires=[
        'jwcrypto',
        'requests',
        'docopt'
    ]
)
