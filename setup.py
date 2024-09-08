from setuptools import find_packages, setup

package_name = 'irs_ros2_connect'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='achukrish',
    maintainer_email='achkrish07@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "intel_pub = irs_ros2_connect.irs_pub:main",
            "intel_sub = irs_ros2_connect.irs_sub:main"
        ],
    },
)
