"""
功能：
1. 获取视频基本信息
2. 视频格式转换
3. 视频帧率调节
4. 视频分辨率调节
"""
# ffmpeg安装
# pip install ffmpeg-python
# https://ffmpeg.org/download.html#build-windows下载ffmpeg安装包，安装后将其添加至环境变量


import ffmpeg

def get_video_info(video_path):
    """
    获取视频基本信息：包括帧宽、帧高、帧数、视频比特率、视频帧率、视频大小、视频时长
    参数：
        video_path: 视频路径
    """
    probe = ffmpeg.probe(video_path)
    print(probe)
    format = probe['format']
    bit_rate = int(format['bit_rate']) / 1000
    duration = format['duration']
    size = int(format['size']) / 1024 / 1024
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    
    if video_stream is None:
        print('No video stream found!')
        return
    
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    num_frames = int(video_stream['nb_frames'])
    fps = int(video_stream['r_frame_rate'].split('/')[0])/int(video_stream['r_frame_rate'].split('/')[1])
    duration = float(video_stream['duration'])
    
    print('帧宽 width: {}'.format(width))
    print('帧高 height: {}'.format(height))
    print('帧数 num_frames: {}'.format(num_frames))
    print('视频比特率 bit_rate: {}k'.format(bit_rate))
    print('视频帧率 fps: {}'.format(fps))
    print('视频大小 size: {}MB'.format(size))
    print('视频时长 duration: {}'.format(duration))

    return width, height, num_frames, bit_rate, fps, size, duration


def videl_format_transformation(input, output):
    """
    视频格式转换：支持.avi/.mp4/.mpeg/.wmv/.rmvb/.m4v/.mov/.asf/.flv/.f4v/.rmvb/.rm/.3gp/.vob等格式
    参数：
    input: 输入文件
    output: 输出文件
    """
    (
        ffmpeg
        .input(input)
        .output(output)
        .global_args('-loglevel', 'warning')
        .run()
    )


def fps_adjust(src_video_path, dst_video_path, fps):
    """调整视频帧率"""
    source_video = ffmpeg.input(src_video_path)
    out = source_video.output(dst_video_path, r=fps)
    # out.run()
    out.global_args('-loglevel', 'warning').run()

def resolution_adjust(src_video_path, dst_video_path, height, width):
    """调整视频分辨率"""
    source_video = ffmpeg.input(src_video_path)
    out = source_video.output(dst_video_path, s=str(width) + 'x' + str(height))
    # out.run()
    out.global_args('-loglevel', 'warning').run()


def horizontal_combine():
    pass

def vertical_combine():
    pass



if __name__ == "__main__":
    
    # video_path = 'C:/Users/27110/Desktop/欢喜 520.mp4'
    video_path = '1.mp4'
    # 获取视频基本信息
    get_video_info(video_path)
    # 视频格式转换
    # videl_format_transformation(video_path, '5.mp4')
    # # 视频帧率调节
    # fps_adjust('1.mp4', '1_fps15.mp4', 15)
    # # 视频分辨率调节
    # resolution_adjust('1.mp4', '1_re.mp4', 640, 360)
