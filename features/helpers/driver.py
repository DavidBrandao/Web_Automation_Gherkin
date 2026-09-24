_driver = None

def set_driver(instance):
    global _driver
    _driver = instance

def get_driver():
    if _driver is None:
        raise RuntimeError("Driver não foi inicializado! Verifique o before_scenario.")
    return _driver
