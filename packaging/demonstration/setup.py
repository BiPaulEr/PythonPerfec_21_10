from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="EducTools",
    version="0.1",
    packages=find_packages(),
    install_requires=["numpy", "click"],
    entry_points={
        "console_scripts":["math=eductools_cli.math_tools_cli:calcul_cli"]
    },
    extras_requires={
        "dev":["pytest"]
    }
    )