class CostException(SystemExit):
    """
    This exception cannot be caught using try/except. It will exit the program. 
    """
    pass

class WebSearchNoResultsException(Exception):
    pass
