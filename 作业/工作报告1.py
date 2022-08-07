import pyecharts

from pyecharts.charts import Line

from pyecharts import options as opts

# 示例数据

cate = [i[0] for i in word_counts_top30]

data1 = [i[1] for i in word_counts_top30]

line = (Line()

.add_xaxis(cate)

.add_yaxis('词频', data1,

markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])).set_global_opts(title_opts=opts.TitleOpts(title="词频统计Top30", subtitle=""),

xaxis_opts=opts.AxisOpts(name_rotate=60,axislabel_opts={"rotate":45}))

)

line.render_notebook()