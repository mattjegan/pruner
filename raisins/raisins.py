"""
This CLI tool should be used with the following command:
    plums <requirements_file> <output_file> <test_command>
"""
import sys

class Raisins(object):
    def __init__(self):
        self._loadArgs()
        self._getRequirements()
        self._loadVirtualEnv()
        self._installRequirements()

    def run(self):
        #raise NotImplementedError('this method is the entry point to running '
        #                          'over all the requirements and testing them')

        for r in self.requirements.keys():
            pass
            # Uninstall the requirement
            # ...
            # Run the test
            # ...
            # Was the test successful?
            # if success: self.requirements[r] = False

        # Output the results
        with open(self.outputFile, 'w') as f:
            for r in self.requirements.keys():
                f.write(r + '\n')

    def _loadArgs(self):
        self.args = sys.argv
        self.reqFile = self.args[1]
        self.outputFile = self.args[2]
        self.testCommand = ' '.join(self.args[3:])

    def _getRequirements(self):
        self.requirements = {r.strip(): True for r in open(self.reqFile, mode='r')}

    def _loadVirtualEnv(self):
        raise NotImplementedError('this method should just shell out and create a'
                                  'blank virtualenv to test in')

    def _installRequirements(self):
        raise NotImplementedError('this method should install each requirement in the virtualenv')

    def _runTest(self):
        raise NotImplementedError('this method should just shell out and '
                                  'run self.testCommand and return the exit bool')


def main():
    r = Raisins()
    r.run()


if __name__ == '__main__': main()