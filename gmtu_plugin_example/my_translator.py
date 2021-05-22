
from gitmetheurl import TranslatorSpec

class MyTranslator(TranslatorSpec):
    remote_regexes = [
        r'git@myservice\.com:(?P<project_name>[\w\-]+)/(?P<repo_name>[\w\-]+)\.git',
        r'https://myservice\.com/(?P<project_name>[\w\-]+)/(?P<repo_name>[\w\-]+)\.git',
    ]

    url_root_recipes = [
        "https://myservice.com/{project_name}/{repo_name}/",
    ]

    url_body_recipes = [
        ("blob/{branch_name}/{path}", "is_folder == False"),
        ("tree/{branch_name}/{path}", "is_folder == True"),
        ("blob/{commit_hash}/{path}", "is_folder == False"),
        ("tree/{commit_hash}/{path}", "is_folder == True"),
    ]

    url_suffix_recipes = [
        ("#L{start_line}-L{end_line}", "is_folder == False"),
        ("#L{line}", "is_folder == False"),
        "",
    ]
