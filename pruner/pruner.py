"""
This CLI tool should be used with the following command:
    pruner <requirements_file> <output_file> <test_command>
"""
import argparse
import os
import subprocess

import crayons

PROMPT = crayons.magenta('PRUNER: ', bold=True)

class Pruner(object):

    def __init__(self):
        parser = argparse.ArgumentParser(description='A CLI tool to help prune your overgrown requirements file')
        parser.add_argument('requirements_file')
        parser.add_argument('output_file')
        parser.add_argument('test_command', nargs='*')
        self.args = parser.parse_args()

        self._loadArgs()
        self._getRequirements()
        self._loadVirtualEnv()
        self._installRequirements()

    def _call(self, *args, **kwargs):

        initial = kwargs.pop('initial', False)
        if not initial:
            with open(os.devnull, "w") as f:
                if isinstance(args[0], list):
                    s = subprocess.call(args[0], stdout=f, stderr=f)
                else:
                    s = subprocess.call(*args, stdout=f, stderr=f, **kwargs)
        else:
            if isinstance(args[0], list):
                s = subprocess.call(args[0])
            else:
                s = subprocess.call(*args, **kwargs)

        return s

    def _cleanUp(self):
        print(PROMPT + 'deactivate')
        self._call('deactivate', shell=True)
        print(PROMPT + 'rm -rf prunertests')
        self._call('rm -rf prunertests', shell=True)

    def run(self):
        # Run initial test to make sure things work as is
        print(PROMPT + 'Running initial test...')
        success = self._runTest(initial=True)
        if success:
            print(PROMPT + 'Initial test was a success, beginning requirement tests...')
        else:
            print(PROMPT + 'Initial test was a failure, we cannot tell why, cleaning and exiting...')
            self._cleanUp()

        for r in self.requirements.keys():
            print(PROMPT + 'Testing {}'.format(r))
            # Uninstall the requirement
            self._call(['pip', 'uninstall', '-y', r])
            # Run the test
            success = self._runTest()
            # Was the test successful?
            if success:
                print(PROMPT + crayons.red('{} was not needed'.format(r)))
                self.requirements[r] = False
            else:
                print(PROMPT + crayons.green('{} was needed'.format(r)))
            # Reinstall the req so that it doesn't change the other reqs results
            self._call(['pip', 'install', r])

        # Kill the virtualenv
        self._cleanUp()

        # Output the results
        print(PROMPT + crayons.white('Writing results to {}'.format(self.outputFile), bold=True))
        with open(self.outputFile, 'w') as f:
            for r in self.requirements.keys():
                if self.requirements[r]:
                    f.write(r + '\n')
        print(PROMPT + crayons.white('DONE', bold=True))

    def _loadArgs(self):
        self.reqFile = self.args.requirements_file
        self.outputFile = self.args.output_file
        self.testCommand = self.args.test_command

    def _getRequirements(self):
        self.requirements = {r.strip(): True for r in open(self.reqFile, mode='r')}

    def _loadVirtualEnv(self):
        print(PROMPT + 'virtualenv prunertests')
        self._call('virtualenv prunertests', shell=True)
        print(PROMPT + 'source prunertests/bin/activate')
        self._call('source prunertests/bin/activate', shell=True)

    def _installRequirements(self):
        # For the initial install we can just use the initial requirements file
        print(PROMPT + 'pip install -r {}'.format(self.reqFile))
        self._call(['pip', 'install', '-r', self.reqFile])

    def _runTest(self, initial=False):
        return not bool(self._call(self.testCommand, initial=initial))


def main():
    r = Pruner()
    r.run()


if __name__ == '__main__': main()