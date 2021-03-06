import sublime

from .golite import utils
from .golite.formatter import GoliteFormatCommand, GoliteFormatListener
from .golite.gocode import GocodeListener
from .golite.godef import GoliteGodefCommand
from .golite.installer import GoliteDoctorCommand, GoliteInstallCommand
from .golite.rename import GoliteRenameCommand

try:
    from .golite.linter import Gometalinter
except ImportError:
    print("""[golite] failed to import 'Gometalinter', please install \
'Sublimelinter'""")


def plugin_loaded():
    sublime.run_command('golite_install')
