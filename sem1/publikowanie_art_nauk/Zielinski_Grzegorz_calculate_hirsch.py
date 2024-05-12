def hirsch_index(articles, citations):
    sorted_article = sorted(zip(articles, citations), key=lambda x: x[1], reverse=True)
    h_index = 0
    for hid, (article, citation) in enumerate(sorted_article, start=1):
        if citation >= hid:
            h_index = hid
        else:
            break
            
    return h_index

articles = ["Art1", "Art2", "Art3", "Art4", "Art5"]
citations = [2, 15, 80, 3, 5]

print("Hirsch Index:")
print(hirsch_index(articles, citations))
