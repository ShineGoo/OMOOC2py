# OMOOC.py 周任务代码试作

## 5w

### diaryRecorder-verSAE-ver0 使用手册

- script for ver0 can be found in _src/om2py4w/5wex0, the files svn to SAE version 
  directory are "index.wsgi" and "config.yaml"

- To find how did I 'upload' those two files to my SAE account, see "教学反转-SAE HowTo" in
  this book
  
- 使用网页版：
  
  - 在浏览器地址栏输入 http://3.agathehello.sinaapp.com/ ，在文本栏内输入新日记的内容，点"submit"按
    钮或按回车键即可提交。文本栏下方是所有过往日记的记录，新提交的日记将出现在记录中。
    
- 使用command line后台服务：

### Note on Database

- 在4w的开发中，选择了安装更方便的sqlite3数据库作为储存日记的载体(for code see 
  ```_src/om2py4w/4wex0/diaryRecorder_server_dbver.py```)，但是在将4w的成果迁移至SAE时发现SAE不
  支持sqlite3,故改用SAE支持的MySQL。
  
- 本书中的"教学反转-SAE HowTo"中描述了如何初始化、管理一个SAE web app对应的MySQL数据库，并描述了对本周
  任务使用到的table "diary0" 的创建。
  
- 使用Python module "MySQLdb"对MySQL database进行操作。


- 私人笔记:
    + wx 后台服务