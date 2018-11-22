import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="math_lib",
    version="0.0.1",
    author="Sage Khanuja",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sagek21/math_lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6.4",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['math', 'os', 'time', 'matplotlib', 'matplotlib.pyplot', 'numpy', 'mpl_toolkits.mplot3d'],
)
