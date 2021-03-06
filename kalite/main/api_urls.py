from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('main.api_views',

    # toss out any requests made to actual KA site urls
    url(r'^v1/', lambda x: HttpResponse("{}")),
    
    url(r'^save_video_log$', 'save_video_log'),
    url(r'^save_exercise_log$', 'save_exercise_log'),

    url(r'^get_video_logs$', 'get_video_logs'),
    url(r'^get_exercise_logs$', 'get_exercise_logs'),

    url(r'^start_video_download$', 'start_video_download'),
    url(r'^check_video_download$', 'check_video_download'),
    url(r'^get_topic_tree$', 'get_topic_tree'),
    url(r'^get_video_download_list$', 'get_video_download_list'),
    
    url(r'^start_subtitle_download$', 'start_subtitle_download'),
    url(r'^check_subtitle_download$', 'check_subtitle_download'),
    url(r'^get_subtitle_download_list$', 'get_subtitle_download_list'),
    url(r'^cancel_downloads$', 'cancel_downloads'),
    url(r'^delete_videos$', 'delete_videos'),
)
