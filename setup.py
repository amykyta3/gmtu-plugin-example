import setuptools

setuptools.setup(
    name="gmtu-plugin-example",
    version="1.0.0",
    author="Alex Mykyta",
    author_email="amykyta3@github.com",
    description="Example git-me-the-url translator plugin",
    packages=setuptools.find_packages(),
    install_requires=[
        "git-me-the-url >= 2.0.0",
    ],
    entry_points =
    """
    [gitmetheurl.translators]
    mytranslator = gmtu_plugin_example.my_translator:MyTranslator
    """,
)
