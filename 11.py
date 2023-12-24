import requests

def get_books_from_api(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        books = response.json()
        return books
    else:
        print(f"Không thể lấy dữ liệu từ API. Mã trạng thái: {response.status_code}")
        return None

def display_books(books):
    if books:
        print("----- Danh sách các bài post -----")
        print(f"Tổng số bài post: {len(books)}\n")

        for book in books:
            print(f"userID: {book['userId']}")
            print(f"id: {book['id']}")
            print(f"title: {book['title']}")
            print(f"body: {book['body']}\n")

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/posts"

    books = get_books_from_api(api_url)

    if books:
        display_books(books)
