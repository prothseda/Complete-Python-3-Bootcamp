# %% [markdown]
# # Functions #8: *args
# Define a function called myfunc that takes in an arbitrary number of arguments, and returns the sum of those arguments.
# Remember, don't run the function, simply provide the definition. 
# For example, a function that returns a count of the number of arbitrary arguments might look like: 
# ~~~
# def myfunc(*args):
#     return len(args)
# ~~~
# This is all you need to enter! 
# To give an idea what the above function would look like when tested: 
# ~~~
# myfunc(5,6,7,8)
# # Output: 4
# ~~~
# Added note: this exercise requires that the function return the sum. Print statements will not work here.


# %%
def myfunc(*args):
    return sum(args)

# %%
myfunc(1,2)

# %%
myfunc(100,200,300)

# %%
