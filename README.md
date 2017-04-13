# 个人成长计划

我变老了 变秃了 也变强了

##git内容
1. 工作上的成果积累和数据积累
2. 读书笔记
3. py学习代码
4. 数据分析课题进展和结果
5. 统计学学习笔记


##每天要做的事情
- 完成3个TODOlist
- 进行8个番茄钟
- 读一个小时的书



MD语法

# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题


普通列表
- 文本1
- 文本2
- 文本3

有序列表

1. 文本1
2. 文本2
3. 文本3

链接
[链接名](http:// 链接地址)


图片
![图片注释、可不加](http:// 图片链接)


引用
>引用文字

*斜体*
**粗体**


`单行代码

```多行代码


表格
| Tables| line1| line2  |
| ----- |:----:| ------:|
| 左对齐| 居中 | 右对齐 |
| 222   |      |        |
| 111   |      |        |


标记列表：
*后续跟踪




select d.fday,d.server,count(distinct d.regid),
sum(case when d.lcd = 0 then 1 else 0 end) as lc1,
sum(case when d.lcd = 1 then 1 else 0 end) as lc2,
sum(case when d.lcd = 2 then 1 else 0 end) as lc3,
sum(case when d.lcd = 3 then 1 else 0 end) as lc4,
sum(case when d.lcd = 4 then 1 else 0 end) as lc5,
sum(case when d.lcd = 5 then 1 else 0 end) as lc6,
sum(case when d.lcd = 6 then 1 else 0 end) as lc7
from
(select c.server,c.regid,c.fday,datediff(c.rday,c.fday) as lcd from
    (select e.server,e.regid,e.fday,a.rday from
        (select distinct user_id as regid,data_day as fday,server 
            from wl_login_his 
            where data_day>='2017-03-14'
            and app_id='400_2013030688'
            and channel not in ('11000020','110','22000101','22000102','22000104')
            and server='500003'
            and is_new=1
            and is_new_server=1) e
        left join 
        (select distinct user_id as uid,data_day as rday
            from wl_login_his 
            where data_day>='2017-03-14'
            and app_id='400_2013030688'
            and channel not in ('11000020','110','22000101','22000102','22000104')
            and server='500003'
            ) a
        on a.uid = e.regid) c) d
group by d.fday,d.server


select price,czmount,count(numid),
sum(case when fd = '>=0<500' then 1 else 0 end) as fd1,
sum(case when fd = '>=500<1000' then 1 else 0 end) as fd2,
sum(case when fd = '>=1000<5000' then 1 else 0 end) as fd3,
sum(case when fd = '>=5000<10000' then 1 else 0 end) as fd4,
sum(case when fd = '>=10000<20000' then 1 else 0 end) as fd5,
sum(case when fd = '>=20000<50000' then 1 else 0 end) as fd6,
sum(case when fd = '>=50000<100000' then 1 else 0 end) as fd7,
sum(case when fd = '>=100000<200000' then 1 else 0 end) as fd8,
sum(case when fd = '>=200000<500000' then 1 else 0 end) as fd9,
sum(case when fd = '>=500000<1000000' then 1 else 0 end) as fd10,
sum(case when fd = '>=1000000<5000000' then 1 else 0 end) as fd11
from `hangzhoumjsr2`
WHERE price != 0
group by price,czmount;


>=0<500
>=500<1000
>=1000<5000





>=5000000<10000000
>=10000000<100000000
>=100000000



SELECT fd,price,czmount,COUNT(numid) FROM `hangzhoumjsr2`
	WHERE price != 0
GROUP BY fd,price,czmount;

