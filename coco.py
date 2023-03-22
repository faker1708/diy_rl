# 首先导入Cocos包

import cocos

# 对图层进行子类化 并在此处定义编程的逻辑


class HelloWorld(cocos.layer.Layer):


    def __init__(self):

        # 调用super构造函数


        super(HelloWorld, self).__init__()

        # 要显示文本，我们将创建一个Label。关键字参数用于设置标签的字体，位置和对齐方式

        label = cocos.text.Label(

            'Hello, world',

            font_name='Times New Roman',

            font_size=32,

            anchor_x='center', anchor_y='center'

        )

        # 标签位置将是屏幕的中心

        label.position = 320, 240

        # 由于Label是CocosNode的子类，因此可以将其添加为子级。所有CocosNode对象都知道如何呈现自身，执行操作和转换。要将其添加为图层的子项，请使用CocosNode.add方法

        self.add(label)

        # 定义HelloWorld类之后，我们需要初始化并创建一个窗口。为此，我们初始化Director

        cocos.director.director.init()

        # 然后我们创建一个HelloWorld实例

        hello_layer = HelloWorld()

        # 然后我们创建一个包含子层的场景HelloWorld

        main_scene = cocos.scene.Scene(hello_layer)

        # 最后我们运行场景

        cocos.director.director.run(main_scene)
a = HelloWorld()