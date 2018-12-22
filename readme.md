## NoirArt (WIP)
### 诺瓦艺术- 墙内的设计作品分享平台(开发中)      

`git tag -n` :查看不同version版本说明      

- v0.1 框架搭建，base基模板编写，主页编写: 蓝图分包，bootstrap主题替换
- v0.2 注册登陆逻辑，添加用户注册登陆功能步骤：    

0. 集成flask-login，init，写好load_user函数后才能在所有上下文里调用`current_user`
1. html注册、登陆原型写好 
2. 用户模型类（数据库建表） 
3. 登陆注册表单`FlaskForm`类写好 
4. auth蓝图中写好登陆注册的view函数: 使用`current_user`的方法判断登陆与否
5. 修改对应模板html类     
