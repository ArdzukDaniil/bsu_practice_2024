try:
    func()
    print("No Exceptions")
except ValueError as ve:
    print("ValueError")
except TypeError as te:
    print("TypeError")
except SystemError as se:
    print("SystemError")