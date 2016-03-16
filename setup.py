from setuptools import setup, find_packages

setup(
    name="anviluplinkimproc",
    version="0.0.1",
    author="Rich Wareham",

    packages=find_packages(),
    install_requires=[
        "numpy", "imageio", "anvil-uplink", "docopt"
    ],

    entry_points={
        "console_scripts": [
            "anvil-uplink-improc=anviluplinkimproc.uplink:main",
        ],
    },
)
