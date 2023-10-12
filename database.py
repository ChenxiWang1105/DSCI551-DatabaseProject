## this is our main program
class Database:
    def __init__(self):
        self.tables = {}

    # def create_table(self, table_name, columns):
    #     if table_name in self.tables:
    #         raise ValueError(f"Table {table_name} already exists.")
    #     self.tables[table_name] = {"columns": columns, "data": []}

    def insert(self, table_name, values):
         if table_name not in self.tables:
             print(f"Table {table_name} doesn't exist.")
         if len(values) != len(self.tables[table_name]):
             print("Number of columns doesn't match.")
         for i in range(self.tables[table_name]):
             self.tables[table_name][i].append(values[i])

    def delete(self, table_name, items, condition):
        if table_name not in self.tables:
            print(f"Table {table_name} doesn't exist.")
        if not condition:
            for ele in items:
                self.tables[table_name][ele] = None
        else:
            #evaluate_conditions()

    def update(self, table_name, values, condition):
        if table_name not in self.tables:
            print(f"Table {table_name} doesn't exist.")
            #evaluate_conditions()

    def get(self, table_name, columns, connect_table, on_condition, conditions=None, grouping=None, ordering=None, order_by=None):
        print(f"output columns {columns} from table {table_name} connect with table {connect_table} on {on_condition} with conditions {conditions} gather by {grouping} order by {order_by} in {ordering} order")
        # if table_name not in self.tables:
        #     raise ValueError(f"Table {table_name} doesn't exist.")
        # data = self.tables[table_name]["data"]

        # if not conditions:
        #     results = data
        # else:
        #     results = []
        #     for row in data:
        #         if self._evaluate_conditions(row, conditions):
        #             results.append(row)

        # if not columns or columns == ["*"]:
        #     return results
        # return [self._filter_columns(row, columns) for row in results]

    # def _evaluate_conditions(self, row, conditions):
    #     # Implement your condition evaluation logic here
    #     # For simplicity, this template assumes that all conditions are met
    #     return True

    # def _filter_columns(self, row, columns):
    #     return {col: row[col] for col in columns}
