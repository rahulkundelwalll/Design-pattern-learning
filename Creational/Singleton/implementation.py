class SingleTon(object):
    __instance = None

    def __new__(cls,*args,**kargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    

a = SingleTon()
a.data = 10

b = SingleTon()
b.data = 20

print(a.data)
