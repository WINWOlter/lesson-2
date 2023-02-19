class Tree:
  age = 200
  height = 600
  color = "brown"
  leafs = 1000000

  def __init__(self, type):
     self.type = type

  def get_older(self):
      self.age += 1
    

  

 
my_tree = Tree("Akacia")

print(my_tree.age)

my_tree.get_older()



   

  
  