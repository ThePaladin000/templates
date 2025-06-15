def read_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]
    