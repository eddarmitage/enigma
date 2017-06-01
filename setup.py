from setuptools import setup
from setuptools import find_packages
setup(
        name='enigma_machine',
        version='0.1dev',
        packages=find_packages('src'),
        package_dir={'':'src'},
        url='http://github.com/eddarmitage/enigma',
        author='Edd Armitage',
        license='MIT'
        )
