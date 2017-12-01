from setuptools import setup
setup(
   name='gtd',
   version='1.0',
   description='A useful module',
   author='yangming',
   author_email='yang756260386@gmail.com',
   packages=['gtd'],  #same as name
   install_requires=['requests','click'], #external packages as dependencies
       entry_points = {
        'console_scripts': ['gtd=gtd.gtd:test'],
    }



)
