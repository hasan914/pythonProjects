#for removing extra spaces from string we use strip() method, lstrip(), rstrip() methods:

favorite_language = " python "


print(favorite_language.rstrip())
print(favorite_language.lstrip())


favorite_language = favorite_language.strip()
print(favorite_language)