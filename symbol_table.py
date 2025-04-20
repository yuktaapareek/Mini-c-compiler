class SymbolTable:
    def __init__(self):
        self.table = {}

    def declare(self, var_type, var_name, value=None):
        if var_name in self.table:
            raise ValueError(f"Variable '{var_name}' already declared")
        self.table[var_name] = {'type': var_type, 'value': value}

    def update(self, var_name, value):
        entry = self.table.get(var_name)
        if not entry:
            raise NameError(f"Undefined variable '{var_name}'")
        entry['value'] = value

    def lookup(self, var_name):
        return self.table.get(var_name)

    def display(self):
        print("\n🔹 Symbol Table:")
        print(f"{'Variable':<10} {'Type':<10} {'Value':<10}")
        print("-" * 30)
        for var, data in self.table.items():
            print(f"{var:<10} {data['type']:<10} {str(data['value']):<10}")
