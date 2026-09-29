try:
    with open("input.txt", "r") as f:
        lines = f.readlines()

        count = len(lines)
        first_two = lines[:2]

    with open("output.txt", "w") as out:
        out.write(f"Total lines: {count}\n")
        out.writelines(first_two)

    print("Done! Check output.txt")

except FileNotFoundError:
    print("Error: input.txt not found")
