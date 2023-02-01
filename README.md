# Reddit ChatGPT Bot(Unofficial API)
Uses API by [PawanOsman](https://github.com/PawanOsman/PyGPT)

# Disclaimer
This is not open source. [PawanOsman](https://github.com/PawanOsman/) can see all your requests and your session token.
`
# Prerequisites
- Reddit account and reddit App, more infomation here [Reddit Bot QuickStart](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html)
- OpenAi ChatGPT account or ChatGPT session

# Usage
1. Update global_constants.py variables with your own info
2. execute script
    ```
    python3 chat_gpt_reply.py
    ```
    or excute script in background
    ```
    nohup python3 -u chat_gpt_reply.py > nohup.out 2>&1 &
    ```
3. watch logs
    ```
    tail -30f nohup.out
    ```
4. The script will monitor target subs latest comments start with ai, wait ChatGPT response, and reply it. E.g. ai What ai What can u do
    ```
    comment.body ai What can u do
    comment.author Select-University338
    Connected to server
    Ready!!
    answer:
    As a language model, I can generate human-like text based on the input I receive. I can answer questions, provide explanations, write creative content, summarize information, and perform many other language-related tasks. Just ask me anything you'd like to know!
    Disconnected from server
    --------------------------
    ```
