from abc import ABC, abstractmethod

# In order to create an abstract class in python we have to
# 1. import ABC class
# ABC - Abstract Base Class from abc package and declare abstract as shown below
# 2. import abstractmethod decorator (annotation) and
# use @abstractmethod decorator (annotation)
# on the methods which are required to be declared as abstract methods.


class AbstractRecipe(ABC):
    def execute(self):
        self.get_ready()
        self.prepare_the_dish()
        self.clean_up()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def prepare_the_dish(self):
        pass

    @abstractmethod
    def clean_up(self):
        pass

# TypeError: Can't instantiate abstract class AbstractRecipe with abstract methods clean_up, get_ready, prepare_the_dish
# recipe = AbstractRecipe()
# recipe.execute()


class Recipe1(AbstractRecipe):

    def get_ready(self):
        print("get_ready from Recipe1")

    def prepare_the_dish(self):
        print("prepare_the_dish from Recipe1")

    def clean_up(self):
        print("clean_up from Recipe1")


recipe1 = Recipe1()
recipe1.execute()


class RecipeWithMicrowave(AbstractRecipe):

    def get_ready(self):
        print("get_ready from RecipeWithMicrowave")

    def prepare_the_dish(self):
        print("prepare_the_dish from RecipeWithMicrowave")

    def clean_up(self):
        print("clean_up from RecipeWithMicrowave")


recipe1 = RecipeWithMicrowave()
recipe1.execute()
