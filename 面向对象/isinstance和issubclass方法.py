# isinstance(obj,cls)检查对象obj是否是cls的对象
# issubclass(sub,super)检查sub类是否是super类的派生类


class A:
    pass


class B(A):
    pass


a = A()
print(isinstance(a,A))
print(issubclass(B,A))
print(issubclass(A,B))