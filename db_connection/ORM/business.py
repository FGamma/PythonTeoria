from dataclasses import dataclass
from review import Review


@dataclass
class Business:
    business_id: str
    full_address: str
    active: str
    categories: str
    city: str
    review_count: int
    business_name: str
    neighborhoods: str
    latitude: float
    longitude: float
    state: str
    stars: float

    # Inserisco le relazioni. Un business può avere molte review.
    # Posso scegliere tra queste 2 opzioni:
    # reviews_id: list[str]
    # reviews: list[Review]

    # Entrambi hanno svantaggi: uso lazy initialization.
    # Devo definire anche get_reviews()
    reviews: list[Review] = None

    def __eq__(self, other):
        return self.business_id == other.business_id

    def __hash__(self):
        return hash(self.business_id)

    def get_reviews(self):
        if self.reviews is None:
            # vado a leggerle dal DAO e popolo la list
            pass
        else:
            return self.reviews
