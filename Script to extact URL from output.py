import json

def extract_urls_from_json(input_file, output_file, to_find='vendorlink'):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)

        urls = []

        for item in data:
            if link_key in item and item[to_find]:
                urls.append(item[to_find].strip())

        with open(output_file, 'w') as out_file:
            for url in urls:
                out_file.write(url + '\n')

        print(f'URLs extracted from {input_file} and saved to {output_file}.')
    except FileNotFoundError:
        print(f'Error: File {input_file} not found.')
    except json.JSONDecodeError as e:
        print(f'Error: Unable to decode JSON from {input_file}. Details: {e}')

if __name__ == "__main__":
    input_file = 'test.json'
    output_file = 'output_urls.txt'
    vendor_link_key = 'vendorlink'
    extract_urls_from_json(input_file, output_file, vendor_link_key)
