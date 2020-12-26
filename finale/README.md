毕业项目：构建一个舆情分析平台
==========================================================================================================================
项目背景：某公司计划新上线一款苏打水饮料，为了了解用户对苏打水的接受程度，需要抓取“什么值得买”( https://www.smzdm.com/fenlei/qipaoshui/ ) 
网站中气泡水种类前 10 的产品的用户评论，通过对用户评论的正向、负向评价了解排名前 10 的气泡水产品的用户接受程度。

注意：
由于这个网站的产品是实时更新的，一些新的气泡水产品可能没有足够数量的评论，大家可以将气泡水替换为其他产品，比如：

手机产品 24 小时排行 https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/
电脑游戏最新排行 https://www.smzdm.com/fenlei/diannaoyouxi/
洗发护发产品 24 小时排行 https://www.smzdm.com/fenlei/xifahufa/h5c4s0f0t0p1/#feed-main/
具体需求：

正确使用 Scrapy 框架或 Selenium 获取评论，如果评论有多页，需实现自动翻页功能，将原始评论结果存入 MySQL 数据库，并使用定时任务每天定期更新。
对评论数据进行清洗（可借助 Pandas 库），并进行语义情感分析，将分析结果存入数据库。
使用 Django 集成在线图表对采集数、舆情进行展示，需包括该产品正、负评价比例，以及评价内容等。
数据展示支持按时间筛选和按关键词筛选功能（参考）
https://www.yqt365.com/newEdition/wb/event/analysis/w1yqtxwb62574190201152403817
评分标准：（实现相应功能，每项 +10 分，部分实现 +5 分）

正确使用 Scrapy 框架获取评论，如果评论有多页，需实现自动翻页功能。
评论内容能够正确存储到 MySQL 数据库中，不因表结构不合理出现数据截断情况。
数据清洗后，再次存储的数据不应出现缺失值。
Django 能够正确运行，并展示采集到的数据，数据不应该有乱码、缺失等问题。
在 Django 上采用图表方式展示数据分类情况。
舆情分析的结果存入到 MySQL 数据库中。
在 Django 上采用图表方式展示舆情分析的结果。
可以在 Web 界面根据关键字或关键词进行搜索，并能够在页面展示正确的搜索结果。
支持按照时间（录入时间或评论时间）进行搜索，并能够在页面展示正确的搜索结果。
符合 PEP8 代码规范，函数、模块之间的调用高内聚低耦合，具有良好的扩展性和可读性。


数据库设计：
==========================================================================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'FinaleDB', #DBName
        'USER': 'zcat',
        'PASSWORD': 'MySQL5.7',
        'HOST': '192.168.0.57',
        'PORT': '3306',
    }
}

class SKUs(models.Model):
    # id 自动创建
    sku = models.PositiveIntegerField() #sku id
    skuname = models.CharField(max_length=200) #sku name
    updatetime = models.DateTimeField() #update time
    skuurl = models.URLField()
    pricescript = models.CharField(max_length=50) #description of price
    skudescription = models.TextField()
    worthy = models.PositiveIntegerField()
    notworthy = models.PositiveIntegerField()
    stars = models.PositiveIntegerField()
    
class Comments(models.Model):
	# id 自动创建
	sku = models.PositiveIntegerField() #sku id 
	cid = models.PositiveIntegerField() #comment id
	qid = models.PositiveIntegerField() #quote id, which comment followed, if more than one commont to follow, use the minimal qid(earlyer)
	user = models.CharField(max_length=200) #user name
	cdescription = models.TextField()
    sentiments = models.FloatField()


爬虫设计：
==========================================================================================================================
SMZDM网站手机24小时排行
'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/'
scrapy crawl smzdm --nolog

分三层爬取
1. 排行榜
2. 详情页
3. 评论

实现要点：
1. 爬虫初始化时建立已有SKU列表，根据最后更新时间（由详情页获取）判断是否需要重新读取
2. 根据最下方是否存在评论页跳转按钮判断是否存在多页评论，分别处理
3. 原创评论和引用评论ID和内容位置不同，分别处理
4. 根据返回item的类型判断需要更新SKU信息还是评论信息，分别处理
5. 引用评论只记录最后一个引用ID，原创评论引用ID为0，可以重建评论树
6. INSERT INTO ... ON DUPLICATE KEY UPDATE ... 
   INSERT INTO ... SELECT ... FROM ... WHERE NOT EXISTS (SELECT ... FROM ... WHERE ...)

问题：
1. 无法通过yield scrapy.Request(meta={'key': item})方式传递数据，获取值不对，原因待查
2. 由于SKU信息和评论信息分开处理和入库，需要执行两遍才能获取全部信息，暂时可通过定时任务方式解决，后续考虑通过pipeline中间件解决


数据清洗与情感分析：
==========================================================================================================================
1. 数据清洗与预处理
2. 基于SnowNLP的情感分析与优化

实现要点：
1. 统计各字段无效值
2. 修正sku名称，去掉营销前缀
3. sku描述去掉控制符
4. 删除空白的评论
5. comments['sentiments'] = comments['cdescription'].apply(lambda x: SnowNLP(x).sentiments)

问题：
1. 用Pandas处理数据时均为全量，可以考虑只处理增量数据
2. 写回数据库时缺失主键定义


网站设计：
==========================================================================================================================
1. 使用django生成详情页
2. 导入bootstrap优化页面布局
3. 根据（1）开始日期、（2）日期区间、（3）关键字对当前商品评论进行搜索
3. 使用gunicorn部署生产环境
4. 使用celery执行定时任务

实现要点：
1. django的MTV模型
2. bootstrap模板的导入
3. 前端与后端数据的传递（GET方式）
4. django数据模型查询

问题：
1. 页面待美化
2. 查询条件未做过滤，有安全隐患