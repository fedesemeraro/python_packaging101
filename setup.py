from setuptools import setup, find_packages
from distutils.extension import Extension

setup(
    name='packaging101',
    version='1.0.0',
    author="Federico Semeraro",
    description="A package to teach how to package.",
    url="https://github.com/fsemerar/python_packaging101",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'packaging101=packaging101.gui.main:main',
        ],
    },
    ext_modules=[
        Extension(
            name='packaging101.utils.fastfactorial',
            sources=['packaging101/utils/fastfactorial.cpp'],
            extra_compile_args=['-std=c++11'],
        )
    ],
)
