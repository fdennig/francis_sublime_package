Francis Sublime Packagge
========================

# wiki_page.py
- this file needs to supercede the file with the same name in the Markdown Editing Package
- It does three things
    1. ensures that wiki links and back links are searched in the entire project. This entails modifications to varios find_files methods
    2. changes the make page reference command so that it doubles up existing square brackets into double square brackets, and pulls up the list of all markdown files so that one can be chosen to insert inside the brackets. This speeds up wiki creation
        + some weird self.view.insert calls were needed, that I still don't fully understand.

# Default.sublime-keymap
- "super+alt+z"
    + opens sublime merge
- "f12"
    + calls open_linked_file when scope is the description of a markdown link (the part inside the square bracket. open_linked_file opens links to files and url and is defined in francis.py
- "tab"
    + calls the mde_make_page_reference command only inside markdown files and when cursor is inside single square brackets. the command is overriden in my version of wiki_page.py so that single brackets are turned into a wiki,  all markdown files are shown in the the dropdown and the selected markdown is inserted in the wiki.
    
# francis.sublime-commands
- adds call to mde_make_page_reference to the command palette

# francis.py
- creates the open_linked_file command to open files and urls in a markdown link from inside the markdown line description