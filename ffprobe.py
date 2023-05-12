import ffmpeg

def scale_with_padding(input_file, output_file):

    try:
        # Probe the input file to get information about its streams
        probe = ffmpeg.probe(input_file)

        # Extract the first video stream from the probe
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)

        # Get the input video resolution from the video stream
        width = int(video_stream['width'])
        height = int(video_stream['height'])

        # Check if scaling is necessary
        if width >= 1920 and height >= 1080:
            # Calculate the amount of padding needed to center the video object within the 1080x1920 frame
            padding_height = int((height - 1920) / 2)

        # Apply padding filter using FFmpeg
            (
                ffmpeg
                .input(input_file)
                .filter('pad', w=1920, h=1080, x=0, y=padding_height, color='black')
                .filter('fps', fps=video_stream['avg_frame_rate'])
                .output(output_file, pix_fmt='yuv420p', aspect='1920:1080', sws_flags='bilinear')
                .overwrite_output()
                .run()
            )

        else:
            print(f"Video successfully processed and saved to {output_file}")
        return  output_file

    except ffmpeg.Error as e:\
    print(f"An error occurred while processing the video: {e.stderr.decode()}")

if __name__ == '__main__':
    scale_with_padding('car.mp4', 'video.mp4')