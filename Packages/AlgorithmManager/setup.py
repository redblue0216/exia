from setuptools import setup,find_packages

setup(
        name = 'AlgorithmManager',
        version = '0.1',
        packages = find_packages(),
        author = 'shihua',
        description = 'AlgorithmManager module',
        install_requires = ['DataAPI','LogDecoratorEK','ModelLibrary','ModelMonitoring','ServerManager']
)