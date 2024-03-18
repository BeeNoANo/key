import json
import random


class Tool:
    def generate_unique_key():
        with open("data.json", "r") as f:
            json_data = json.load(f)
        ascii_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
        digits = "0123456789"
        while True:  # Tạo key mới cho đến khi tìm được key duy nhất
            key = "UnHwid_" + "".join(random.choice(ascii_letters + digits) for i in range(16))
            if not any(key in item for item in json_data):  # Kiểm tra trùng lặp
                return key

class Key:
    def __init__(self, key):
        with open("data.json", "r") as f:
            json_data = json.load(f)
        self.listkey = json_data
        self.key = key
    def check(self):
        for item in self.listkey:
            if self.key in item:
                return item[self.key]
        return None  # Trả về None nếu không tìm thấy
    def create(self, num_keys):
        if self.key ==  "04072009":
            for i in range(num_keys):
                new_key = Tool.generate_unique_key()
                self.listkey.append({new_key: "NotHwid"})
            with open("data.json", "w") as f:
                json.dump(self.listkey, f, indent=4)
        else:
            return False

    def remove(self):
        for index, item in enumerate(self.listkey):
            if self.key in item:
                del self.listkey[index]
                break

        # Lưu lại dữ liệu
        with open("data.json", "w") as f:
            json.dump(self.listkey, f, indent=4)
        return True

    def changeValue(self, newValue):
        try:
            item_to_change_value = next(item for item in self.listkey if self.key in item)
            item_to_change_value[self.key] = newValue
            with open("data.json", "w") as f:
                json.dump(self.listkey, f, indent=4)
        except StopIteration:
            return None
        


a = Key("UnHwid_5R7Q8NRMQSB64M1P").remove()
print(a)