####################################import#####################################
from pytube import YouTube
from pathlib import Path
from tqdm import tqdm
import argparse
from pytube.exceptions import PytubeError, VideoUnavailable


####################################Youtube Downloader#####################################
class YoutubeDownloader:

    def __init__(self,url, quality=None, output_path= None) -> None:
        self.url = url
        self.quality = quality or "highest"
        self.yt = YouTube(
            url=self.url,
            )
        if output_path == None:
            self.output_path = Path().cwd()
        else:
            self.output_path = output_path



    def download(self):

        # check video url is available
        try:
            self.yt.check_availability()
        except VideoUnavailable:
            print("Video is unavaible")
            exit(1)
            
        try:
            if self.quality == "highest":
             stream = self.yt.streams.filter(
                    progressive=True, 
                    file_extension='mp4'
                    ).get_highest_resolution()
            else:    
                stream = self.yt.streams.filter(
                    progressive=True, 
                   file_extension='mp4', 
                   resolution=self.quality
                   ).first()
                        
            # Download the video
            stream.download(self.output_path)
            return stream.default_filename

        except Exception as e:
            print(e)
            exit(1)    





if __name__ == "__main__":

    parser = argparse.ArgumentParser(description= 'Download a YouTube video at a specified quality and output path.')
    parser.add_argument("-u", "--url", help="'The YouTube URL to download'", default="https://www.youtube.com/watch?v=C4YNcqNF4hg")
    parser.add_argument("-q", "--quality", help="The desired video quality (e.g., 720p, 1080p, highest)", default="720p")
    parser.add_argument("-o", "--output_path", help="The output directory to save the video", default=None)
    args = parser.parse_args()


    Y = YoutubeDownloader(
        url=args.url,
        quality=args.quality,
        output_path=args.output_path
        )
    
    Y.download(filename='movie')

