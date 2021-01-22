import api_data


class Lists:
    def __init__(self, rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales):
        self.rank = rank
        self.name = name
        self.platform = platform
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.na_sales = na_sales
        self.eu_sales = eu_sales
        self.jp_sales = jp_sales
        self.other_sales = other_sales
        self.global_sales = global_sales

    @staticmethod
    def get_details(self):
        print(self.api_data.game[1].name)

