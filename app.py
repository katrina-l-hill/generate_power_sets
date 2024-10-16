def generate_power_set(input_set):
    # Convert the input set to a list to allow indexing
    input_list = list(input_set)
    
    power_set = []

    def get_set_recurse(subset, index):
        # Base case: If the index reaches the length of the input list, add the current subset to the power set
        if index == len(input_list):
            power_set.append(frozenset(subset))  # Convert subset to frozenset for immutability
            return
        
        # Recursive case 1: Exclude the current element and recurse to the next index
        get_set_recurse(subset, index + 1)
        
        # Recursive case 2: Include the current element and recurse to the next index
        get_set_recurse(subset + [input_list[index]], index + 1)

    # Start the recursion with an empty subset and index 0
    get_set_recurse([], 0)
    
    return power_set

def get_user_input():
    user_input = input("Enter the elements of the set, separated by commas: ")
    
    elements = [x.strip() for x in user_input.split(',')]
    
    return set(elements)

input_set = get_user_input()

power_set = generate_power_set(input_set)

print("Power Set:")
for subset in power_set:
    print(subset)
