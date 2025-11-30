class DataError(RuntimeError):
    """
    Custom exception type to signal issues with data
    """
    pass

class ConfigurationError(RuntimeError):
    """
    Signals issues with configuration
    """
    pass
