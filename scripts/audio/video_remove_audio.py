"""
功能：删除视频中的音频文件
"""

from moviepy.editor import VideoFileClip
import argparse
import os

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="删除视频中的音频文件")

    parser.add_argument("-v", "--video_file", type=str, 
                            help="目标文件所在目录或路径")
    parser.add_argument("-s", "--save_file", type=str, default=None,
                            help="目标文件所在目录或路径")

    args = parser.parse_args()
    return args

def remove_audio(video_path, save_path=None):
    """
    视频无声化处理
    参数：
        video_path: 源视频路径
        save_path: 保存视频路径
    """
    if not save_path:
        save_path = video_path.rsplit('.', 1)[0] + '_remove_audio.' + video_path.rsplit('.', 1)[1]

    video = VideoFileClip(video_path)
    video = video.without_audio()
    video.write_videofile(save_path)

def multi_remove_audio(video_dir, save_dir=None):
    """
    将目录下的视频文件全部转为无声视频
    参数：
        video_path: 源视频目录
        save_path: 保存视频目录
    """
    video_files = os.listdir(video_dir)  # 后续添加对视频文件的判断

    if not save_dir:
        save_dir = video_dir
        save_path = [os.path.join(save_dir, file.rsplit('.', 1)[0] + '_silent.' + \
            file.rsplit('.', 1)[1]) for file in video_files]
    
    else:
        save_path = [os.path.join(save_dir, file) for file in video_files]


    for i in range(len(video_files)):
        
        try:
            remove_audio(os.path.join(video_dir, video_files[i]), save_path[i])
        except:
            print(f'{video_files[i]} trnasformation failed')


if __name__ == '__main__':
    
    args = argv_parse()
    
    if os.path.isfile(args.video_file):
        # 单个文件处理
        remove_audio(args.video_file, args.save_file)
    
    if os.path.isdir(args.video_file):
        # 文件批量处理
        multi_remove_audio(args.video_file, args.save_file)
