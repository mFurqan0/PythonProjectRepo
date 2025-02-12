from collections import Counter


fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'banana']


fruit_counter = Counter(fruits)


print("Fruit counts:", fruit_counter)


print("\nMost common two fruits:", fruit_counter.most_common(2))


new_fruits = ['apple', 'grape', 'apple', 'grape']
fruit_counter.update(new_fruits)


print("\nUpdated fruit counts:", fruit_counter)


print("\nNumber of apples:", fruit_counter['apple'])
print("Number of grapes:", fruit_counter['grape'])