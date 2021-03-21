class BillType:
    bill_types = {
        1: "Ambata",
        2: "Ambo",
        3: "Terno",
        4: "Quaterna",
        5: "Cinquina",
    }

    def __init__(self, bill=0):
        self.__bill = bill

    def bill_check(self):
        if self.__bill in BillType.bill_types.keys():
            return True
        return False

    def get_bill(self, bill):
        self.__bill = bill
        if self.bill_check():
            return BillType.bill_types[bill]

    @staticmethod
    def print_bill():
        for key, value in BillType.bill_types.items():
            print(key, value)


# Test
bill = BillType()
print(bill.get_bill(1))
