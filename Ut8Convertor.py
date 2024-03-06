import chardet


# Step 1: Detect the encoding of the original file
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(4 * 1024)  # Read the first 4KB to guess the encoding
        result = chardet.detect(raw_data)
        return result['encoding']


# Step 2: Read the file with the detected encoding
def convert_file_to_utf8(original_file_path, new_file_path):
    original_encoding = detect_encoding(original_file_path)

    # Ensure an encoding was detected; otherwise, default to ISO-8859-1
    if not original_encoding:
        original_encoding = 'ISO-8859-1'

    with open(original_file_path, 'r', encoding=original_encoding) as original_file:
        contents = original_file.read()

    # Step 3: Write the data to a new file with UTF-8 encoding
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(contents)


# Example usage
#original_file_path = 'packages.txt'
#new_file_path = 'packages_utf8.txt'
#convert_file_to_utf8(original_file_path, new_file_path)