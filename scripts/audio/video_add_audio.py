"""
功能：合并无声视频文件和音频文件
"""

from moviepy.editor import VideoFileClip, AudioFileClip
import os
import argparse

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="实现mp4文件向mp3文件的转换")

    parser.add_argument("-v", "--video_file", type=str, 
                            help="目标视频文件所在目录或路径")
    parser.add_argument("-a", "--audio_file", type=str, 
                            help="目标音频文件所在目录或路径")
    parser.add_argument("-s", "--save_file", type=str, default=None,
                            help="保存文件所在目录或路径")

    args = parser.parse_args()
    return args

def add_audio(video_path, audio_path, save_path=None):
    """
    向单个无声视频文件中添加音频文件
    参数：
        video_path：视频文件所在路径
        audio_path: 音频文件所在路径
        save_path: 保存视频路径
    """ 
    if not save_path:
        save_path = video_path.rsplit('.', 1)[0] + '_add_audio.' + video_path.rsplit('.', 1)[1]

    video = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    video = video.set_audio(audio_clip)
    video.write_videofile(save_path)

def multi_add_audio(video_dir, audio_dir, save_dir=None):
    """
    多个视频文件添加多个音频文件生成多个视频（需保证源视频和源音频同名）
    参数：
        video_dir：视频文件所在目录
        audio_dir: 音频文件所在目录
        save_dir: 保存视频目录
    """
    video_files = os.listdir(video_dir)
    audio_file_path = [os.path.join(audio_dir, file) for file in video_files]

    if not save_dir or save_dir == video_dir:
        save_files = [i.rsplit('.', 1)[0] + '_add_audio.' + i.rsplit('.', 1)[1] for i in video_files]
        save_path = [os.path.join(video_dir, file) for file in save_files]
    
    else:
        save_path = [os.path.join(save_dir, file) for file in video_files]

    for i in range(len(video_files)):
        
        try:
            add_audio(
                os.path.join(video_dir, video_files[i]), 
                audio_file_path[i], 
                save_path[i])  
        
        except:
            print(f'{video_files[i]} add audio failed')



if __name__ == '__main__':
    
    args = argv_parse()
    
    if os.path.isfile(args.video_file):
        # 单个文件合并
        add_audio(args.video_file, args.audio_file, args.save_file)
    
    if os.path.isdir(args.video_file):
        # 多个文件合并
        multi_add_audio(args.video_file, args.audio_file, args.save_file)
