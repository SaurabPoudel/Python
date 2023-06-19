def slugify(*args, sep="-"):
    return sep.join(args)


print(slugify("hello", "world"))
