class Tree:
  age = 200
  height = 600
  color = "brown"

  def __init__(self):
     print("")

  def get_older(self):
      self.age += 1

 
my_tree = Tree()

print(my_tree.age)

my_tree.get_older()

   

  
  