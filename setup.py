from setuptools import setup, find_packages
setup(name='ditrace_schem_gen',
		version='0.0.0b1',
		description='Diptrace Schematic Generator',
		url='https://github.com/snhobbs/DiptraceSchematicApi',
		author='Simon Hobbs',
		author_email='simon.hobbs@hobbs-eo.com',
		license='BSD',
		packages=find_packages(),
		install_requires=[
			'pyfiglet'
		],
		#test_suite='nose.collector',
		#tests_require=['nose'],
		#scripts=['bin/'],
		include_package_data=True,
		zip_safe=True)
