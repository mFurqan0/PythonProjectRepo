list = [
    {"name":"Zain", "age":25},
    {"name":"Zarak", "age":29},
    {"name":"Furqan", "age":19}
]

def Sort_list(list):
    return list["age"]


sorted_list = sorted(list,key=Sort_list)

print(sorted_list)
