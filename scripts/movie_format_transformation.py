from moviepy.editor import *

class Moviepy_method():
    def __init__(self,path1,path2,path3="‪J:\vedio",path4 = "‪J:\vedio\original"):
        self.input_path = path1.strip("\u202a")
        self.path2 = path2.strip("\u202a")
        self.path3 = path3.strip("\u202a")
        self.path4 = path4.strip("\u202a")



    def getvideo(self,start_time,end_time):
        """视频提取"""
        vedio1 = VideoFileClip(self.input_path)
        # vedio2 = vedio1.without_audio()
        video2 = vedio1.subclip(start_time, end_time)
        # video4 = vedio2.subclip(9,-1)
        video2.write_videofile(self.path2)




    def video_concat(self):
        """视频合成"""
        video1 = VideoFileClip(self.input_path).fx(vfx.resize, width=848)
        video2 = VideoFileClip(self.path2).fx(vfx.resize, width=848)
        video3 = VideoFileClip(self.path3).fx(vfx.resize, width=848)
        # video4 = VideoFileClip(path4)
        final_clip = concatenate_videoclips([video1, video2, video3], method="compose")
        final_clip.to_videofile(self.path4, fps=24, remove_temp=False)

    def audio_concat_vedio(self,audio_path):
        """音频视频合成"""
        video = VideoFileClip(self.path)
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)  # 不能直接是audio的路径
        video.write_videofile(self.path2)
