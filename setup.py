# coding: utf-8
from setuptools import find_packages, setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(name='examplePackage',
      version='0.0.1',
      description='Serialize payload TargetService',
      long_description=open(README).read(),
      long_description_content_type="text/markdown",
      author="William Yizima", author_email="william.yizima@hotmail.com",
      license="MIT",
      keywords=[],
      packages=find_packages(where='.'),
      package_dir={"examplePackage": "examplePackage"},
      zip_safe=True,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: Portuguese',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
          'Topic :: Software Development :: Libraries',
      ],
        install_requires=[
        'azure-functions >= 1.7.0, < 2.0.0',
        'requests'
        # Any additional packages that will be used in your extension
        ],
      url='https://github.com/WilliamYizima/examplePackage/',)
