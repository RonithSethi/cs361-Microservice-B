import json
from time import sleep

# Load the food names from JSON once at the beginning
with open("foodIndexMicro.json", "r") as f:
    food_list = json.load(f)

while True:
    sleep(.1)  # Prevent excessive CPU usage

    with open("pipeB.txt", "r") as prng:
        x = prng.read().strip()  # Read and strip whitespace

    if x.isdigit():  # Ensure it's a valid integer
        index = int(x)

        if 0 <= index < len(food_list):  # Check index bounds
            food_name = food_list[index]

            # Write the food name back into pipeB.txt
            with open("pipeB.txt", "w") as pw:
                pw.write(food_name)
