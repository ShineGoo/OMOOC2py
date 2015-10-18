# Draft for my own tutorials
Quick notes before the tutorials are finalized.
## GitBook "Double Push" issue
###Background
在GitHube repository "https://github.com/janice-lu-zeng/OMOOC2py"（下面简称为```GitHub repo OMOOC2py```）已存在的前提下，注册了GitBook，新建book “https://janice-lu-zeng.gitbooks.io/omooc2py-the-book/” （下面简称```omooc2py the book```），并设定为由```GitHub repo OMOOC2py```直接导入，```omooc2py the book```新建成功。
后来为了调试Disqus插件编辑book.json文件，编辑了```GitHub repo OMOOC2py```中的book.json文件并使用```$ git push origin master```，结果是```GitHub repo OMOOC2py```与```omooc2py the book```中的book.json文件都更新了，且Disqus插件也可以正常使用了（并没有马上==），所以当时得出的结论是```omooc2py the book``` 与 ```GitHub repo OMOOC2py```联动成功。
直到10月18日想要在```ommoc2py the book```中添加新的章节，在```Github repo OMOOC2py```的本地clone中新建了相关md文件并更新了SUMMARY.md文件，并```git pus origin master```，在gitbook.com上新建的md文件无法正常显示（目录根据SUMARRY.md的更新有所更新，但是新建的章节标题在目录中显示为灰色，点击无法显示内容。）在```omooc2py the book```对应的git ```https://git.gitbook.com/janice-lu-zeng/omooc2py-the-book.git```的本地clone中直接做相同的编辑动作并```git push origin master```, 编辑在gitbook.com上生效。由此判断```omooc2py the book```未与```GitHub repo OMOOC2py```完全联动。
所以还是需要弄清楚“Double Push”这件事。
###How I did it
完全按照[这张芝麻星卡片](http://www.iomooc.com/pages/cards.html?packType=like#tip5)背面的步骤来操作的。
  * 现有：```GitHub repo OMOOC2py``` ```https://github.com/janice-lu-zeng/OMOOC2py.git```,```omooc2py the book``` ```https://git.gitbook.com/janice-lu-zeng/omooc2py-the-book.git```
  * 并已将```GitHub repo OMOOC2py``` clone 至本地，路径为```/Users/apple/Documents/gitHub/OMOOC2py```
  * 在terminal中输入
  ```
  ~ apple$ cd /Users/apple/Documents/gitHub/OMOOC2py 
  OMOOC2py apple$ git remote -v
  ```
  terminal中返回
  ```
  origin	https://github.com/janice-lu-zeng/OMOOC2py.git (fetch)
  origin	https://github.com/janice-lu-zeng/OMOOC2py.git (push)
  ```