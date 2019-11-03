# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Functions #7: is greater
# Define a function called is_greater that takes in two arguments, and returns True if the first value is greater than the second, False if it is less than or equal to the second.
# 
# Remember, don't run the function, simply provide the definition.
# 
# For example, a function that returns True if the first value is less than the second might look like:
# ~~~
# def is_less(c,d):
#     if c < d:
#         return True
#     else:
#         return False
# ~~~
# This is all you need to enter!
# 
# To give an idea what the above function would look like when tested:
# ~~~
# is_less(5,9)
# # Output: True
# ~~~
# Added note: this exercise requires that the function return True or False. Print statements will not work here.
# 

# %%
def is_greater(x,y):
    if x > y:
        return True
    else:
        return False


# %%
is_greater(1, 2)


# %%
is_greater(2,1)


# %%
is_greater(1,1)

