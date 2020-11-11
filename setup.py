from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = ["requests", "websockets == 6.0"]

setup(
    name="okex",
    version="1.0.0",
    description="Python client for OKEx API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='OKEx',
    author_email="https://github.com/okex/V3-Open-API-SDK",
    url="https://github.com/devinbarry/okex-client",
    python_requires='>=3.6',
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    keywords=["OpenAPI", "OKEx", "OKEx API"],
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
