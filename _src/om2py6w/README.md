# OMOOC.py 周任务代码试作

## 6w

### diaryRecorder-verWEIXIN-ver0 使用手册

- 关注测试公众号。
  ![snapshot1](/screenshots/QRcode.jpeg)

- 关注后用户收到欢迎信息。按信息中的说明，用户输入'read'将会收到目前所有日记的记录。用户输入'write'将会
  收到信息“Send me your new line of diary.", 用户随后输入想记录的文本，发送后若文本保存成功将收到回复
  "Your new dairy has been saved"。
  ![snapshot1](/screenshots/weixin_1.jpg)
  ![snapshot1](/screenshots/weixin_1.jpg)
  
- 新日记保存成功后，可输入'read' 查看更新后的日记本，或在浏览器访问 http://3.agathehello.sinaapp.com/
  查看。

- script for ver0 can be found in _src/om2py6w/6wex0, the files svn to SAE version 
  directory are "index.wsgi", "tpl.py" and "config.yaml".
  
- exported mysql database used can be found in _src/om2py6w/6wex0, the two tables used are
  directory are "menu0.sql" and "diary0.sql".
  
  
### 开发中遇到的问题

- 如果用户在公众号中输入了一条过长的日记，则再在公众号输入“read”则无法正常反馈现有日记记录，但是仍可以写入
  新日记，web端读写也正常。"过长的日记"截图如下:
  ![snapshot1](/screenshots/weixin_error.png)

  

- 私人笔记:
    + 移动 web 应用