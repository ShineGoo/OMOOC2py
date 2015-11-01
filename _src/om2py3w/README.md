# OMOOC.py 周任务代码试作

## 3w

- 私人笔记:
    + UDP 网络服务
    + HTTP 服务端

### diaryRecorder-verNET-ver1 使用手册

- src for ver1 can be found in _src/om2py3w/3wex0

- 将脚本文件 diaryRecorder_server.py与保存有过往日记的文本文件myDiary.txt保存于同一文件夹中。

- 在terminal中进入diaryRecorder\_server.py所在的文件夹，
  在terminal中输入```$ python diaryRecorder_server.py```

- 在一个新打开的terminal中进入diaryRecorder\_client.py所在的文件夹，
  在terminal中输入```$ python diaryRecorder_client.py``` 

- 在运行client的terminal中，过往日记内容将被打印。

- 在运行client的terminal中，按提示在输入窗口输入新日记内容，点“Submit"提交新日记，
  这行内容将被写入myDiary.txt中，并在运行server的terminal窗口中显示。

- 在运行client的terminal窗口中，新内容被存储后按提示输入“y“则可再次写入新的日记，
  输入任何其他内容退出client程序。