from setuptools import setup
from biketrauma_am import __version__ as current_version

setup(
  name='biketrauma_am',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='http://github.com/exogenee.git',
  author='amine.tzn',
  author_email='amine.tzn34@gmail.com',
  license='MIT',
  packages=['biketrauma_am','biketrauma_am.io', 'biketrauma_am.preprocess', 'biketrauma_am.vis'],
  zip_safe=False
)

