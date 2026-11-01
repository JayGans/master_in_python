# multi-level inheritance = inherit from a parent which inerits from another parent
#                           C(B) <- B(A) <- A

class GrandFather:
    def Land(self):
        print("Land come from grandfather")

class Father(GrandFather):
    def home(self):
        print("home purchased by father")

class Children(Father):
    def home(self):
        print("Home purchased by Father but modified by child")

c1 = Children()
c1.Land()
c1.home()