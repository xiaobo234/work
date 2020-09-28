1、并发开启多个进程，并行开启多个线程
2、pytest.ini:配置文件
1)pytest配置文件可以改变pytest的运行方式，它是一个固定的文件pytest.ini文件，读取配置信息，按指定的方式去运行
非test文件
2)就放在项目根目录下 ，不要乱放，不要乱起其他名字
3)pytest里面有些文件是非test文件
    pytest.ini：pytest的主配置文件，可以改变pytest的默认行为
    conftest.py：测试用例的一些fixture配置
    _init_.py：识别该文件夹为python的package包
marks:
作用：测试用例中添加了 @pytest.mark.webtest 装饰器，如果不添加marks选项的话，就会报warnings
addopts:
作用：addopts参数可以更改默认命令行选项，这个当我们在cmd输入一堆指令去执行用例的时候，就可以用该参数代替了，省去重复性的敲命令工作