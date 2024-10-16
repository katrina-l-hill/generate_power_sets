def generate_power_set(input_set):
    power_set = set()
    power_set.add(frozenset())
    power_set.add(get_set_recurse(input_set, power_set))
    return power_set

def get_set_recurse(input_set, output_set):
    for i in input_set:
        output_set.add(frozenset(input_set))
        excluded_set = {x for x in input_set if x != i}
        if(len(input_set) > 1):
            get_set_recurse(excluded_set, output_set)

for garbage in generate_power_set([0,1,2]):
    print(garbage)

