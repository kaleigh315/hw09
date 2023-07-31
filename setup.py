from distutils.core import setup
setup(
    name='mypackagedir',
    version='1.0.0',
    url='https://github.com/kaleigh315/mypackage',
    author='Kaleigh OHara',
    author_email='ear3cg@virginia.edu',
    description='Description of my package',
    license='MIT',
    packages=['M09'],    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)