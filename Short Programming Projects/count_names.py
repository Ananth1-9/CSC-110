def read_file(filename):
  new_list = []
  file = open(filename, "r")
  for line in file:
    line_parts = line.strip().split(",")
    for p in line_parts:
      new_list.append(p)
  return new_list

def read_file(filename):
    data_list = []
    with open(filename, 'r') as file:
        for line in file:
            items = line.strip().split(',')
            data_list.extend(items)
    return data_list

def count_names(my_list):
    name_counts = {}
    for item in my_list:
        # Per the lab hint, if the first character is not numeric,
        # it's a name.
        if item and (not item[0].isnumeric()):
            if item in name_counts:
                name_counts[item] += 1
            else:
                name_counts[item] = 1
    return name_counts

def find_name(counts_dict, name):
    if name in counts_dict:
        count = counts_dict[name]
        return f"The name {name} occurs {count} times."
    else:
        return f"{name} not found."

def get_most_common_name(counts_dict):
    most_common_name = None
    max_count = -1

    for name, count in counts_dict.items():
        if count > max_count:
            max_count = count
            most_common_name = name
            
    return f"The name {most_common_name} occurs {max_count} times."


if __name__ == "__main__":
   my_list = read_file("names_and_numbers.txt")
   my_counts = count_names(my_list)
   print(my_counts)
   print(len(my_counts))
   print(find_name(my_counts, "Adriana"))
   print(find_name(my_counts, "Maria"))
   print(get_most_common_name(my_counts))



  