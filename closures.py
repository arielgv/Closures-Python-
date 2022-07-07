#Closures: Python Closures are these inner functions that
#  are enclosed within the outer function.
#  Closures can access variables present in the outer function scope.
#  It can access these variables even after the outer function has completed its execution


"""
  This program ask the user a number, and a phrase or word, 
  returning the phrase (or word) as many times as the integer entered before.
  This code has been written in one of my first approaches to this code so i 
  decided not change some of the names in the variables. Just for remember my
  early times.
"""

def repeater(n):
    def palabra(wordar):
        return wordar * n
    return palabra

    



veces = int(input("How many times?  "))
pickedword = input("Enter a string: ")

repeat_func = repeater(veces)
print(repeat_func(pickedword))


# Written in Visual Studio Code.