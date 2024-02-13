import json

def extract_urls_from_json(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)

        urls = []

        for item in data:
            if 'vendorlink' in item and item['vendorlink']:
                urls.append(item['vendorlink'].strip())

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
    extract_urls_from_json(input_file, output_file)
