import setuptools

setuptools.setup(
    name="gmtu-plugin-example",
    version="1.0.0",
    author="Alex Mykyta",
    author_email="amykyta3@github.com",
    description="Example git-me-the-url translator plugin",
    packages=['gmtu_plugin_example'],
    install_requires=[
        "git-me-the-url",
    ],
    entry_points =
    """
    [gitmetheurl.translators]
    mytranslator = gmtu_plugin_example.my_translator:MyTranslator
    """,
)
