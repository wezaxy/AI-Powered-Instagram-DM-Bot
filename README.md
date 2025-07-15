
# AI-Powered Instagram DM Bot

This project is an **AI-powered Instagram Direct Message (DM) bot** that automatically responds to Instagram DMs using artificial intelligence. It uses GPT models to process and generate responses to the latest DM messages received.

## Features

- **Automated Direct Messaging**: Automatically reads and replies to Instagram DMs.
- **AI-Powered Responses**: Uses GPT to generate AI-based replies to messages.
- **Proxy Support**: Allows the use of proxy servers for safe and anonymous interaction.
- **Group Message Control**: Optionally enable or disable responses to group messages.
- **Language Support**: Configure the language of the AI responses.

## Prerequisites

Before running the bot, make sure you have the following installed:

- Python 3.7 or higher
- A valid Instagram account (and login credentials)
- Proxy (optional)

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/wezaxy/ai-powered-instagram-dm-bot.git
   cd ai-powered-instagram-dm-bot
   ```

2. **Install Dependencies**:

   Run the following command to install the required dependencies:

   ```bash
   python install.py
   ```

   This script will automatically install all the necessary libraries for you.

3. **Create Configuration File**:

   In the project directory, you'll need to edit the `config.json` file. This file contains the necessary settings for the bot.

   **Example `config.json`**:

   ```json
   {
     "username": "wezaxyy",
     "password": "your password",
     "language": "turkish",
     "use_proxy": true,
     "group_messages": false
   }
   ```

   - **username**: Your Instagram username.
   - **password**: Your Instagram password.
   - **language**: Set the language for AI responses (e.g., "english", "turkish").
   - **use_proxy**: Set to `true` if you want to use a proxy, otherwise `false`.
   - **group_messages**: Set to `true` if you want the bot to respond to group messages, otherwise `false`.

4. **Add Proxies (Optional)**:

   If you're using proxies, you should add them in the `proxies.txt` file, one per line, in the following format:

   ```
   username:password@proxy_host:proxy_port
   ```

## Usage

Once the setup is complete, you can start the bot by running:

```bash
python main.py
```

### How the Bot Works

- The bot logs into your Instagram account.
- It checks the latest messages in your Instagram DMs.
- If the message is from you (the bot owner), it ignores it.
- If the message is from someone else, it sends the message to an AI model (like GPT).

### Key Files:

- **`install.py`**: Installs required modules and sets up the environment.
- **`main.py`**: The main bot script that runs the DM response automation.
- **`config.json`**: Configuration file where you set your Instagram credentials and bot preferences.
- **`proxies.txt`**: (Optional) A file for proxy settings.

## Notes

- This project is intended for educational purposes only. I am not responsible for any issues, account suspensions, or other problems that may occur.
- Be cautious when using your personal Instagram account with this bot. It’s recommended to use a secondary account.
- Ensure you comply with Instagram's terms of service to avoid account suspension.
- The bot can be modified to add more features, such as handling comments or other message types.

## Contact

For assistance or business inquiries, you can reach me on:

- **Discord**: wezaxy
- **Signal**: wezaxy.43
- **Telegram**: [@wezassy](https://t.me/wezassy)
https://discord.gg/c44FB4PFcW
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
