def read_ip_addresses(file_path):
    with open(file_path, 'r') as file:
        # Read the IP addresses from the file and return them as a set
        ip_addresses = {line.strip() for line in file}
    return ip_addresses

def find_differences(file1_path, file2_path):
    # Read IP addresses from both files
    ip_addresses1 = read_ip_addresses(file1_path)
    ip_addresses2 = read_ip_addresses(file2_path)

    # Find differences between the two sets
    differences1 = ip_addresses1 - ip_addresses2
    differences2 = ip_addresses2 - ip_addresses1

    return differences1, differences2

def save_differences_to_file(file_path, differences):
    with open(file_path, 'w') as file:
        file.write('\n'.join(differences))

def main():
    file1_path = 'file.txt'  # Replace with the path to your first file
    file2_path = 'file2.txt'  # Replace with the path to your second file
    output_file_path = 'differences.txt'  # Replace with the desired output file path

    differences1, differences2 = find_differences(file1_path, file2_path)

    print("IP addresses present in file1 but not in file2:")
    print(differences1)

    print("\nIP addresses present in file2 but not in file1:")
    print(differences2)

    save_differences_to_file(output_file_path, differences1)
    print(f"\nDifferences saved to {output_file_path}")

if __name__ == "__main__":
    main()
