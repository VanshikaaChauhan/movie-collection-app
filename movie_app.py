import json
import os

MOVIE_FILE = "movies.json"


def load_movies():
    if os.path.exists(MOVIE_FILE):
        with open(MOVIE_FILE, "r") as f:
            return json.load(f)
    return []


def save_movies(movies):
    with open(MOVIE_FILE, "w") as f:
        json.dump(movies, f, indent=4)


def add_movie(movies):
    title = input("Enter movie title: ")
    year = input("Enter release year: ")
    director = input("Enter director: ")
    genre = input("Enter genre: ")

    movie = {
        "title": title,
        "year": year,
        "director": director,
        "genre": genre
    }

    movies.append(movie)
    print(f"✅ '{title}' added to your collection.")


def view_movies(movies):
    if not movies:
        print("📭 No movies in your collection.")
        return

    for idx, movie in enumerate(movies, start=1):
        print(f"\n📽️ Movie {idx}")
        print(f"Title: {movie['title']}")
        print(f"Year: {movie['year']}")
        print(f"Director: {movie['director']}")
        print(f"Genre: {movie['genre']}")


def search_movie(movies):
    search = input("🔍 Enter title to search: ").lower()
    found = [m for m in movies if search in m["title"].lower()]
    if found:
        for movie in found:
            print(f"\n🎞️ {movie['title']} ({movie['year']}) - {movie['director']} - {movie['genre']}")
    else:
        print("❌ No matching movies found.")


def delete_movie(movies):
    title = input("Enter movie title to delete: ").lower()
    for i, movie in enumerate(movies):
        if movie["title"].lower() == title:
            del movies[i]
            print(f"🗑️ '{title}' deleted from collection.")
            return
    print("❌ Movie not found.")


def main():
    movies = load_movies()

    while True:
        print("\n🎬 Movie Collection App")
        print("1. Add movie")
        print("2. View all movies")
        print("3. Search movie")
        print("4. Delete movie")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_movie(movies)
            save_movies(movies)
        elif choice == "2":
            view_movies(movies)
        elif choice == "3":
            search_movie(movies)
        elif choice == "4":
            delete_movie(movies)
            save_movies(movies)
        elif choice == "5":
            save_movies(movies)
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
