class Player:

    # This variable is by default static
    count = 0

    # Here only 'name' is instance variable and 'count' is static variable
    def __init__(self, name):
        self.name = name
        Player.count += 1

    # This is a static method - we have to use decorator(like annotation in Java)
    @staticmethod
    def get_count():
        return Player.count


messi = Player('Messi')
ronaldo = Player('Ronaldo')

print(Player.count)
print("------------------------------------------------------------")
# We should never set the static values using instance variable.
# By doing so we would see different behaviour
# For ex -

messi.count = 100
print(messi.count)

print(Player.count)
print("------------------------------------------------------------")
# We have to set like static variables like this.
Player.count = 100
print(Player.count)
Player.count = 0
print("------------------------------------------------------------")

# Now we can call the static method directly
andre = Player('Andre')
nadal = Player('Nadal')
print(andre.get_count())
print(andre.get_count())
print(Player.get_count())

