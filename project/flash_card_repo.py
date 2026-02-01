import csv
import random
from typing import Optional
from flash_card import FlashCard


class FlashCardRepo:
    """
    A repository for storinng flash cards using a csv file.

    Attributes:
        file_name (str): The csv file name.
        _flash_cards (list[FlashCard]): The in-memory list of flash cards.
    """

    ID = "id"
    FRONT = "front"
    BACK = "back"
    TAGS = "tags"
    CATEGORY = "category"
    FRONT_LANG = "front_lang"
    BACK_LANG = "back_lang"
    COMPLEXITY = "complexity"

    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self._flash_cards: list[FlashCard] = []

        try:
            with open(self.file_name, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames
                for row in reader:
                    flash_card = FlashCard()
                    flash_card.id = int(row[FlashCardRepo.ID])
                    flash_card.front = row[FlashCardRepo.FRONT]
                    flash_card.back = row[FlashCardRepo.BACK]
                    flash_card.tags = row[FlashCardRepo.TAGS]
                    flash_card.category = row[FlashCardRepo.CATEGORY]
                    flash_card.front_lang = row[FlashCardRepo.FRONT_LANG]
                    flash_card.back_lang = row[FlashCardRepo.BACK_LANG]
                    flash_card.complexity = int(row[FlashCardRepo.COMPLEXITY])
                    self._flash_cards.append(flash_card)
        except FileNotFoundError:
            with open(self.file_name, mode="w", encoding="utf-8", newline="") as file:
                headers = self._get_header()
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()

    def add(self, flash_card: FlashCard) -> None:
        """
        Adds a new flash card to the repository. Raises exception if the front term already exists.

        Parameters
        -------------
        flash_card: FlashCard
            The flash card to be added.

        Returns
        -------------
        None
        """
        # check name exists
        generator = (f for f in self._flash_cards if f.front == flash_card.front)

        card = next(generator, None)

        if card is not None:
            raise ValueError("Card already exists")
        id = max([f.id for f in self._flash_cards], default=0) + 1
        flash_card.id = id
        with open(self.file_name, mode="a", encoding="utf-8", newline="") as file:
            headers = self._get_header()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow(flash_card.__dict__)
        # after making sure it is stored in the file, we can add it to the in-memory list
        self._flash_cards.append(flash_card)

    def get_random(self, category: Optional[str] = None) -> FlashCard:
        """
        Selects randomly a card in the specified category or in all categories.

        Parameters
        -------------
        category: str | None
            The specified category. 'None' to select among all the available cards.

        Returns
        -------------
        FlashCard
            A randomly selected flash card.
        """
        filtered_ids = [
            fc.id for fc in self._flash_cards if not category or fc.category == category
        ]
        id = random.choice(filtered_ids)
        gen = (fc for fc in self._flash_cards if fc.id == id)
        rfc = next(gen)
        return rfc

    def get_list(self, category: str) -> list[FlashCard]:
        """
        Returns all cards in the specified category.

        Parameters
        -------------
        category: str
            The specified category.

        Returns
        -------------
        list[FlashCard]
            List of flash cards.
        """
        filtered = [fc for fc in self._flash_cards if fc.category == category]
        filtered.sort(key=lambda card: card.front)
        return filtered

    def search(self, search_phrase: str) -> list[FlashCard]:
        """
        Returns the cards with the specified phrase in their front or back side.

        Parameters
        -------------
        search_phrase: str
            The specified search phrase.

        Returns
        -------------
        list[FlashCard]
            List of flash cards.
        """
        search_phrase = search_phrase.strip().lower()
        filtered = [
            fc
            for fc in self._flash_cards
            if search_phrase in fc.front.lower() or search_phrase in fc.back.lower()
        ]
        filtered.sort(key=lambda card: card.front)
        return filtered

    def get_cat_list(self) -> list[str]:
        """
        Returns the list of categories used in the available flash cards.

        Parameters
        -------------

        Returns
        -------------
        list[str]
            List of categories.
        """
        categories = sorted(list(set([fc.category for fc in self._flash_cards])))
        return categories

    def check_card(self, front: str) -> bool:
        """
        Checks if a front term has been used exactly in the stored flash cards.

        Parameters
        -------------
        front: str
            The front side term.

        Returns
        -------------
        bool
            True if the input front term is available, False otherwise.
        """
        generator = (f for f in self._flash_cards if f.front == front)
        card = next(generator, None)
        return not not card

    def remove_card(self, id: int) -> bool:
        """
        Deletes a card with the specified id.

        Parameters
        -------------
        front: id
            The specified id.

        Returns
        -------------
        bool
            True if the existing card is deleted successfully.
        """
        generator = (i for i, v in enumerate(self._flash_cards) if v.id == id)
        i = next(generator, None)
        if i is None:
            return False
        del self._flash_cards[i]
        with open(self.file_name, mode="w", encoding="utf-8", newline="") as file:
            headers = self._get_header()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for flash_card in self._flash_cards:
                writer.writerow(flash_card.__dict__)
        return True

    def _get_header(self) -> list[str]:
        """
        Returns the list of csv headers (database columns)

        Parameters
        -------------

        Returns
        -------------
        list[str]
            list of csv headers.
        """
        headers = []
        headers.append(FlashCardRepo.ID)
        headers.append(FlashCardRepo.FRONT)
        headers.append(FlashCardRepo.BACK)
        headers.append(FlashCardRepo.TAGS)
        headers.append(FlashCardRepo.CATEGORY)
        headers.append(FlashCardRepo.FRONT_LANG)
        headers.append(FlashCardRepo.BACK_LANG)
        headers.append(FlashCardRepo.COMPLEXITY)
        return headers
