from youtube_downloader import YoutubeDownloader
from pytube import YouTube
from pathlib import Path
from tqdm import tqdm
import argparse
from pytube.exceptions import PytubeError, VideoUnavailable
import streamlit as st
import os

def Download(link, quality):

    Y = YoutubeDownloader(
        url=link,
        quality=quality,
        output_path="./video"
        )

    file = Y.download()
    



st.markdown("<h1> &nbsp  &nbsp  &nbsp  &nbsp  &nbsp YouTube Video Downloader </h1>",unsafe_allow_html=True)
st.image("src/images/imge01.PNG", )
link = st.text_input("Url", "Paste your video link here")
quality = st.selectbox("Quality", options=("480p", "720p", "1080p"))
col1, col2, col3,  col4, col5 =st.columns(5)
btn = col3.button("Download", on_click= lambda : Download(link, quality))


