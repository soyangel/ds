from __future__ import absolute_import

__all__ = ['Provider']


class Provider(object):
    name = None

    def get_options(self):
        return {}

    def execute(self, workspace, task):
        raise NotImplementedError
