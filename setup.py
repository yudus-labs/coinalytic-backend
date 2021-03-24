# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# All dependences
deps = {
    'yfolio': ['Flask', 'pymongo', 'ruamel.yaml', 'flask-mongoengine'],
    'test': [
        'pytest',
    ],
    'dev': [
        'tox',
        'pylint',
        'autopep8',
        'rope',
        'black',
    ],
}
deps['dev'] = deps['yfolio'] + deps['dev']
deps['test'] = deps['yfolio'] + deps['test']

install_requires = deps['yfolio']
extra_requires = deps
test_requires = deps['test']

with open('README.adoc') as readme_file:
    long_description = readme_file.read()

setup(
    name='yfolio',
    version='0.0.1',
    description='yFolio backend',
    long_description=long_description,
    long_description_content_type='text/asciidoc',
    author='duyyudus - Yudus Labs',
    author_email='duyyudus@gmail.com',
    url='https://github.com/yudus-labs/yfolio-backend',
    include_package_data=True,
    tests_require=test_requires,
    install_requires=install_requires,
    extras_require=extra_requires,
    license='MIT',
    zip_safe=False,
    keywords='yFolio backend',
    python_requires='>=3.7',
    packages=find_packages(where='src', exclude=['tests', 'tests.*', '__pycache__', '*.pyc']),
    package_dir={
        '': 'src',
    },
    package_data={'': ['**/*.yml']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Operating System :: POSIX :: Linux',
    ],
)