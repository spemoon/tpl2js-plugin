import sublime, sublime_plugin
import os ,sys
import traceback

sys.path.append("/usr/local/bin")

class Tpl2jsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            file_old = self.view.file_name()
            file_new = file_old[0:-4] + 'js'
            done = os.system("PATH=$PATH:/usr/local/bin /usr/local/lib/node_modules/tpl2js/lib/tpl.bin.js %s %s" % (file_old, file_new))
        except:
            self.view.insert(edit, 0, traceback.format_exc())        
