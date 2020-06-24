from moviepy.editor  import VideoFileClip, concatenate_videoclips
import sys
flag=input("If you want to merge some video files, press 1. To exit, press 0: \n")
if int(flag)==False:
    sys.exit()
VideoStream=[]
VideoStream.append(VideoFileClip(input('Enter the name/location of the first video clip: ')))
while int(flag)==True:
    clip=VideoFileClip(input('Enter the name/location of the next Video Clip: '))
    VideoStream.append(clip)
    flag=input('Press 0 if this was the last file that you wanted to add, press any other key to continue adding files: ')

final_clip=concatenate_videoclips(VideoStream)
output=input("What should the name of the output file be? : ")
final_clip.write_videofile(output)
