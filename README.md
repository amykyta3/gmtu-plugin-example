
# Example Git me the URL plugin

Fork this repository and edit it as needed.

If you create a translator for a public Git hosting service, let me know so I
can add it to the project: https://github.com/amykyta3/git-me-the-url/issues

## Things you'll want to change

* Rename the `gmtu_plugin_example` module folder
    * Recommend keeping the "gmtu" prefix, but it's not necessary.
* Edit/rename [gmtu_plugin_example/my_translator.py](gmtu_plugin_example/my_translator.py) as needed.
* [setup.py](setup.py)
    * Change the `entry_points` string to point to your new translator class.
      This is how the `gitmetheurl` command line application discovers plugins.
    * Update everything else to match your package name (and your name!)
