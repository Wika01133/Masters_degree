def evaluate(data):
    remaining_articles = []
    sum_of_points = 0
    #posortowanie autorów malejąco
    data = sorted(data, key=lambda x: len(x[1]), reverse=True)
    
    for i in range(len(data)):
        articles = data[i][1]
        points = data[i][2]
        selected_articles = []
        number_of_articles = len(articles)
        if number_of_articles != 0:
            #sortowanie malejaco
            sorted_articles = sorted(zip(articles, points), key=lambda x: x[1], reverse=True)

            #3 z najwiekszym wynikiem
            selected_articles = sorted_articles[:3]
            #pozostałe dodane do uzycia potem
            remaining_articles.extend(sorted_articles[3:])
            

            #gdy było użyte mniej niz 3 artykuły
            while(number_of_articles < 3):
                if len(remaining_articles) != 0:
                    remaining_articles = sorted(remaining_articles, key=lambda x: x[1], reverse=True)
                    replenished_article = remaining_articles[0]
                    selected_articles.append(replenished_article)
                    del remaining_articles[0]
                number_of_articles+=1

        print(f"{data[i][0]} used articles: {selected_articles}")
        sum_of_points += sum(x[1] for x in selected_articles)


    evaluation = sum_of_points / len(data)

    return evaluation


authors_data = [
    ("Author 1", ["Author 1, article 1", "Author 1, article 2", "Author 1, article 3"], [45, 11, 33]),
    ("Author 2", ["Author 2, article 1", "Author 2, article 2"], [33, 13]),
    ("Author 3", ["Author 3, article 1"], [12]),
    ("Author 4", ["Author 4, article 1"], [78]),
    ("Author 5", [], []),
    ("Author 6", ["Author 6, article 1", "Author 6, article 2", "Author 6, article 3", "Author 6, article 4"], [33, 55, 66, 42]),
]


results = evaluate(authors_data)

print("\nWynik - ", results)
