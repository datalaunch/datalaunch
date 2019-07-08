from setuptools import setup, find_packages
import versioneer

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="datalaunch",
    description="launch your data project into the cloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="cloud deploy data",
    url="https://github.com/datalaunch/datalaunch",
    license="MIT",
    author="Martijn Arts, Andreas Bollig",
    author_email="m.arts@gmx.net, andreas.bollig@gmail.com",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3",
    install_requires=[],
)
