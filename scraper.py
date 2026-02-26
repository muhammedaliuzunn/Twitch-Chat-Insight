import sqlite3
import twitchio
from twitchio.ext import commands
from datetime import datetime

# --- STEP 1: DATABASE SETUP ---
def setup_database():
    """Initializes the SQLite database and creates the messages table if it doesn't exist."""
    connection = sqlite3.connect('chat_logs.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            content TEXT,
            timestamp DATETIME
        )
    ''')
    connection.commit()
    connection.close()
    print("Database is ready!")

# --- STEP 2: TWITCH CHAT LISTENER ---
class ChatAnalyzerBot(commands.Bot):
    def __init__(self):
        # NOTE: Remember to hide your oauth token before pushing to GitHub!
        super().__init__(
            token='oauth:YOUR_TOKEN_HERE', 
            prefix='!', 
            initial_channels=['']
        )

    async def event_ready(self):
        """Triggered when the bot successfully connects to Twitch."""
        print(f"Logged in as {self.nick} on Twitch servers.")
        print("Listening to chat... Data is being streamed to the database.")

    async def event_message(self, message):
        """Processes incoming messages and saves them to the database."""
        # Ignore messages sent by the bot itself
        if message.echo:
            return

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Save message to SQLite
        connection = sqlite3.connect('chat_logs.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO messages (username, content, timestamp)
            VALUES (?, ?, ?)
        ''', (message.author.name, message.content, current_time))
        connection.commit()
        connection.close()

        # --- FANCY TERMINAL OUTPUT ---
        RED = '\033[91m'
        GREEN = '\033[92m'
        BLUE = '\033[94m'
        GRAY = '\033[90m'
        RESET = '\033[0m'

        print(f"{GRAY}[{current_time}]{RESET} 💬 {GREEN}{message.author.name}{RESET}: {BLUE}{message.content}{RESET}")

if __name__ == "__main__":
    setup_database()
    bot = ChatAnalyzerBot()

    bot.run()

