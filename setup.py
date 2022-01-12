from setuptools import setup, find_packages

setup(
    name='pyqt-polygon-window',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_polygon_window.style': ['button.css'], 'pyqt_polygon_window.ico': ['close.png']},
    description='PyQt polygon window',
    url='https://github.com/yjg30737/pyqt-polygon-window.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)