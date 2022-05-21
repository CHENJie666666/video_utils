# video_utils
Some useful utils for common video processing

## 1. 视频基本处理





## 2. 视频轨中的音频处理

### 2.1 MP4文件提取MP3

#### moviepy

提取MP4文件的MP3音频

- 安装包

```shell
pip install moviepy
```

- 单个mp4文件转化，调用`mp4_to_mp3.py`文件

```shell
python mp4_to_mp3.py -s 'a.mp4' 
```

- 多个mp4文件转化，调用`mp4_to_mp3.py`文件

```shell
python mp4_to_mp3.py -s 'mp4_dir' 
```



### 2.2 删除视频中的音频轨

#### moviepy

删除视频文件中的音频

- 安装包

```shell
pip install moviepy
```

- 单个视频文件转化，调用`video_remove_audio.py`文件

```shell
python video_remove_audio.py -v 'a.mp4'
```

- 多个视频文件转化，调用`video_remove_audio.py`文件

```shell
python video_remove_audio.py -v 'mp4_dir' -s 'new_mp4_dir'
```



### 2.3 合并无声视频和音频

#### moviepy

合并无声视频文件和音频文件

- 安装包

```shell
pip install moviepy
```

- 单个视频文件和音频文件合并，调用`video_add_audio.py`文件

```shell
python video_add_audio.py -v 'a.mp4' -a 'a.mp3'
```

- 多个视频文件转化，调用`video_add_audio.py`文件

```shell
python video_add_audio.py -v 'mp4_dir' -a 'mp3_dir' -s 'new_mp4_dir'
```

