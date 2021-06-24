from setuptools import setup,find_packages

setup(
        name = 'ServerManager',
        version = '0.1',
        packages = find_packages(),
        author = 'shihua',
        description = 'ServerManager module',
        install_requires = ['paramiko','python-consul','flask','minio']
)