def load_file_index():
    try:
        with open('cfg/file_index.txt', 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0