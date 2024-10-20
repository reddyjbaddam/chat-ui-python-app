import openai
import tkinter as tk
from tkinter import scrolledtext

# Set up OpenAI API key
openai.api_key = 'XYZ'

# Function to call ChatGPT API
def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # You can switch to 'gpt-4' if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"


# Function to send the message from the user and get the response
def send_message(event=None):
    user_input = entry_box.get("1.0", "end").strip()

    if user_input:
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"You: {user_input}\n", "user")
        chat_history.see(tk.END)

        # Get response from GPT
        bot_response = get_gpt_response(user_input)
        chat_history.insert(tk.END, f"Bot: {bot_response}\n", "bot")
        chat_history.see(tk.END)

        # Clear the input box after sending
        entry_box.delete("1.0", "end")
        chat_history.config(state=tk.DISABLED)


# GUI setup using Tkinter with a modern, clean look
root = tk.Tk()
root.title("ChatGPT Bot - Fancy UI")
root.geometry("600x700")
root.configure(bg="#2C2C2C")

# Style variables
font_style = ("Arial", 12)
bg_color = "#2C2C2C"
text_color = "#F1F1F1"
button_color = "#4CAF50"
button_hover_color = "#45A049"
entry_bg_color = "#3A3A3A"
entry_fg_color = "#FFFFFF"

# Chat history window
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', bg=bg_color, fg=text_color,
                                         font=font_style, height=20)
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_history.tag_config("user", foreground="lightblue")
chat_history.tag_config("bot", foreground="lightgreen")

# User input box
entry_frame = tk.Frame(root, bg=bg_color)
entry_frame.pack(padx=10, pady=10, fill=tk.X)

entry_box = tk.Text(entry_frame, height=3, bg=entry_bg_color, fg=entry_fg_color, font=font_style, relief=tk.FLAT)
entry_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
entry_box.bind("<Return>", send_message)


# Send button
def on_button_hover(event):
    send_button.config(bg=button_hover_color)


def on_button_leave(event):
    send_button.config(bg=button_color)


send_button = tk.Button(entry_frame, text="Send", command=send_message, bg=button_color, fg="white", font=font_style,
                        relief=tk.FLAT, padx=20)
send_button.pack(side=tk.RIGHT, padx=10, pady=5)
send_button.bind("<Enter>", on_button_hover)
send_button.bind("<Leave>", on_button_leave)

# Make pressing "Enter" key also send the message
entry_box.bind("<Shift-Return>", lambda event: None)  # Allows for multi-line input with Shift+Enter
entry_box.bind("<Return>", send_message)

# Start the Tkinter GUI loop
root.mainloop()
