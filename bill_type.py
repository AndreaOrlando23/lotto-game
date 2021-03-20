class BillType:
    bill_types = {
        1: "Ambata",
        2: "Ambo",
        3: "Terno",
        4: "Quaterna",
        5: "Cinquina",
    }

    def __init__(self, bill=0):
        self.bill = bill

    def city_check(self):
        if self.bill in BillType.bill_types.keys():
            return True
        return False

    @staticmethod
    def print_bill():
        for key, value in BillType.bill_types.items():
            print(key, value)
