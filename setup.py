from setuptools import setup

setup(author='Matthew Egan',
      author_email='matthewj.egan@hotmai.com',
      description='A CLI tool for pruning your overgrown requirements file',
      name='pruner',
      py_modules=[
          'pruner.pruner',
      ],
      entry_points={
            'console_scripts': [
                  'pruner = pruner.pruner:main'
            ]
      },
      install_requires=[
            'crayons==0.1.2',
      ],
      url='https://github.com/mattjegan/pruner',
      version='0.0.5'
)
