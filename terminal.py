# -*- coding: utf-8 -*-

"""
A module to emulate UNIX terminal functionality
"""

import shlex
import subprocess


class Terminal:

    @staticmethod
    def check_output(command):
        """
        Executes a given shell command
        :param command:
        :return:
        """
        output = subprocess.check_output(command, encoding='utf-8', shell=True)
        return output.strip()

    @staticmethod
    def execute_command(command, stdout=True):
        """
        Executes a given shell command
        :param stdout:
        :param command:
        :return:
        """
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, encoding='utf-8')
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if stdout:
                print(output.strip())
        rc = process.poll()
        return rc
