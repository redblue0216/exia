from setuptools import setup,find_packages

setup(
        name = 'ModelLibrary',
        version = '0.1',
        packages = find_packages(),
        author = 'shihua',
        description = 'ModelLibrary module',
        install_requires = ['paramiko','pymongo','dill']
)