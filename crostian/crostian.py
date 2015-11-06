import random as rand

__author__ = "JairoVadillo"


class CrostException(Exception):
    """
    Inherits from Exception to create a freshly new crostianized exception.
    """
    pass


def crostiada(func):
    """
    To be used as decorator.
    Overrides the function you are trying to call by random stuff. No one knows how crostian-core can react.
    :param func: Function to be crostianized
    :return: Crostianized function
    """
    def inner():
        # Crostiresponses
        responses = [
            None,
            'Tu si que {}'.format(func.__name__),
            17,
            'No me pagan.',
            func()
        ]

        # Generate random index
        idx = rand.randint(0, len(responses))

        # Case Crosti raise exception
        if idx == len(responses):
            raise CrostException('No.')

        # Case no exception return random value
        return responses[rand.randint(0, len(responses) - 1)]

    return inner
