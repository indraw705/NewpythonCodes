# organize the desktop
# moves images, videos, screenshots, and audio files
# into corresponding folders
import os
import shutil


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf", ".avi")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

doc = (".pdf", ".csv", ".xlsx", ".pdf", ".zip", ".docx", "ps1", ".txt", ".json", )

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_doc(file):
    return os.path.splitext(file)[1] in doc


def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

os.chdir("C:\\Users\\inarvekar\\Desktop")
os.getcwd()

for file in os.listdir():
    if is_audio(file):
        shutil.move(file, "C:\\Users\\inarvekar\\Desktop\\audio")
    elif is_video(file):
        shutil.move(file, "C:\\Users\\inarvekar\\Desktop\\video")
    elif is_doc(file):
        shutil.move(file, "C:\\Users\\inarvekar\\Desktop\\Documents")
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, "C:\\Users\\inarvekar\\Desktop\\screenshots")
        else:
            shutil.move(file, "C:\\Users\\inarvekar\\Desktop\\images")
    else:
        shutil.move(file, "C:\\Users\\inarvekar\\Desktop\\documents1")