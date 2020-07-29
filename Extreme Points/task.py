# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
# Work with the 'test_dict'
min = min(test_dict, key=test_dict.get)
max = max(test_dict, key=test_dict.get)
print("min:", min )
print("max:", max)
