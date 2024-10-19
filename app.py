def generate_power_set(input_set):
    power_set = set()
    power_set.add(frozenset())
    get_set_recurse(input_set, power_set)
    return power_set

def get_set_recurse(input_set, output_set):
    for i in input_set:
        output_set.add(frozenset(input_set))
        excluded_set = {x for x in input_set if x != i}  
        if len(input_set) > 1:
            get_set_recurse(excluded_set, output_set)  

def main():
    user_input = input("Enter the elements of the set, separated by commas: ")
    input_set = set(user_input.split(','))
    power_set = generate_power_set(input_set)
    print("Power Set:")
    for subset in power_set:
        print(subset)

if __name__ == "__main__":
    main()
