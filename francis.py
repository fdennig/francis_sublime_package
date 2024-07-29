import sublime
import sublime_plugin
import re
import os
import webbrowser


def open_file(path):
    # Regular expression to check if the string is a URL
    url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if url_regex.match(path):
        # Open URL in default web browser
        webbrowser.open(path)
    # Check if the path exists
    elif os.path.exists(path):
        # Open the file with its default application
        try:
            if sublime.platform() == "windows":
                os.startfile(path)
            elif sublime.platform() == "osx":
                subprocess.run(['open', path])
            else:
                subprocess.run(['xdg-open', path])
        except Exception as e:
            print("Failed to open file {path}. Error: {error}".format(path=path, error=str(e)))
    else:
        print("The path {path} does not exist".format(path=path))

class OpenLinkedFileCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        selection = self.view.sel()
        for region in selection:
            # find the actual path of the link
            pt = region.end()
            link_start = self.view.find("\((<\w|\w|\"w|<\"\w)", pt)
            link_path = self.view.expand_to_scope(link_start.end()-1,"meta.link.inline.metadata.markdown")

            clean_link_path = self.view.substr(link_path).strip("(<\">)")
            # Open the file
            open_file(clean_link_path)
