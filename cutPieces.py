import os
import json

def main():
    with open("timeline.json",'r', encoding='utf-8') as f:
        data = json.load(f)

    originalName = data["fileName"]
    outputPath= data["outputPath"]
    fileType=data["fileType"]
    times = data["pieces"]
    piecesType=data["piecesType"]

    assert len(times)%2==0
    assert (piecesType=="video" or piecesType=="music")
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)

    for i in range(0,len(times),2):
        startTime = times[i]
        endTime = times[i+1]
        cutPiece(originalName,fileType,startTime,endTime,outputPath,piecesType)

def cutPiece(originalName,fileType,startTime,endTime,outputPath,piecesType):
    # startTime='00:07:42'
    # endTime='00:09:11'
    # originalName='【椎名菜羽】2020年8月录播合集 P4 【20200809】【B限】夏日歌曲演奏会'
    outputName=originalName+' '+startTime.replace(':','_')+'-'+endTime.replace(':','_')

    # os.system('ffmpeg -i ./"%s".flv -ss %s -to %s -acodec copy -vcodec copy ./output/"%s".flv' % (originalName,startTime,endTime,outputName))
    if piecesType=="video":
        os.system('ffmpeg -ss %s -to %s -accurate_seek -i ./"%s".%s -acodec copy -vcodec copy -avoid_negative_ts 1 "%s"/"%s".%s' % (startTime,endTime,originalName,fileType,outputPath,outputName,fileType))
    if piecesType=="music":
        os.system('ffmpeg -ss %s -to %s -accurate_seek -i ./"%s".%s -vn -acodec copy -avoid_negative_ts 1 "%s"/"%s".m4a' % (startTime,endTime,originalName,fileType,outputPath,outputName))

main()