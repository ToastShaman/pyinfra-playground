from  pyinfra.api import FactBase

class SwapEnabled(FactBase):
    '''
    Returns a boolean indicating whether swap is enabled.
    '''

    command = 'swapon --show'

    def process(self, output):
        return len(output) > 0  # we have one+ lines
