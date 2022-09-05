class emp:
    no_of_leaves = 10

    @classmethod #class method is used to do operation on class enviroment and avoid instance
    def change_leaves (cls ,new_leaves):
        cls.no_of_leaves = new_leaves



aman = emp
sahu = emp

sahu.change_leaves(20)
print(aman.no_of_leaves)
