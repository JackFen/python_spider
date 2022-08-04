# python_spider
 记录自己学习python爬虫的过程
# douban爬取top250榜单项目
## 摘要
本爬虫项目以doubanTop250榜单为目标，将数据爬取到数据库中，采用一些第三方库对数据进行分类与统计，并采用flask框架实现了数据的可视化
## 项目结构
<img src="https://github.com/JackFen/python_spider/blob/main/img_of_readme/1.png" width = 100% height = 100% />

## 所用到的库
1. sqlite3  //python内置的轻量级数据库
2. jieba    //一个将中文段落分为许多词语的库
3. matplotlib //绘制图片的库
4. wordcloud  //生成词云的库
5. PIL        //图片处理的库
6. numpy      //生成词云时处理矩阵运算的库
## 模块
1. 功能选择
: 基于flask框架，整个项目的请求转发采取注释型编程，逻辑清晰，代码简洁，和SSM架构相似
2. 数据展示
: 基于flask框架，将爬取到的数据从数据库发送到前端页面，然后进行展示，点击对应的影片名称便可以跳转到该影片的详情页面
3. 数据分析
: 采用EChart技术，将数据进行统计分析后显示到前端html页面
4. 数据统计
: 采用了wordcloud技术，将对电影的一句话评价进行词频统计，并生成词频树显示到页面上，
