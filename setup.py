from setuptools import setup

setup(
	name='ion',
	version='0.1',
	packages=['ion'],
	entry_points='''
	[console_scripts]
	ion=ion.__main__:main
	'''
)
