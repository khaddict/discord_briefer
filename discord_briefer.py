'''
DiscordBriefer is a tool that sends ChatGPT the last 100 messages from a Discord channel and summarizes them for you in a few lines.
Limitations : Discord API can get the 100 last messages only
'''
import json
import os
import argparse
import requests
import openai
import pyfiglet

discord_briefer = pyfiglet.figlet_format("DiscordBriefer")
print(discord_briefer)

def get_openai_token():
    """
    Get OpenAI API token
    The following environement variables need to be set :
        - OPENAI_TOKEN
    """
    openai_token = os.environ['OPENAI_TOKEN']
    return openai_token

def get_discord_token():
    """
    Get Discord API token
    The following environement variables need to be set :
        - DISCORD_TOKEN
    """
    discord_token = os.environ['DISCORD_TOKEN']
    return discord_token

def get_discord_messages(channel_id, messages_limit):
    """
    Get Discord messages
    """
    discord_authorization_token = get_discord_token()
    headers = {
        'authorization': discord_authorization_token
    }
    response = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={messages_limit}", headers=headers, timeout=10)
    json_response = json.loads(response.text)
    chat = []
    for i in json_response:
        chat.append(f"{i['author']['username']} : {i['content']}")
    return chat[::-1]

def send_response_to_openai(chat, language):
    """
    Send response to OpenAI
    """
    if language == 'french':
        entrypoint = "Bonjour, résume moi la conversation suivante en quelques lignes : "
    else:
        entrypoint = "Hello, summarize the following conversation for me in a few lines : "
    openai_token = get_openai_token()
    openai.api_key = openai_token
    prompt = entrypoint + str(chat)
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

def main(args):
    """
    Main function
    """
    language = args.language
    channel_id = args.channel_id
    messages_limit = args.messages_limit

    chat = get_discord_messages(channel_id, messages_limit)
    print(send_response_to_openai(chat, language))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-ci', '--channel_id', type=int, help="[REQUIRED] Channel ID. Example : 453414355414185992", required=True)
    parser.add_argument('-l', '--language', type=str, help="[NOT REQUIRED] Answer language (english/french). default=english", required=False, default="english")
    parser.add_argument('-ml', '--messages_limit', type=int, help="[NOT REQUIRED] Messages limit (1 < x < 100). default=50", required=False, default=50)
    args = parser.parse_args()
    main(args)
