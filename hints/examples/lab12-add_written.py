num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}

print("Give me two written numbers between one and twenty.")
num1 = input("First num: ")
num2 = input("Second num: ")
added_nums = num_dict[num1] + num_dict[num2]
print(f"The sum is {added_nums}."
