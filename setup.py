#!/usr/bin/env python

""" Setup for da_controller """

from glob import glob
from os.path import basename, dirname, realpath

from setuptools import find_packages, setup


def main():
    return setup(
        author="Sijin Zhang",
        author_email="sijin.zhang@esr.cri.nz",
        # data_files=[("var_blending/etc", glob("etc/*"))],
        description="to be added",
        maintainer="ESR data science group",
        maintainer_email="sijin.zhang@esr.cri.nz",
        # Use name of the directory as name
        name=basename(dirname(realpath(__file__))),
        scripts=["cli/cli_data.py"],
        packages=find_packages(),
        zip_safe=False,
    )


if __name__ == "__main__":
    main()
