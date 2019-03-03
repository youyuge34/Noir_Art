## NoirArt (WIP)
### 诺瓦艺术- 墙内的设计作品分享平台(开发中)      

`git tag -n` :查看不同version版本说明      
`git check v0.1` :切换到指定版本号，每个版本可运行

------

### **v0.1**
**框架搭建，`base`基模板编写，主页编写: 蓝图分包，`bootstrap`主题替换**

-------

### **v0.2**
**注册登陆逻辑，添加用户注册登陆功能步骤：**

0. 集成flask-login，init，写好`load_user`函数后才能在所有上下文里调用`current_user`
1. html注册、登陆原型写好 
2. 用户模型类（数据库建表） 
3. 登陆注册表单`FlaskForm`类写好 
4. auth蓝图中写好登陆注册的view函数: 使用`current_user`的方法判断登陆与否
5. 修改对应模板html类     

------

### **v0.3**
**RBAC 基于权限的角色控制**

0. 创建角色和权限的模型数据库: `role` 角色表和 `permission` 权限表建立多对多关系，`User`和`role` 一对多关系. 用户创建时自动`set_role()`
1. 权限验证`decorator`编写，方便以后函数的权限检验

-----

### **v0.4**
**`Dropzone` 上传模块**

0. `extensions.py`中注册第三方模块
1. 设置静态参数到`settings.py`
2. Dropzone支持`wtf-CSRFprotect`扩展，配置一下
3. 添加dropzone的`js/css`资源文件，编写`upload.html`
4. 处理保存上传图片
    - 添加photo数据库模型，建立和User的一对多关系
    - 编写`upload.html`
    - 视图函数`main.upload`实现图片保存和图片信息写入数据库


**基页面添加动态视频背景，首页组建重写透明度**

0. html5的`video`标签只支持avc编码的mp4
1. 父元素使用`opacity`后子元素也就只能透明，所以要用`rgba`设置
2. `z-index`可指定布局所在层级

------

### **v0.5**
**`Dynamic BG` 动态/静态 背景开关**

0. 先写`change_theme`视图函数，接受`video`/`photo`参数，存入`cookies`中， 返回之前的页面
1. `base.html`页面中先从`cookies`中获取参数（默认`video`），加载对应标签元素
2. `base.html`页面的导航栏item中写背景开关，用`checkbox`,默认`checked`,`onclick()`中写JS函数回调，点击后JS会传`checkbox`的状态参数到 0 step中的视图函数
3. `base.html`页面最后写`jQuery`函数，根据`cookies`中参数设定改变对应的`checkbox`状态,必须要声明在`script.js`文件后面，不然函数还没加载到

------

### **v0.6**
**`User`页面，`Photo`详情页面编写完毕**

太复杂不想写了！

-----

### **v0.7**
**使用AJAX技术，实现鼠标放到头像上之后就弹小窗口**

0. 编写`ajax`蓝图中的视图函数，接收`user_id`后返回小窗口页面`html`
1. 在头像的父布局`_comment.html`中添加虚拟`class`和`data-url`
2. 在`js`中编写弹出/隐藏函数，目标url就是`data-url`=0.中的视图函数，返回弹窗内容后，显示出来
3. 在`js`中绑定虚拟`class`和弹出/隐藏函数

> AJAX流程总结：点击按钮后，执行并传参给绑定的JS函数，js函数内通过`url get`的方式调用视图函数，得到返回结果。
得到结果后，将结果插入/显示到`html`中,达到动态的效果。

**使用js编写toast弹窗提示函数**

0. `base.html`中添加一个`id`容器
1. css中编写toast样式，s中编写toast函数，
2. js中使用时只需调用`toast(body)`就好啦~

### **v0.8**     
**添加图片收藏功能**

### **v0.9**
**各个页面添加关注功能**

### **v1.0**
**动态轮询推送，消息中心功能~**

### **v1.1**
**登陆后首页显示动态**