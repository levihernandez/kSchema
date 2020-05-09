class Sqlite:
    def __init__(self, typeo):
        self.typeo = typeo

    def returntype(self):
        to = self.typeo
        x = ""
        if to == "INTEGER":
            x = 'int'
        if to == "BLOB":
            x = 'string'
        if to == "REAL":
            x = 'int'
        if to == "TEXT":
            x = 'string'
        if to == "NUMERIC":
            x = 'float'
        return x
