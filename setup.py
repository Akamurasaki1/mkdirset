from setuptools import setup, find_packages

setup(
    name='mkdirset',
    version='0.1.0',
    description='A CLI tool to create/display directory structures from text files',
    author='Akamurasaki1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'mkdirset=mkdirset.cli:main',
        ],
    },
    python_requires='>=3.6',
)
