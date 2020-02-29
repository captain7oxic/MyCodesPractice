class xyz:

    """http://pythontutor.com/visualize.html#code=class%20xyz%3A%0A%0A%20%20%20%20def%20InstanceMethod%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28%22Instance%20method%22%29%0A%20%20%20%20%20%20%20%20print%28type%28self%29%29%0A%0A%20%20%20%20def%20ClassMethod%28cls%29%3A%0A%20%20%20%20%20%20%20%20print%28%22Class%20Method%22,%20type%28cls%29%29%0A%0A%20%20%20%20def%20StaticMethod%28%29%3A%0A%20%20%20%20%20%20%20%20print%28%22Static%20method%22%29%0A%0A%20%20%20%20%22%22%22making%20the%20class%20and%20static%20method%22%22%22%0A%20%20%20%20ClassMethod%20%3D%20classmethod%28ClassMethod%29%0A%20%20%20%20StaticMethod%20%3D%20staticmethod%28StaticMethod%29%0A%0A%0AO%20%3D%20xyz%28%29%0Aprint%28type%28O%29%29%0AO.InstanceMethod%28%29%0Axyz.InstanceMethod%28O%29%0A%0AO.ClassMethod%28%29%0Axyz.ClassMethod%28%29%0A%0A%0A%0A%22%22%22%20Class%20method%20take%20only%20one%20arguement%20'self'%20%22%22%22%0A%0A%0AO.StaticMethod%28%29%0Axyz.StaticMethod%28%29%0A&cumulative=false&curInstr=29&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"""

    def InstanceMethod(self):
        print("Instance method")
        print(type(self))

    def ClassMethod(cls):
        print("Class Method", type(cls))

    def StaticMethod():
        print("Static method")

    """making the class and static method"""
    ClassMethod = classmethod(ClassMethod)
    StaticMethod = staticmethod(StaticMethod)


O = xyz()
print(type(O))
O.InstanceMethod()
xyz.InstanceMethod(O)

O.ClassMethod()
xyz.ClassMethod()
"""Exception has occurred: TypeError
ClassMethod() takes 1 positional argument but 2 were given
File "C:\Users\Vatsal\Desktop\codes\Automate the boring stuff with python\OOPS\methods.py", line 24, in < module >
xyz.ClassMethod(O)
"""
""" Class method take only one arguement 'self' """


O.StaticMethod()
xyz.StaticMethod()
