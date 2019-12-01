class Sum(object):
    """
    Handler for Sum operation
    """
    def __init__(self, name):
        self.name = name

    def do(self, data):
        """
        Perform sum operation

        Args:
            data (list): List of values

        Returns:
            float, int: Result operation

        """
        pass


class Max(object):
    """
    Handler for Max operation
    """
    def __init__(self, name):
        self.name = name

    def do(self, data):
        """
        Perform sum operation

        Args:
            data (list): List of values

        Returns:
            float, int: Result operation

        """
        pass


class Min(object):
    """
    Handler for Min operation
    """
    def __init__(self, name):
        self.name = name

    def do(self, data):
        """
        Perform sum operation

        Args:
            data (list): List of values

        Returns:
            float, int: Result operation

        """
        pass


class Mean(object):
    """
    Handler for Mean operation
    """
    def __init__(self, name):
        self.name = name

    def do(self, data):
        """
        Perform sum operation

        Args:
            data (list): List of values

        Returns:
            float, int: Result operation

        """
        pass


SUM = Sum("(SUM)")
MAX = Max("(MAX)")
MIN = Min("(MIN)")
MEAN = Mean("(MEAN)")
