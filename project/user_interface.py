import langcodes
from typing import Optional, Callable
from deep_translator import GoogleTranslator  # type: ignore
from flash_card_repo import FlashCardRepo
from flash_card import FlashCard
from user_data import UserData


class UserInterface:
    """
    Provides user interface layer.

    Attributes:
        fcr (FlashCardRepo): The FlashCard repository used for storing and retrieving flash cards.
        user_data (UserData): The UserData object for storing settings and points.
        func_fix_space (Callable[[str], str]): The function used for trimming front and back phrases.
        func_calc_complexity (Callable[[str], int]): The function used the calculation of the front side phrase complexity to be used as earned user's points.
        func_clean_tag_list (Callable[[list[str]], str]): The function used for cleaning and sorting the tag list and making a joint string.
        category (str): Stores the current category.
        front_lang (str): Stores the current front side language code.
        back_lang (str): Stores the current back side language code.
        points (int): Stores the current user's points earned from correct answers.
    """

    def __init__(
        self,
        fcr: FlashCardRepo,
        user_data: UserData,
        func_fix_space: Callable[[str], str],
        func_calc_complexity: Callable[[str], int],
        func_clean_tag_list: Callable[[list[str]], str],
    ):
        self.fcr: FlashCardRepo = fcr
        self.user_data: UserData = user_data
        self.func_fix_space: Callable[[str], str] = func_fix_space
        self.func_calc_complexity: Callable[[str], int] = func_calc_complexity
        self.func_clean_tag_list: Callable[[list[str]], str] = func_clean_tag_list
        self.category: str = user_data.read("category", "general")
        self.front_lang: str = user_data.read("front_lang", "it")
        self.back_lang: str = user_data.read("back_lang", "en")
        self.points: int = user_data.read("points", 0)

    def main_menu(self) -> None:
        """
        Provides the main menu for the user.
        """
        print("Hi chum! Welcome to the ChumFlash!")
        print("Category:", self.category)
        lang_name = self.get_lang_name_from_code(self.front_lang)
        print("Front language:", lang_name)
        lang_name = self.get_lang_name_from_code(self.back_lang)
        print("Back language:", lang_name)
        print("Your points:", self.points)

        while True:
            command = input(
                "Give command(1:set category, 2: front lang, 3: back lang, 4:add flash, 5:category test, 6:global test, 7:list, 8:search, 9:remove, 0:end):"
            ).lower()
            match command:
                case "1":
                    self.set_cat()
                case "2":
                    self.set_front_lang()
                case "3":
                    self.set_back_lang()
                case "4":
                    self.add_flash()
                case "5":
                    self.test_flash_rand(self.category)
                case "6":
                    self.test_flash_rand()
                case "7":
                    self.get_list()
                case "8":
                    self.search()
                case "9":
                    self.remove()
                case "0":
                    print("Bye!")
                    break

    def set_cat(self) -> None:
        """
        Menu entry for changing the current category.
        """
        try:
            cat_list: list[str] = self.fcr.get_cat_list()
            if self.category not in cat_list:
                cat_list = [*cat_list, self.category]

            print("Available categories:")
            for i in range(len(cat_list)):
                print(i + 1, cat_list[i])
            cat_no = int(input("Select a number, zero for a new one: "))
            if cat_no <= 0 or cat_no > len(cat_list):
                cat = input("New category: ")
                if cat:
                    cat = cat.strip().lower()
                if cat:
                    self.category = cat
                    self.user_data.write("category", self.category)
            else:
                self.category = cat_list[cat_no - 1]
                self.user_data.write("category", self.category)
        except Exception as e:
            print("Error:", str(e))

    def set_front_lang(self) -> None:
        """
        Menu entry for changing and persisting the front side language.
        """
        try:
            lang_name = self.get_lang_name_from_code(self.front_lang)
            print("Current front language:", lang_name)
            lang = self.get_lang_from_user()
            if lang and lang.language != self.front_lang:
                self.front_lang = "" if lang.language is None else lang.language
                self.user_data.write("front_lang", self.front_lang)
                print(
                    f"Front side language changed to {lang.display_name()}({lang.language})"
                )
            else:
                lang_name = self.get_lang_name_from_code(self.front_lang)
                print(
                    f"Front side language remained unchanged: {lang_name}({self.front_lang})"
                )
        except Exception as e:
            print("Error:", str(e))

    def set_back_lang(self) -> None:
        """
        Menu entry for changing and persisting the back side language.
        """
        try:
            lang_name = self.get_lang_name_from_code(self.back_lang)
            print("Current back language:", lang_name)
            lang = self.get_lang_from_user()
            if lang and lang.language != self.back_lang:
                self.back_lang = "" if lang.language is None else lang.language
                self.user_data.write("back_lang", self.back_lang)
                print(
                    f"Back side language changed to {lang.display_name()}({lang.language})"
                )
            else:
                lang_name = self.get_lang_name_from_code(self.back_lang)
                print(
                    f"Back side language remained unchanged: {lang_name}({self.back_lang})"
                )
        except Exception as e:
            print("Error:", str(e))

    def get_lang_from_user(self) -> Optional[langcodes.Language]:
        """
        Gets the language by name or code from the user.
        """
        lnc = input("Enter the language name or code: ")
        lang = None
        try:
            lang = langcodes.find(lnc)
        except:
            try:
                lang = langcodes.get(lnc)
            except:
                pass
        if lang:
            if lang.is_valid():
                yn = input(
                    f"Your selected language is {lang.display_name()}({lang.language})?(Y/n) "
                )
                if yn != "n" and yn != "N":
                    return lang

        return None

    def get_lang_name_from_code(self, lang_code: str) -> str:
        """
        Returns the language name based on the language code.

        Parameters
        -------------
        lang_code: str
            Language code like en.

        Returns
        -------------
        str
            Language name like English.
        """
        try:
            lc = langcodes.get(lang_code)
            return lc.display_name()
        except:
            return lang_code

    def add_flash(self) -> None:
        """
        Menu entry for creating a new flash card.
        """
        try:
            front = input("Give me the front word or phrase: (Enter to cancel) ")
            if not front:
                return
            front = self.func_fix_space(front)
            if self.fcr.check_card(front):
                raise ValueError("Card already exists!")

            back = None
            try:
                back = GoogleTranslator(
                    source=self.front_lang, target=self.back_lang
                ).translate(front)
            except:
                pass
            if back is None:
                back = input("Give me the back: ")
            else:
                print(f"Suggested back: {back}")
                tmp_back = input(
                    "Give me the back: (Enter to accept the suggested back) "
                )
                if tmp_back:
                    back = tmp_back
            back = self.func_fix_space(back)

            print("Give me the tags. Press Enter alone to terminate the list!")
            tag_list = []
            while True:
                tag = input().strip().lower()
                if not tag:
                    break
                tag_list.append(tag)
            tags = self.func_clean_tag_list(tag_list)

            complexity = self.func_calc_complexity(front)
            flash_card = FlashCard(
                front=front,
                back=back,
                tags=tags,
                category=self.category,
                front_lang=self.front_lang,
                back_lang=self.back_lang,
                complexity=complexity,
            )
            self.fcr.add(flash_card)
        except Exception as e:
            print("Error:", str(e))

    def test_flash_rand(self, cat: Optional[str] = None) -> None:
        """
        Menu entry to quiz the user with a random flash card.

        Parameters
        -------------
        cat: str | None
            The category from which to select a random flashcard. Use None to select from all categories.

        Returns
        -------------
        None
        """
        try:
            card = self.fcr.get_random(cat)
            if card is None:
                print("Card not found")
                return

            print("front:", card.front)
            back = input("Give me the back:")

            if card.back.lower() == self.func_fix_space(back.lower()):
                self.add_point(card.complexity)
                print(
                    f"Bravo! You gained {card.complexity} points, reaching a total of {self.points}"
                )
            else:
                print("oops!")
                print(f"Answer: {card.back}, Lang: {card.back_lang}")
        except Exception as e:
            print("Error:", str(e))

    def get_list(self) -> None:
        """
        Menu entry for getting all cards from the repository and displaying them.
        """
        try:
            card_list = self.fcr.get_list(self.category)
            print()
            if len(card_list):
                print(f"{len(card_list)} Cards in the {self.category} category:")
                for card in card_list:
                    print("-------------------------------")
                    print(card)
            else:
                print(f"No Card in the {self.category} category.")
            print()
        except Exception as e:
            print("Error:", str(e))

    def search(self) -> None:
        """
        Menu entry for searching a flash card by a phrase in its front or back side.
        """
        try:
            search_phrase = input("Enter the search phrase: ").strip()
            card_list = self.fcr.search(search_phrase)
            print()
            if len(card_list):
                print(f"{len(card_list)} cards with this phrase were found:")
                for card in card_list:
                    print("-------------------------------")
                    print(card)
            else:
                print("No card was found with this phrase!")
            print()
        except Exception as e:
            print("Error:", str(e))

    def remove(self) -> None:
        """
        Menu entry to remove a card by its id.
        """
        try:
            id = 0
            try:
                id = int(input("Enter the card id: ").strip())
            except:
                pass
            if id > 0:
                if self.fcr.remove_card(id):
                    print("Card was removed.")
                else:
                    print("card was not found.")
        except Exception as e:
            print("Error:", str(e))

    def add_point(self, p: int) -> None:
        """
        Adds a value to the user's points and persists the new value.

        Parameters
        -------------
        p: int
            The incrementing value.

        Returns
        -------------
        None
        """
        self.points += p
        self.user_data.write("points", self.points)
