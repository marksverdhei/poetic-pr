from setuptools import setup

setup(
    name="poetic-pr",
    version="0.0.0",
    description="A command line utlity to enrichen your pull requests",
    packages=["ppr"],
    package_dir={"ppr": "src/ppr"},
    entry_points={
        "console_scripts": ["ppr=ppr.main:main"],
    },
    install_requires=[
        "revChatGPT",
        "argh",
    ],
)
