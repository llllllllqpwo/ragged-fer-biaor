# ragged fer biaor

## To-do list 
### GUI
- [x] 学习PyQt5
    - [x] Qt Designer 失败
- [x] 初步设计GUI
- [ ] 连接控制器
- [ ] 完善
### 数据库
- [x] 学习Sqlite
    - [x] Sqlite expert personal
- [x] 初步建立数据库
- [ ] 连接控制器
### 功能
- 账号登录注册
    - [ ] 学生
    - [ ] 教师
    - [ ] 非法
- 控制器
    - [ ] 学生查自己
        - [ ] 选择考试（可多选）
        - [ ] 指定科目
        - [ ] 是否显示班级
        - [ ] 是否显示排名
        - [ ] 生成几次考试总成绩和班级排名折线图
        - [ ] 该学科各次考试折线图
        - [ ] 个人成长报告
        - [ ] 用日期查询（选
    - [ ] 教师
        - [x] 录入    
        - [ ] 导出
        - [ ] 班级平均分折线图，各科得分率柱状图
        - [ ] 平均成绩统计、标准差、历次考试成绩统计、学生名次变化统计等。
        - [ ] 不同教师权限（任课、教务处、教学秘书、课程负责人）（选）
        - [ ] 线性回归（选）

 - [ ] 打包exe（选）


---
二、 基本实验要求
搭建一个具有 GUI 界面的成绩管理系统，主要功能如下:
1. 教师/学生用户的注册以及登录
2. 教师用户可以在其对应的界面中：

    （1）对学生成绩进行增、删、改、查操作；

    （2）导出成绩为不同格式文件

    （3）生成可视化的成绩图表

    （4）实现数据统计分析
3. 学生用户可以在其对应的界面中查询自己的成绩和排名情况
4. 系统中的数据，如已注册的教师或学生账户以及已录入的成绩等需要使用数据库在
本地文件保存

三、必做部分
1. 系统必须具有 GUI 界面，要求用户的所有操作在 GUI 内完成，且用户与系统交互的
方式对用户友好。
2. 数据库的使用
要求系统必须使用数据库存储教师用户与学生用户的各项信息(工号/学号、密码等)以
及学生成绩信息，在程序运行过程中连接数据库对上述信息进行增删改查操作。
3. 教师/学生用户的登录以及注册

    (1)登录界面
登录界面需要用户输入工号/学号以及密码登录，由用户选择身份（教师或学生）
或通过工号/学号特征检验确认用户身份。

    (2) 学生注册界面
学生注册需要输入姓名、学号、班级、登录密码和班级注册码(自行规定)来进行注
册，这些信息需满足一定的规范(自行制定，如学号必须是 8 位的整数)，否则注册失败。8

    (3) 教师注册
教师注册需要输入姓名、教师工号、登录密码和教师注册码(自行规定)进行注
册，这些信息需满足一定的规范(自行制定， 如工号必须是 5 位的整数)，否则注册失
败。

    (4) 非法信息处理
登录/注册时若有密码错误或注册信息不符合规范等情况出现，使用弹出警告窗口
等方式进行提醒。
4. 学生用户界面
学生用户能够在该界面选择查询条件，并据此看到自己的成绩(不可更改自己的成
绩)。可选的查询条件应该包括:指定某次或某几次考试、指定科目、是否显示班级以及
年级排名等。同时学生能够选择生成学生各次考试的总成绩折线图和班级排名折线图，
或学生指定学科后给出该学科在各次考试中的成绩折线图。
5. 教师用户界面

    (1) 成绩录入部分
成绩录入部分应当有类似表格的组件，教师用户在该组件中进行的修改能够实时同
步到数据库文件当中。实现效果可参考下图。

    (2) 成绩导出部分
成绩导出应当部分可以让用户选择某次考试成绩单进行导出，且能选择文件导出格
式(xlsx、 csv 等)。

    (3) 成绩分析图表
成绩分析图图表应当提供一系列图表生成参数的选择，如生成多次考试班级平均分
折线图，各科目得分率柱状图等。9

    （ 4）成绩统计
成绩分析要求用户能对成绩进行统计并将统计数据显示在 GUI 中，统计方式可以
包括平均成绩统计、标准差、历次考试成绩统计、学生名次变化统计等。
    
 四、选做部分
1. 将程序打包为.exe 后缀的应用程序，确保其正常运行
2. 设置不同的教师权限，如任课老师可对自己负责学科成绩进行更改、教务处老师可
对全科成绩进行更改等。权限引入方式自由，如通过不同的教师注册码来进行区分。 权限的
分级亦可自由发挥，引入大学模式的教学秘书/课程负责人等。
3. 根据学生的成绩变化情况、单科排名、全科排名等信息生成一个文本类的成绩分析
报告。
4. 提供更多的成绩分析形式，比如对考试成绩进行线性回归并画出。
5. 对于学生用户，提供更多的成绩查询形式，比如指定学科和考试日期查询对应的成
绩。
选做内容不要求全部完成，系统功能也可以在完成必做的基础上自由发挥