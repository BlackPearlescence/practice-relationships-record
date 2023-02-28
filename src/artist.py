class Artist:
    def __init__(self,name:str):
        self._name = name
        self._records = []
    
    def get_name(self) -> str:
        return self._name
    def set_name(self, name:str): 
        self._name = name
    def get_records(self) -> list:
        return self._records
    def set_records(self,records:list):
        self._records = records

    # Record with earliest year
    def get_first_record(self):
        min_record = min(self._records, key=lambda record:record.year)
        return min_record
    
    name = property(get_name,set_name)
    records = property(get_records,set_records)

    