 # Now that you’ve learned about optional and keyword parameters, we can introduce a new way to use the format method.

names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))
ometimes, you may want to use the .format method to insert the same value into a string multiple times. You can do this by simply passing the same string into the format method, assuming you have included {} s in the string everywhere you want to interpolate them. But you can also use positional passing references to do this! The order in which you pass arguments into the format method matters: the first one is argument 0, the second is argument 1, and so on.
