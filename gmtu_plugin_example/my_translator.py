
import re

from gitmetheurl import Translator

class MyTranslator(Translator):

    SSH_REGEX = r'git@myservice\.com:(?P<project>[\w\-]+)/(?P<repo>[\w\-]+)\.git'
    HTTPS_REGEX = r'https://myservice\.com/(?P<project>[\w\-]+)/(?P<repo>[\w\-]+)\.git'

    def construct_source_url(self, remote: str, relpath: str, is_folder: bool, line = None, commit: str = None, branch: str = None):
        
        # Parse remote
        m = re.fullmatch(self.SSH_REGEX, remote) or re.fullmatch(self.HTTPS_REGEX, remote)
        project_name, repo_name = m.group("project", "repo")

        if is_folder:
            urltype = "tree"
            line_suffix = ""
        else:
            urltype = "blob"
            if isinstance(line, int):
                line_suffix = "#L%d" % line
            elif isinstance(line, tuple) and len(line) == 2:
                line_suffix = "#L%d-L%d" % line
            else:
                line_suffix = ""

        if branch is not None:
            ref = branch
        elif commit is not None:
            ref = commit
        else:
            # uuh panic!!
            ref = "master"
        
        return "https://myservice.com/%s/%s/%s/%s/%s%s" % (
            project_name, repo_name,
            urltype, ref,
            relpath, line_suffix
        )
