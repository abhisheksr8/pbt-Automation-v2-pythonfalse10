from setuptools import setup, find_packages

setup(
    name='AutomationPBTNo_v2-pythonfalse10',
    version='1.0',
    packages=find_packages(include=['automationpbtno_v2pythonfalse10*']),
    description='AutomationPBTNo_v2-pythonfalse10',
    install_requires=[
        'prophecy-libs==1.9.32'
    ],
    entry_points={
        'console_scripts': [
            'main = automationpbtno_v2pythonfalse10.pipeline:main',
        ],
    },
    data_files=[(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require={
        'test': ['pytest', 'pytest-html'],
    }
)