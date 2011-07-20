import os
import sublime
import sublime_plugin


class Pep8CheckCommand(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if view.file_name().endswith('.py'):
            folder_name, file_name = os.path.split(view.file_name())
            view.window().run_command('exec', {'cmd': ['flake8',
                file_name], 'working_dir': folder_name})
            sublime.status_message("pep8 " + file_name)