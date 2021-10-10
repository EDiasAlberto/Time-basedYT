from googleapiclient.discovery import build
import datetime, pytz
from os import getenv
from dotenv import load_dotenv

timezone = pytz.timezone(' '.join(pytz.country_timezones['gb']))

load_dotenv()
API_KEY = getenv("API_KEY")


def getLink(time):
    videoID = None
    if time is None:
        time = datetime.datetime.now(timezone).strftime("%H:%M")
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(part="snippet", maxResults=1, videoCategoryId=10, q=time, type="video")
    response = request.execute()
    video = response["items"][0]
    vidInfo = {"id": None}
    vidInfo["title"] = video["snippet"]["title"]
    vidInfo["id"] = video["id"]["videoId"]
    if vidInfo["id"] is None:
        print("No video found")
        return None
    return vidInfo


def main():
    vidInfo = getLink()
    print(vidInfo["title"])
    print(f"https://www.youtube.com/watch?v={vidInfo['id']}")

if __name__ == '__main__':
    main()