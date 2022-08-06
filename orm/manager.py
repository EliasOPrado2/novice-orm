
class BaseManager:

    def __init__(self, model_class):
        self.model_class = model_class

    def select(self, *field_names):
        pass

    def bulk_insert(self, rows: list):
        pass

    def update(self, new_data: dict):
        pass

    def delete(self):
        pass