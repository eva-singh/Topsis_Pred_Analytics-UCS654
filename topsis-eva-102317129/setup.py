from setuptools import setup, find_packages

setup(
    name="topsis-eva-102317129",
    version="1.0.0",
    author="eva",
    description="TOPSIS implementation using Python",
    packages=find_packages(),
    install_requires=["pandas","numpy"],
    entry_points={
        "console_scripts":[
            "topsis=topsis.cli:run"
        ]
    }
)
