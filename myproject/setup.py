# setup.py

from setuptools import setup

setup(
    name='myproject',
    version='1.0.0',
    description='My Django project',
    author='John Qian',
    packages=['myproject'],
    install_requires=[
        # 项目的依赖关系
        # 'requests',
        # 'other_dependency',
    ],
    # 其他设置...
)
