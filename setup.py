from setuptools import setup, find_packages

setup(
    name='seppay',
    version='1.0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=4.0',
        'djangorestframework>=3.14.0',
        'requests'
    ],
    description='Saman bank payment gateway. SEP',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/freecyberhawk/sep_pay_pi',
    author='FreeCyberHawk',
    author_email='freecyberhawk@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
