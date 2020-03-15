from setuptools import setup


requires = []


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
