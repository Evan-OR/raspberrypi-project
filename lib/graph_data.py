class GraphData:
    def __init__(self, max_data_length=100) -> None:
        self.data = []
        self.max_data_length = max_data_length

    def add(self, new_data: list):
        if len(self.data) == self.max_data_length:
            del self.data[0]

        self.data.append(new_data)

    def get(self) -> list:
        x = [item[0] for item in self.data]
        y = [item[1] for item in self.data]
        return [x, y]
