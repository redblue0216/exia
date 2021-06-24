from setuptools import setup,find_packages

setup(
        name = 'DataAPI',
        version = '0.1',
        packages = find_packages(),
        author = 'shihua',
        description = 'DataAPI module',
        install_requires = ['pandas','pymysql']
)