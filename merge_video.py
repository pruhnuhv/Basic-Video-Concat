from moviepy.editor  import *
import sys

#Very Basic Video editor. You can merge videos of different sizes/resolutions
#using this code all by the CLI. 

flag=input("If you want to merge some video files, press 1. To exit, press 0: \n")
if int(flag)==False:
    sys.exit()

VideoStream=[]
VideoStream.append(VideoFileClip(input('Enter the name/location of the first video clip: ')))

while int(flag)==True:
    clip=VideoFileClip(input('Enter the name/location of the next Video Clip: '))
#    if clip.rotation in (90, 270):                        #Uncomment to not get a squeezed landscape video from a portrait one.
#        clip = clip.resize(clip.size[::-1])
#        clip.rotation = 0
    VideoStream.append(clip)
    flag=input('Press 0 if this was the last file that you wanted to add, press any other numeric key to continue adding files: ')

final_clip=concatenate_videoclips(VideoStream,method='compose')
output=input("What should the name of the output file be? : ") #Asking for name assuming that the files are in the same directory
final_clip.write_videofile(output)
