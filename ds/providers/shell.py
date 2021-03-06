from __future__ import absolute_import

__all__ = ['ShellProvider']

from .base import Provider


class ShellProvider(Provider):
    def get_options(self):
        return {
            'command': {'required': True},
        }

    def execute_task(self, workspace, task):
        command = task.provider_config['command'].format({
            'environment': task.environment,
            'sha': task.sha,
            'ref': task.ref,
            'task': task.name,
        })

        return workspace.run(command)
