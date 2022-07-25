from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = self.get_matrix()

    def get_matrix(self):
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for row in range(self.pages):
            if len(self.photos[row]) == 4:
                continue
            self.photos[row].append(label)
            label_index = len(self.photos[row])
            return f"{label} photo added successfully on page {row + 1} slot {label_index}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for row in range(self.pages):
            len_page = len(self.photos[row])
            photos = ["[]" for _ in range(len_page)]
            if len_page == 0:
                result += "\n"
            else:
                result += " ".join(photos) + "\n"
            result += "-----------\n"

        return result.strip()
