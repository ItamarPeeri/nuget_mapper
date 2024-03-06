def parse_config(config_file_name):
    parameters = {}

    with open(config_file_name, "r") as file:
        config = file.read()

    # Split the config data by lines and iterate through them
    for line in config.strip().split('\n'):
        # Split each line by '=' to separate the key and value
        key, value = line.split('=', 1)

        # Strip whitespace and remove any trailing or leading quotes from the key
        key = key.strip().strip('\'"')

        # Evaluate the value to handle lists and strings correctly
        try:
            value = eval(value.strip())
        except NameError:
            # Handle the case where eval might raise a NameError for unquoted strings
            value = value.strip().strip('\'"')

        parameters[key] = value

    return parameters