# OMOOC.py 周任务代码试作

## 4w

### diaryRecorder-verWeb-ver0 使用手册

- script for ver0 can be found in _src/om2py4w/4wex0

- 将脚本文件 diaryRecorder_server.py与保存有过往日记的文本文件myDiary.txt保存于同一文件夹中。
  此脚本文件与作为例子的txt日记本均可在 _src/om2py4w/4wex0 中被找到。

- 在terminal中进入diaryRecorder\_server.py所在的文件夹，
  在terminal中输入```$ python diaryRecorder_server.py```
  
- 使用网页版：
  
  - 在浏览器地址栏输入 http://localhost:8080/diary ，在文本栏内输入新日记的内容，点"submit"按钮或
    按回车键即可提交。文本栏下方是所有过往日记的记录，新提交的日记将出现在记录中。
    
- 使用command line版：

  - 在一个新打开的terminal中进入diaryRecorder\_client.py所在的文件夹，
    在terminal中输入```$ python diaryRecorder_client.py``` 

  - 在运行client的terminal中，过往日记内容将被打印。

  - 在运行client的terminal中，按提示输入新日记内容，按回车提交新日记。

  - 在运行client的terminal窗口中，新内容被存储后输入“y“则可再次写入新的日记，
    输入任何其他内容退出client程序。
    
#### 使用截图

- Web version

![snapshot1](/screenshots/w4_web.png)

- CLI version

![snapshot1](/screenshots/w4_cli.png)

### diaryRecorder-verWeb-ver1
Update ver 0 by replacing myDiary.txt with myDiary.db.

- Reason for this update is that in order to create a 'real' web application
  (other than one that works locally on localhost), it is both reasonable and
  necessary to save data in a database.
  
- ```sqlite3``` is used to do relevant database programming.

- scripts for ver1 reside in the same directory as those for ver0: _src/om2py4w/4wex0
  [server script] (http:....)
  [client script] (haven't started yet ><)
  
- The functionality and appearance of ver1 is identical to ver0 so I haven't made 
  any screenshots for this version. With the external look of the application
  remains unchanged, data involved are now stored in a much more structural way. 


## Next Steps  
- 私人笔记:
 + SAE 发布服务
 + web 页面端口
 + 用户认证
 
