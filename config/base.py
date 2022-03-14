class Config:
    debug = False
    run_local = False

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            if not hasattr(cls, "_instance"):
                cls._instance = object.__new__(cls)
        return cls._instance
