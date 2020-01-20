# from distutils.core import setup
from setuptools import setup

setup(
    name='chatgirl',
    version='1.0',
    author="Suku and Immyyy",
    author_email="gi5@gmail.com",
    description="A chatbot AI engine is a chatbot builder platform that provids both bot intelligence and"
                " chat handler with minimal codding",
    packages=['chatbot', 'chatbot.spellcheck'],
    license='ENSAO',
    keywords='chatbot ai engine and chat builder platform',
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    package_dir={'chatbot': 'chatbot', 'chatbot.spellcheck': 'chatbot/spellcheck'},
    include_package_data=True,
    package_data={"chatbot":  ["default.template", "spellcheck/words.txt"]},
    install_requires=[
          'requests',
      ]
)
