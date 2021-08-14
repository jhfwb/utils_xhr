#!/usr/bin/env python
# coding=utf-8
import setuptools
# 打包语句：python setup.py sdist bdist_wheel
# sys.argv=['setup.py','sdist','bdist_wheel'] #将sys.argv的外部参数改成setup.py。相当于是运行python
setuptools.setup(
    name="utils_xhr",#软件包名称
    version='1.0.0.2',
    author="许焕燃",
    author_email='527077832@qq.com',
    description="这是一个基础工具包",
    long_description=open('README.md',encoding='utf-8').read(),#详细描述
    long_description_content_type="text/markdown",#详细描述的格式
    # url="utils_xhr@git+https://github/jhfwb/...", #模块的github地址
    packages=setuptools.find_packages(),
    license='TMT',
    include_package_data=True,
    zip_safe=False,
    # py_modules=["Tool"],
    classifiers=[# 程序的所属分类列表
    ],
    install_requires=[# 填写依赖包(github格式:  包名@git+https://github/jhfwb/包所在文件 )
    ],
    python_requires='>=3'
)
