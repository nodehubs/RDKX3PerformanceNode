from setuptools import setup

package_name = 'RDKX3PerformanceNode'

setup(
    name=package_name,
    version='0.0.0',
    packages=[
        package_name,
        package_name + '.templates',
        package_name + '.static',
        package_name + '.static.images',
        ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={
        package_name:[
            'templates/*.*',
            'static/*.*',
            'static/images/*.*',
        ]
    },
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='WuChao_JMUer',
    maintainer_email='2672873269@qq.com',
    description='Show RDK X3 & RDK X3 Module CPU, BPU, Memory and Disk info on Web.',
    license='Licensed under the Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'RDKX3PerformanceNode = RDKX3PerformanceNode.performance_node:main',
        ],
    },
)
