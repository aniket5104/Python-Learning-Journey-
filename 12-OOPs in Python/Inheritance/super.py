class A:
    def show(self):
        print("A")

class B(A):
    def show_parent(self):
        super().show()

o1=B()
o1.show_parent()