ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list.remove("tata!")
ft_list.append("World!")

ft_tuple_copy = list(ft_tuple)
ft_tuple_copy.remove("toto!")
ft_tuple_copy.append("France!")
ft_tuple = tuple(ft_tuple_copy)

ft_set.remove("tutu!")
ft_set.add("Mulhouse!")

ft_dict["Hello"] = "42Mulhouse!"

print(ft_list)
print(ft_tuple)
print(sorted(ft_set))
print(ft_dict)
