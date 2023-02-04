thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020, "color": "red"})
print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["year"]
print(thisdict)