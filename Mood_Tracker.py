import datetime
import random


def main():
    print("🌈 Welcome to the Mood Tracker!")

    # All moods and their advice lists
    moods = {
        "happy": [
            "Keep smiling and spread your joy! 🌟",
            "Celebrate the little wins today! 🎉",
            "Happiness looks good on you. 😊",
            "Use this energy to do something creative! 🎨"
        ],
        "sad": [
            "It’s okay to feel low sometimes. 🌿",
            "Tough times don’t last, strong people do. 💪",
            "Listen to your favorite song and relax. 🎵",
            "Remember, after rain comes sunshine. ☀️"
        ],
        "stressed": [
            "Take a deep breath. You’ve got this. 🧘",
            "Pause and organize your thoughts. 🧩",
            "Try a 10-minute break, it really helps. 🌤️",
            "You’re doing better than you think. 🌱"
        ],
        "tired": [
            "Rest is productive too. 😴",
            "You’ve worked hard, take a break. 💤",
            "Hydrate and stretch a bit. 💧",
            "Slow down. You deserve rest. 🌙"
        ],
        "excited": [
            "Love that energy! Make today count! ⚡",
            "Great things start with excitement. 🚀",
            "Share your joy, it multiplies! 🎉",
            "Let your passion guide you today! 🔥"
        ],
        "angry": [
            "Pause. Breathe. Respond calmly. 🌬️",
            "Step away for a moment, peace first. 🧘‍♂️",
            "Don’t let anger control your words. 💭",
            "Cool minds make better decisions. ❄️"
        ],
        "bored": [
            "Try something new today, even a small change helps. 🌈",            "Explore a hobby or read something interesting. 📚",
            "Turn boredom into creativity. 🎨",
            "Call a friend or watch something uplifting! ☕"
        ],
        "anxious": [
            "Inhale......... Exhale.......... You're safe right now. 🌿",
            "Focus on what you can control. Let go of the rest. 🌤️",
            "You’re stronger than your worries. 💪",
            "Try journaling or a short walk to calm your thoughts. 🚶"
        ],
        "motivated": [
            "Perfect time to take action! 🚀",
            "Keep that drive, small steps lead to big wins! 💡",
            "Stay consistent, success follows persistence. 🔥",
            "Use that motivation to finish something today. 🏁"
        ],
        "lonely": [
            "You’re never truly alone, reach out to someone. 💬",
            "Spend time doing something you love. 🌸",
            "It’s okay to enjoy your own company. ☕",
            "Message an old friend, you’ll make their day. ❤️"
        ]
    }

    # Display mood options
    print("Choose your mood:")
    mood_list = list(moods.keys())

    for i, mood in enumerate(mood_list, start=1):
        print(f"{i}. {mood.capitalize()}")

    #Take user input
    try:
        choice = int(input("Enter the number that matches your mood: "))
        if 1 <= choice <= len(mood_list):
            selected_mood = mood_list[choice - 1]
        else:
            print("Invalid choice. Please run again.")
            return
    except ValueError:
        print("Please enter a valid number next time.")
        return

    #  Show random advice
    advice = random.choice(moods[selected_mood])
    print(f"\n{advice}")

    # Take optional note
    note = input("\nWrite a short note about your day (or press Enter to skip): ")

    # Save data to file
    date = datetime.date.today()
    with open("mood_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{date}] Mood: {selected_mood} _ Note: {note}")

    # Confirmation message
    print("\nSaved! Check 'mood_log.txt' for your past entries.")
    print("\n🌟 Have a great day! 👍")


if __name__ == "__main__":
    main()
