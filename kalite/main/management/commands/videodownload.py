from django.core.management.base import BaseCommand, CommandError
from kalite.main.models import VideoFile
from kalite.utils.videos import download_video

def download_progress_callback(video):
    def inner_fn(percent):
        if (percent - video.percent_complete) >= 5 or percent == 100:
            if percent == 100:
                video.flagged_for_download = False
                video.download_in_progress = False
            video.percent_complete = percent
            video.save()
    return inner_fn
            

class Command(BaseCommand):
    help = "Download all videos marked to be downloaded"

    def handle(self, *args, **options):
        
        while True: # loop until the method is aborted
            
            if VideoFile.objects.filter(download_in_progress=True).count() > 0:
                self.stderr.write("Another download is still in progress; aborting.\n")
                return
            
            videos = VideoFile.objects.filter(flagged_for_download=True, download_in_progress=False)
            if videos.count() == 0:
                self.stdout.write("Nothing to download; aborting.\n")
                return

            video = videos[0]
            
            video.download_in_progress = True
            video.percent_complete = 0
            video.save()
            
            self.stdout.write("Downloading video '%s'...\n" % video.youtube_id)
            download_video(video.youtube_id, callback=download_progress_callback(video))
            self.stdout.write("Download is complete!\n")