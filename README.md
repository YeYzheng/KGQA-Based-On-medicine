# 基于医药知识图谱的智能问答系统
* 这是一个基于Python模块REfO实现的知识库问答初级系统. 该问答系统可以解析输入的自然语言问句生成 SPARQL 查询，进一步请求后台基于TDB知识库的Apache Jena Fuseki 服务, 进而得到问题的结果。
* 提供疾病症状、疾病用药、药品查询等功能。
* demo演示
![](Image/kgqa-demo-1.png 'Image-1')
![](Image/kgqa-demo-2.png 'Image-2')
# 需要环境
* python3.5.2开发环境
    * 安装jieba中文分词组件
    * 安装sparqlwrapper，python与Apache Jena Fuseki服务的交互组件
    * Django，Web应用框架，用于交互展示
* Apache Jena，是一个开源的Java语义网框架（open source Semantic Web Framework for Java），用于构建语义网和链接数据应用
    * apache-jena-fuseki，开启Apache Jena Fuseki 服务
* Java环境，Apache Jena需要在Java环境下运行
* 数据
    * [TDB药品疾病知识库](https://pan.baidu.com/s/1V7yqs4HKcQYJqDznf2MbSA)   

# 怎么运行
* 下载TDB药品疾病知识库数据 & clone项目代码
* 开启Apache Jena Fuseki 服务
    *  将TDB数据和Apache Jena Fuseki放在同一个目录下。
    *  进入Apache Jena Fuseki文件夹，运行fuseki-server.bat，然后退出。程序为我们在当前目录自动创建“run”文件夹
    *  将项目代码apache_configuration文件夹下的kgdrug.tll和rules.tll文件移动到“run”文件夹下。
        * kgdrug.tll：知识库本体文件
        * rules.tll：规则推理配置文件
    * 将项目代码apache_configuration文件夹下的fuseki_conf.ttl文件移动到“run”文件夹下。
        * fuseki_conf.ttl：Fuseki配置文件，主要配置上述两个文件的路径和TDB知识库路径
    * 上述操作配置好后，再次运行fuseki-server.bat，开启Apache Jena Fuseki 服务
* 安装python环境需要的包
```python
pip install requirements.txt
```
* 这里需要修改项目代码中setting.py文件中的字典导入路劲，因为我们的文件路径可能不一样。
* 运行KB_query文件夹中的query_main.py，开启命令行模式。
```python
python query_main.py
```
* 在项目根目录下运行manage.py,开启项目的web模式
```
python manage.py runserver
```

# 可能遇到的问题
* 第二次开动Apache Jena Fuseki 服务时，如果启动失败，需要到TDB文件把prefix前缀的文件全部删除掉。
* 代码运行错误，应该大部分集中在路径错误上，请仔细阅读报错信息。

# 项目不足
* 只支持一问一答式的对话。
* 只支持查询知识库有的数据，知识库不包含的数据则查询不到。
* 页面UI设计交简陋

# 后期更新
* 加入药品、疾病的同义词，增加系统的鲁棒性
* 增加疾病推断功能
* 增加多轮式对话功能
* 重新设计页面UI

# 参考
[基于 REfO 的 KBQA 实现及示例](http://www.openkg.cn/tool/refo-kbqa)
