class xyz:

    def InstanceMethod(self):
        print("INSTANCE METHOD", type(self))

    @classmethod
    def ClassMethod(cls):
        print("CLASS METHOD", type(cls))

    @staticmethod
    def StaticMethod():
        print("Static Method")


obj = xyz()
obj.InstanceMethod()
xyz.InstanceMethod(obj)

obj.ClassMethod()
xyz.ClassMethod()

obj.StaticMethod()
xyz.StaticMethod()
