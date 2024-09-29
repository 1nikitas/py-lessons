class ObjectNotFound(Exception):
    def __init__(self, message, extra_info=None) -> None:
        super().__init__(message)
        self.extra_info = extra_info



