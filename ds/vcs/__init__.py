from __future__ import absolute_import

from .manager import VcsManager
from .git import GitVcs

manager = VcsManager()
manager.add('git', GitVcs)

get = manager.get
