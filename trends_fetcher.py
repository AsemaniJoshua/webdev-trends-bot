import requests

def get_trends():
    url = "https://dev.to/api/articles?tag=webdev&top=1"
    response = requests.get(url)
    articles = response.json()

    # Take only 3 top articles
    top_articles = articles[:3]

    trends = []
    for article in top_articles:
        trends.append({
            "title": article.get("title", "No Title"),
            "description": article.get("description", "No description"),
            "url": article.get("url", "#"),
            "image": article.get("cover_image") or "https://via.placeholder.com/150"
        })

    return trends
