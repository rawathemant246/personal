import ffmpeg

import sys

sys.path.append(r'C:\Program Files\ffmpeg-2023-05-08-git-2d43c23b81-essentials_build\bin') #path of ffmpeg


stream = ffmpeg.input('car.mp4')

stream = stream.trim(start =0, duration = 5).filter('setpts', 'PTS-STARTPTS')

stream = ffmpeg.output(stream, 'output.mp4')

ffmpeg.run(stream)