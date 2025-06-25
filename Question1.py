# INTI Matriculation Number: P23015051
# Name: Ng Jing Wen

import random


# Part 1: Create Hash Function
def ic_hash(ic_number, table_size):
    ic_str = str(ic_number)

    if len(ic_str) != 12 or not ic_str.isdigit():
        raise ValueError("Malaysian IC number must be 12 digits")

    hash_value = 0
    group_size = 3  # Group size for folding

    for i in range(0, 12, group_size):
        group = ic_str[i:i + group_size]
        hash_value += int(group)

    return hash_value % table_size


# Part 2(a): Generate 1000 IC Numbers
def generate_random_ic():
    """Generate a random 12-digit Malaysian IC number in format YYMMDDXXXXXX"""
    # First 6 digits: YYMMDD (birthdate)
    year = random.randint(0, 99)  # Last two digits of birth year
    month = random.randint(1, 12)

    if month == 2:
        day = random.randint(1, 28)
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)

    # Next 2 digits: Birthplace code (simplified to random for this example)
    birthplace = random.randint(0, 99)

    # Last 4 digits: Randomly generated
    last_four = random.randint(0, 9999)

    # Combine into 12-digit string
    return f"{year:02d}{month:02d}{day:02d}{birthplace:02d}{last_four:04d}"


# Part2(b): Create Hash Table
def create_hash_table(size):
    """Create a hash table of given size using separate chaining"""
    return [[] for _ in range(size)]


# Part2(c): Insert IC Number into Hash Table
def insert_into_table(table, ic_number, table_size):
    """Insert IC number into hash table, return True if collision occurred"""
    index = ic_hash(ic_number, table_size)
    collision_occurred = len(table[index]) > 0
    table[index].append(ic_number)
    return collision_occurred


def print_hash_table(table):
    for i, bucket in enumerate(table):
        # if bucket:
            chain = " --> ".join(bucket)
            print(f"table[{i}] --> {chain}")


def main():
    """Run the collision experiment for 10 rounds"""
    table1_size = 1009  # Prime number
    table2_size = 2003  # Larger prime number

    rounds = 10
    num_ic_numbers = 1000

    table1_collisions = [0] * rounds
    table2_collisions = [0] * rounds

    for round_num in range(rounds):
        # Generate random IC numbers for this round
        ic_numbers = [generate_random_ic() for _ in range(num_ic_numbers)]

        # Create fresh hash tables for this round
        table1 = create_hash_table(table1_size)
        table2 = create_hash_table(table2_size)

        # Insert all IC numbers and count collisions
        for ic in ic_numbers:
            if insert_into_table(table1, ic, table1_size):
                table1_collisions[round_num] += 1
            if insert_into_table(table2, ic, table2_size):
                table2_collisions[round_num] += 1

        print("\nHash Table with size 1009: ")
        print_hash_table(table1)

        print("\nHash Table with size 2003: ")
        print_hash_table(table2)

    # Part 3: Calculate Statistics
    # Calculate the average collisions for each hash table
    avg_table1 = sum(table1_collisions) / rounds
    avg_table2 = sum(table2_collisions) / rounds

    table1_rates = []
    table2_rates = []

    for i in range(rounds):
        rate1 = (table1_collisions[i] / num_ic_numbers) * 100
        rate2 = (table2_collisions[i] / num_ic_numbers) * 100
        table1_rates.append(rate1)
        table2_rates.append(rate2)

    # Calculate the collision rate for each hash table
    avg_rate1 = sum(table1_rates) / rounds
    avg_rate2 = sum(table2_rates) / rounds

    total_collisions = []

    # Display results
    # Display the total collisions for each round
    print("\nRound\tTable 1 Collisions\tTable 2 Collisions\tTotal Collisions")
    print("-----\t-------------------\t-------------------\t----------------")
    for i in range(rounds):
        total = table1_collisions[i] + table2_collisions[i]
        total_collisions.append(total)
        print(f"{i + 1:>5}\t{table1_collisions[i]:>19}\t{table2_collisions[i]:>19}\t{total_collisions[i]:>16}")

    # Display the average collisions for each hash table
    print(f"\nAverage Collision for Hash Table 1: {avg_table1:.2f}")
    print(f"Average Collision for Hash Table 2: {avg_table2:.2f}")

    # Display the collision rate for each hash table
    print(f"\nCollision Rate for Hash Table 1: {avg_rate1:.2f}%")
    print(f"Collision Rate for Hash Table 2: {avg_rate2:.2f}%")


# Run the program
if __name__ == "__main__":
   main()