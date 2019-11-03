# %% [markdown]
# # Functions #10: skyline
# Define a function called myfunc that takes in a string, and returns a matching string where every letter is uppercase, and every odd letter is lowercase.
# Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation.
# The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.
# Example:
# ~~~
# myfunc('Example')
# # Output: 'eXaMpLe'
# ~~~

# %%
def myfunc(string):
    out = []
    for i in range(len(string)):
        if i % 2 == 0:
            out.append(string[i].upper())
        else:
            out.append(string[i].lower())
    return ''.join(out)
    

# %%
myfunc('Example')

# %%
