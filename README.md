# DiscordBriefer
DiscordBriefer is a tool that sends ChatGPT the last 100 messages from a Discord channel and summarizes them for you in a few lines.

Context : You were AFK 30 min and you have 300 unread messages on a Discord channel. You still want to discuss but you have no idea what people were talking about. ChatGPT can help you put yourself back in context !

![mogwhite_idea](https://github.com/khaddict/discord_briefer/assets/139250194/59ca489c-10de-429a-96fc-dbe3513ed63f)

Tested on Windows 11 Pro & Debian 11

## I) Get your Discord token

To get your Discord token, you have to enable the developper mode on your application.

### 1) Windows
- `WIN + R`
- `appdata`
- → Roaming → discord → settings.json
- Add one line :
  ```
  "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING": true
  ```
- Restart Discord
- `CTRL + SHIFT + I` → Network → get a request (ack for example) and get the content of `authorization`

## II) Get your OpenAI token

https://platform.openai.com/api-keys

## III) Setup environment variables

### 1) Windows (PowerShell console)
- `setx OPENAI_TOKEN "your_token"`
- `setx DISCORD_TOKEN "your_token"`

  If you are working on an IDE, you have to restart it to set the environment variables.
  After doing it, you can check if the variables are set :
- `Get-ChildItem Env:`

### 2) Linux
a) You can put the environment variables in your .bashrc file & reload your bash :
  ```
  export OPENAI_TOKEN="your_token"
  export DISCORD_TOKEN "your_token"
  ```
- `bash`

b) You can also export them :
- `export OPENAI_TOKEN="your_token"`
- `export DISCORD_TOKEN="your_token"`

## IV) Get the channel ID
For a specific channel in a Discord server :

![image](https://github.com/khaddict/discord_briefer/assets/139250194/4bdf58f6-3360-46f4-93bb-88d7e62c4167)

For private messages :

![image](https://github.com/khaddict/discord_briefer/assets/139250194/ff644310-a93a-4fe2-bdec-998053ccff1e)

##  V) Clone the repo & install the modules

### :warning: Best practice is to install everything in a virtual environment. :warning:

- `git clone https://github.com/khaddict/discord_briefer.git`
- `cd discord_briefer`
- `pip install -r requirements.txt`
- `python3 discord_briefer.py --help`
```
 ____  _                       _ ____       _       __
|  _ \(_)___  ___ ___  _ __ __| | __ ) _ __(_) ___ / _| ___ _ __ 
| | | | / __|/ __/ _ \| '__/ _` |  _ \| '__| |/ _ \ |_ / _ \ '__|
| |_| | \__ \ (_| (_) | | | (_| | |_) | |  | |  __/  _|  __/ |   
|____/|_|___/\___\___/|_|  \__,_|____/|_|  |_|\___|_|  \___|_|   

usage: discord_briefer.py [-h] -ci CHANNEL_ID [-l LANGUAGE] [-ml MESSAGES_LIMIT]

options:
  -h, --help            show this help message and exit
  -ci CHANNEL_ID, --channel_id CHANNEL_ID
                        [REQUIRED] Channel ID. Example : 453414355414185992
  -l LANGUAGE, --language LANGUAGE
                        [NOT REQUIRED] Answer language (english/french). default=english
  -ml MESSAGES_LIMIT, --messages_limit MESSAGES_LIMIT
                        [NOT REQUIRED] Messages limit (1 < x < 100). default=50
```

Command example : `python3 discord_briefer.py -ci 453414355414185992 -l french -ml 80`
