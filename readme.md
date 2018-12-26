## NoirArt (WIP)
### 诺瓦艺术- 墙内的设计作品分享平台(开发中)      

`git tag -n` :查看不同version版本说明      
`git check v0.1` :切换到指定版本号，每个版本可运行

#### **v0.1**
**框架搭建，`base`基模板编写，主页编写: 蓝图分包，`bootstrap`主题替换**

-------

#### **v0.2**
**注册登陆逻辑，添加用户注册登陆功能步骤：**

0. 集成flask-login，init，写好`load_user`函数后才能在所有上下文里调用`current_user`
1. html注册、登陆原型写好 
2. 用户模型类（数据库建表） 
3. 登陆注册表单`FlaskForm`类写好 
4. auth蓝图中写好登陆注册的view函数: 使用`current_user`的方法判断登陆与否
5. 修改对应模板html类     

------

#### **v0.3**
**RBAC 基于权限的角色控制**

0. 创建角色和权限的模型数据库: `role` 角色表和 `permission` 权限表建立多对多关系，`User`和`role` 一对多关系. 用户创建时自动`set_role()`
1. 权限验证`decorator`编写，方便以后函数的权限检验

-----

#### **v0.4**
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

