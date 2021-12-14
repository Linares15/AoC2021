binary_numbers = []
with open("inputs/day_03.txt") as stream:
    for line in stream.readlines():
        binary_numbers.append(list(map(int, line.strip())))

number_of_bits = len(binary_numbers[0])

def most_common(binary_numbers, bit):
    zero = 0
    one = 0
    for binary_number in binary_numbers:
        if binary_number[bit] == 0:
            zero = zero + 1
        else:
            one = one + 1
    if zero <= one:
        return 1
    else:
        return 0

gamma_rate = ""
epsilon_rate = ""
for bit in range(number_of_bits):
    value = most_common(binary_numbers, bit)
    gamma_rate += str(value)
    if value == 0:
        epsilon_rate += "1"
    else:
        epsilon_rate += "0"
actual_gamma_rate = int(gamma_rate, 2)
actual_epsilon_rate = int(epsilon_rate, 2)

power_consumption = actual_gamma_rate * actual_epsilon_rate

print(f"part 1: {power_consumption}")

# part 2

def keep(arr, bit, value):
    return list(filter(lambda x: x[bit] == value, arr))

def least_common(binary_numbers, bit):
    value = most_common(binary_numbers, bit)
    return 1 if value == 0 else 0

o2_generator_ratings = binary_numbers
co2_scrubber_ratings = binary_numbers

for bit in range(number_of_bits):
    value = most_common(o2_generator_ratings, bit)
    o2_generator_ratings = keep(o2_generator_ratings, bit, value)
    if len(o2_generator_ratings) == 1:
        break

for bit in range(number_of_bits):
    value = least_common(co2_scrubber_ratings, bit)
    co2_scrubber_ratings = keep(co2_scrubber_ratings, bit, value)
    if len(co2_scrubber_ratings) == 1:
        break

o2_generator_rating = ""
for value in o2_generator_ratings[0]:
    o2_generator_rating += str (value)

co2_scrubber_rating = ""
for value in co2_scrubber_ratings[0]:
    co2_scrubber_rating += str (value)

actual_o2_generator_rating = int(o2_generator_rating, 2)
actual_co2_scrubber_rating = int(co2_scrubber_rating, 2)

life_support_rating = actual_o2_generator_rating * actual_co2_scrubber_rating

print(life_support_rating)