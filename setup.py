from setuptools import setup, find_packages
import os
import sys

directory = os.path.abspath(os.path.dirname(__file__))
if sys.version_info >= (3, 0):
    with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
else:
    with open(os.path.join(directory, 'README.md')) as f:
        long_description = f.read()

setup(name='BanDiTS',
      packages=find_packages(),
      include_package_data=True,
      setup_requires=['setuptools_scm'],
      use_scm_version=True,
      description='A Python module for time series analysis',
      classifiers=[
          'License :: FSF Approved :: WTFPL License',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
      ],
      install_requires=["fiona",
                        'scipy',
                        'rasterio',
                        'pathos>=0.2',
                        'numpy'],
      python_requires='>=3.6.0',
      url='https://github.com/marlinmm/BanDiTS.git',
      author='Marlin Mueller', #'Jonas Ziemer'  # how to add second author?
      author_email='marlin.markus.mueller@uni-jena.de',
      license='WTFPL',
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown')
