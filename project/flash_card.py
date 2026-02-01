class FlashCard:
    """
    Represents a flash card used for language learning.

    Attributes:
        id (int): Unique id.
        front (str): The term on the front of the card.
        back (str): The translated term on the back of the card.
        tags (str): Dash separated string of the categorizing tags.
        category (str): The category label.
        front_lang (str): Front side language code.
        back_lang (str): Back side language code.
        complexity (int): An integer assigned to the card as its complexity used later for giving points to the user.
    """

    def __init__(
        self,
        id: int = 0,
        front: str = "",
        back: str = "",
        tags: str = "",
        category: str = "general",
        front_lang: str = "",
        back_lang: str = "",
        complexity: int = 0,
    ):
        self.id: int = id
        self.front: str = front
        self.back: str = back
        self.tags: str = tags
        self.category: str = category
        self.front_lang: str = front_lang
        self.back_lang: str = back_lang
        self.complexity: int = complexity

    def __str__(self):
        return f"id: {self.id}\nfront: {self.front}\nback: {self.back}\ntags: {self.tags}\ncategory: {self.category}\nfront_lang: {self.front_lang}\nback_lang: {self.back_lang}\ncomplexity:{self.complexity}"
