import mysql.connector
import sys

# Make sure to install the connector: pip install mysql-connector-python

# ==============================================================================
# 🛠️ 1. CONFIGURATION (MYSQL CREDENTIALS)
# ==============================================================================

# IMPORTANT: Students MUST update these details to match their local MySQL setup.
DB_CONFIG = {
    'host': '127.0.0.1',  # e.g., 'localhost' or '127.0.0.1'
    'user': 'root',  # Change this to your MySQL username
    'password': 'gokstad',  # Change this to your MySQL password
    'database': 'oliver_db'  # Change this to the name of your database
}


def get_db_connection():
    """Returns a connection object to the MySQL database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print("\n" + "=" * 50)
        print("❌ ERROR: Database Connection Failed.")
        print(f"Details: {err}")
        print("Please check your DB_CONFIG (host, user, password, database) and ensure MySQL is running.")
        print("=" * 50 + "\n")
        # Exit the application if the connection fails
        sys.exit(1)


def create_table():
    """Connects to the database and creates the playlist table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # MySQL syntax for creating the table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS playlist (
                id INT AUTO_INCREMENT PRIMARY KEY,
                song_title VARCHAR(255) NOT NULL,
                artist_name VARCHAR(255) NOT NULL,
                genre VARCHAR(255)
            )
        """)
        conn.commit()
        # print("Database table initialized successfully.") # Optional confirmation
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        cursor.close()
        conn.close()


# ==============================================================================
# 🎶 2. CRUD OPERATIONS (FUNCTIONS)
# ==============================================================================

# C (Create): Add Song
def add_song(title, artist, genre):
    """Adds a new song to the playlist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Use %s as the placeholder for MySQL
    query = "INSERT INTO playlist (song_title, artist_name, genre) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (title, artist, genre))
        conn.commit()
        print(f"\n✅ Added: '{title}' by {artist}.")
    except mysql.connector.Error as err:
        print(f"Error adding song: {err}")
    finally:
        cursor.close()
        conn.close()


# R (Read All): Display Playlist
def view_playlist():
    """Retrieves and prints all songs in the playlist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT id, song_title, artist_name, genre FROM playlist')
        songs = cursor.fetchall()

        if not songs:
            print("\n▶️ The playlist is empty.")
            return

        print("\n--- 🎧 Current Playlist 🎧 ---")
        print(f"{'ID':<4} | {'Song Title':<30} | {'Artist Name':<20} | {'Genre':<15}")
        print("-" * 75)

        for song in songs:
            # Data from MySQL needs to be formatted for printing
            print(f"{song[0]:<4} | {song[1]:<30} | {song[2]:<20} | {song[3]:<15}")
        print("-" * 75)

    except mysql.connector.Error as err:
        print(f"Error viewing playlist: {err}")
    finally:
        cursor.close()
        conn.close()


# U (Update): Change Genre
def update_song_genre(song_id, new_genre):
    """Updates the genre of a song based on its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE playlist SET genre = %s WHERE id = %s"
    try:
        cursor.execute(query, (new_genre, song_id))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"\n✅ Song ID {song_id} updated. New Genre: {new_genre}.")
        else:
            print(f"\n⚠️ Error: No song found with ID {song_id}.")

    except mysql.connector.Error as err:
        print(f"Error updating song: {err}")
    finally:
        cursor.close()
        conn.close()


# D (Delete): Delete Song
def delete_song(song_id):
    """Deletes a song from the playlist based on its ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM playlist WHERE id = %s"
    try:
        cursor.execute(query, (song_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"\n🗑️ Song ID {song_id} deleted successfully.")
        else:
            print(f"\n⚠️ Error: No song found with ID {song_id} to delete.")

    except mysql.connector.Error as err:
        print(f"Error deleting song: {err}")
    finally:
        cursor.close()
        conn.close()


# ==============================================================================
# 💻 3. CLI INTERFACE (MAIN LOOP)
# ==============================================================================
def main():
    """The main command-line interface loop."""
    # Step 1: Ensure the database connection works and the table exists
    create_table()

    while True:
        print("\n--- Playlist Manager CLI (MySQL) ---")
        print("1. Add a new song (Create)")
        print("2. View the full playlist (Read All)")
        print("3. Update a song's genre (Update)")
        print("4. Delete a song (Delete)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            genre = input("Enter genre: ")
            add_song(title, artist, genre)

        elif choice == '2':
            view_playlist()

        elif choice == '3':
            view_playlist()  # Show list to help user choose ID
            try:
                song_id = int(input("Enter the ID of the song to update: "))
                new_genre = input("Enter the new genre: ")
                update_song_genre(song_id, new_genre)
            except ValueError:
                print("\n❌ Invalid input. Please enter a valid number for the ID.")

        elif choice == '4':
            view_playlist()  # Show list to help user choose ID
            try:
                song_id = int(input("Enter the ID of the song to delete: "))
                delete_song(song_id)
            except ValueError:
                print("\n❌ Invalid input. Please enter a valid number for the ID.")

        elif choice == '5':
            print("\n👋 Exiting Playlist Manager. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please select a number from 1 to 5.")


# ==============================================================================
# 🚀 4. ENTRY POINT
# ==============================================================================
if __name__ == '__main__':
    main()