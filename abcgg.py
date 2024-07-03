def load_values():
    result = []
    with open('choose_model.txt') as lines:
        for line in lines:
            _, value = line.strip().split('=')
            result.append(int(value.strip()))
    return result

print(load_values()[1])