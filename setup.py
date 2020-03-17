from setuptools import setup


requires = ["chardet>=3.0.4", "pandas>=1.0.2", "xlrd>=1.2.0"]


setup(
    name='ckanreader',
    version='0.1',
    description='CKANのWebAPIにアクセスするwrapperモジュールです',
    url='https://github.com/sandfishfactory/ckan-reader',
    author='sandfishfactory',
    author_email='sandfishfactory@gmail.com',
    license='MIT',
    keywords='python ckan',
    packages=[
        "ckanreader",
        "ckanreader.action",
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)
