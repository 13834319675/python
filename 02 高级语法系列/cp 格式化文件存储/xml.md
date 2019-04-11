# 结构化文件存储
- xml,json
- 为了解决不同设备之间的切换
- xml
- json
# xml文件
- 参考资料
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285

- XML(eXtensibleMarkupLanguage)， 可扩展标记语言
    - 标记语言： 语言中使用尖括号括起来的文本字符串标记
    - 可扩展：用户可以自己定义需要的标记
    - 例如：
            
            <Teacher> 
                自定义标记Teacher
                在两个标记之间任何内容都应该跟Teacher相关
            </Teacher>
            
    - 是w3c租住规定的一个标准
    - xml描述的事数据本身,即数据的结构和语义
    - HTML侧重于如何显示web页面中的数据
- xml文档的构成
    - 处理指令(可以认为一个文件内只有一个处理指令)
        - 最多只有一行
        - 切必须在第一行
        - 内容是与xml本身处理相关的一些声明或者指令
        - 以xml关键字开头
        - 一般同于声明xml的版本和采用的编码
            - version(版本)属性是必须的
            - encoding属性用来致辞xml解析器使用的编码
        -根目录(一个文件内只有根目录)
            - 在整个xml文件中,可以把它看做一个树形结构
            - 根元素有且只有一个
        - 子元素
        - 属性
        - 内容
            - 表明标签存储的信息
        - 注释
            - 起说明作痛的信息
            - 注释不能嵌套在标签里
            - 只有在注释的开始和结尾使用短横线
            
            
                <name> <!-- wangdapeng -->   </name> #可以
                <name <!-- wangdapeng -->>   </name> #不可以，注释在标签内
                
                <!--my-name-by-wang--> #可以，注释内容可以有一个短横线
                <!--my--name--by--wang-->#不可以，双短横线只能出现在开头或结尾
                
                <!---my-name--> #可以， 三短横线只能出现在开头
                <!---my-name---> #不可以， 三短横线只能出现在开头
                
 
- 保留字符的处理
    - xml中视同的符号跟字符可能跟实际符号字符相冲突,典型的事左右尖括号
    - 使用实体引用    
    
    
        <score>csore>88</> #有错误 不能出现
        <score> score&gt;80</score> #使用实体引用
         
- 把含有保留字符的部分放在CDATA块内部，CDATA块把内部信息视为不需要转义
                  
      
      <![CDATA[
         select name,age
         from Student
         where score>80
         ]]>
- 常用的需要转移的保留字符和对应实体引用
    
    
        - &:&amp;
        - <:&lt;
        - >:&gt;
        - ':&apos;
        - ":&quot;
        - 一共五个， 每个实体引用都以&开头并且以分号结尾
 
- xml标签的命名规则
    - Pascal命名法
    - 用单词表示 第一个字母大写
    - 大小写严格区分
    - 配对的标签必须一致
    
- 命名空间
    -为了防止命名冲突
    
    
        <Student>
            <Name>chenpeng</Name>
            <Age>18</Age>
        </Student>
        <Room>
            <Name>zhangsan</Name>
            <Location>1111</Location>
        </Room>
- 如果归并上述两个内容信息，会产生冲突
    
              
              <Schooler>
                        <Name>LiuYing</Name>
                        <Age>23</Age>
                    <Name>2014</Name>
                    <Location>1-23-1</Location>
                </Schooler>
                      
- 为了避免冲突，需要给可能冲突元素添加命名空间
- xmlns: xml name space 的缩写
    
    
              <Schooler xmlns:student="http://my_student" xmlns:room="http://my_room">
                        <student:Name>LiuYing</student:Name>
                        <Age>23</Age>
                    <romm:Name>2014</room:Name>
                    <Location>1-23-1</Location>
                </Schooler>      

# xml访问

## 读取
- xml读取两个主要技术,SAX,DOM
- SAX（Simple API for XML):
    - 基于事件驱动的API
    - 利用SAX解析文档设计到解析器和事件处理两部分
    - 特点:
        - 快
        - 流式读取
        
- - DOM
    - 是W3C规定的XML编程接口
    - 一个XML文件再缓存中以树形结构保存，读取
    - 用途
        - 定位浏览XML任何一个节点信息
        - 添加删除相应内容
        
    - minidom
        - minidom.parse(filename):加载读取的xml文件,filename也苦役是xml代码
        - doc.documentElement:获取xml文件对象,一个xml文件只有一个对于的文档对象
        - mode.getAttribute(attr_name):获取xml节点属性值
        - mode.getElementByTagName(tage_name]):得到一个节点对象集合
        - mode.childNodes:得到所有孩子节点
        - mode.childNodes[index].modeValue:获取单个节点值
        - mode.firstNode:得到一个节点.等价于mode.childNodes[0]
        - mode.attribute[tage_name]
        - 案例01
   
