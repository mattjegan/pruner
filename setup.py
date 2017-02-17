from setuptools import setup

setup(author='Matthew Egan',
      author_email='matthewj.egan@hotmai.com',
      description='A CLI tool for pruning your overgrown requirements file',
      name='plum',
      py_modules=[
          'plum.plum',
      ],
      entry_points={
            'console_scripts': [
                  'plum = plum.plum:main'
            ]
      },
      url='https://github.com/mattjegan/plum',
      version='0.0.1'
)
