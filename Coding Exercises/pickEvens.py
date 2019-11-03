# %%
def myfunc(*args):
    return [x for x in args if x % 2 == 0]

# %%
myfunc(5,6,7,8)