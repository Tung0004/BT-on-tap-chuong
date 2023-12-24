import requests

def get_featured_books(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        featured_books = response.json()
        return featured_books
    else:
        print(f"Không thể lấy dữ liệu từ API. Mã trạng thái: {response.status_code}")
        return None

def display_featured_books(featured_books):
    if featured_books:
        print("----- Danh sách các bài post nổi bật -----")
        limited_books = featured_books[:3]  # Giới hạn chỉ hiển thị 3 bài đầu
        for book in limited_books:
            print(f"postId: {book['postId']}")
            print(f"id: {book['id']}")
            print(f"name: {book['name']}")
            print(f"email: {book['email']}")
            print(f"body: {book['body']}\n")

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/comments?postId=1"

    featured_books = get_featured_books(api_url)

    if featured_books:
        display_featured_books(featured_books)
