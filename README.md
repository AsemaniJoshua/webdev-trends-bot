by Asemani Joshua

# Web Development Trends Bot

This project is a Python script that automatically fetches the latest web development trends from dev.to and sends them to a specified email address.

## How it works

The script performs the following tasks:

1.  **Fetches Trends:** It uses the `requests` library to fetch the top 3 articles from the dev.to API with the `webdev` tag.
2.  **Formats Email:** It then formats the fetched trends into an HTML email, including the article title, description, image, and share buttons for Twitter, LinkedIn, and Facebook.
3.  **Sends Email:** Finally, it sends the email using `smtplib` to the specified receiver.

## Automation

The script is automated to run daily at 7am GMT using a GitHub Actions workflow defined in `.github/workflows/main.yml`.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/webdev-trends-bot.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up environment variables:**
    The script requires the following environment variables to be set:
    *   `EMAIL`: The email address to send the trends from.
    *   `PASSWORD`: The password for the sender's email account.
    *   `RECEIVER`: The email address to send the trends to.

    You can set these as secrets in your GitHub repository for the GitHub Actions workflow.

## Usage

The script can be run manually:

```bash
python main.py
```

Or it will be run automatically by the GitHub Actions workflow.

by Asemani Joshua
