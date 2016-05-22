from distutils.core import setup

setup(
    name="make_proj",
    version="0.1",
    packages=[
        "make_proj", "make_proj.templates", "make_proj.templates.vs2015"
    ],
    install_requires=["cheetah=2.4.4"],
    license="MIT",
)
