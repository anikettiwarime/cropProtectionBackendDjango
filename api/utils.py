# utils.py

def find_class(class_index):
    class_mapping = {
        0: "butterfly",
        1: "cat",
        2: "chicken",
        3: "cow",
        4: "dog",
        5: "elephant",
        6: "horse",
        7: "sheep",
        8: "spider",
        9: "squirrel",
    }
    return class_mapping.get(class_index, "Unknown")
