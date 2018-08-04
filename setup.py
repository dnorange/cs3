from setuptools import setup, find_packages

setup(
    name='cs3',
    version='0.0.1',
    description='content server 3',
    url='https://github.com/dnorange/cs3',
    author='Ethan.Chen',
    author_email='dnorange@hotmail.com',
    keywords='content server',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django==1.11.7', 'six', 'future', 'httplib2',
                      'django-reversion', 'django-formtools',
                      'django-crispy-forms', 'django-import-export', 'Pillow',
                      'MySQL-python']
)
