class Card:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.image_url = kwargs.get("imageUrl")
        self.set = kwargs.get("set")

    def __str__(self):
        return f"{self.name} ({self.set}) - image: {self.image_url}"
