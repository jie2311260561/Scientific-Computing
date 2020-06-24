#数据处理

from pyecharts.charts import Geo
import pandas as pd

df = pd.read_csv(r"D:\learn Java\pyday\Scientific-Computing\对全球未成年人生育率数据实现地理数据可视化\data\adol-fertility.csv",encoding='gb18030')
geo=Geo()
attr=list(df['country']) #生成国家名列表
value=list(df['ad_fert_rate']) #生成生育率值列表
dictionary = dict(zip(attr,value))
geo_countries_coords={df.iloc[i]['country']:[df.iloc[i]['longitude'],df.iloc[i]['latitude']] for i in range(len(df))}
# cccc  = ([df.iloc[i]['longitude'],df.iloc[i]['latitude']] for i in range(len(df)))
geo.add_schema("world",is_roam=True)

# for i in range(len(df)):
#     geo.add_coordinate(attr,df.iloc[i]['longitude'],df.iloc[i]['latitude'])

# ********* End *********#
#生成html文件
geo.render('map.html')
