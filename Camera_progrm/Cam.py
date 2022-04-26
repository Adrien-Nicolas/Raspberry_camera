import time
import os
os.system("raspivid -o – -t 0 -n | cvlc -vvv stream:///dev/stdin –sout ' #rtp{sdp=rtsp://:8554/}' :demux=h264")