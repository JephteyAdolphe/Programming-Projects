import bokeh
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, HoverTool, tools, Plot, Patches, Slider, CustomJS
from bokeh.plotting import figure, output_file
from bokeh.sampledata.us_counties import data as counties
from bokeh.io import show
from data import IncomeParser

csv_list = ["12incynj.csv", "13incynj.csv", "14incynj.csv", "15incynj.csv", "16incynj.csv", "17incynj.csv",]

my_objects = []
parsedDataListOfDicts = []

for files in csv_list:
    my_objects.append(IncomeParser(files))

for objects in my_objects:
    parsedDataListOfDicts.append(objects.getCountyData())

nj_counties = {
    code: county for code, county in counties.items() if county["state"] == "nj"
}

nj_county_xs = [county["lons"] for county in nj_counties.values()]
nj_county_ys = [county["lats"] for county in nj_counties.values()]

nj_county_names = [county['name'] for county in nj_counties.values()]

income_master_list = []

for dicts in parsedDataListOfDicts:
    holder = []
    for i in dicts:
        holder.append(dicts[i])
    income_master_list.append(holder)


source = ColumnDataSource(data=dict(x=nj_county_xs, y=nj_county_ys, name=nj_county_names, income=income_master_list[0]))

p = figure(title="New Jersey Median Income", tools="")
p.patches('x', 'y', source=source, fill_alpha=0.5, fill_color='#8E0D3F', line_color="white", line_width=0.5)

year_slider = Slider(start=2012, end=2017, value=2012, step=1, title="Year")

callback = CustomJS(args=dict(source=source, year=year_slider, master=income_master_list), code="""
    var data = source.data;
    var yr = year.value;
    const x = data['x'];
    const y = data['y'];
    const names = data['name'];
    data['income'] = master[yr - 2012];
    
    source.change.emit()
""")

year_slider.js_on_change('value', callback)

layout = row(
    p,
    column(year_slider)
)

hover = HoverTool()
hover.point_policy = "follow_mouse"
hover.tooltips = """
<div>
    <h3>@name County</h3>
    <div><strong>Median Income: </strong>@income</div>
    <div><strong>(Long, Lat): </strong>($x, $y)</div>
    <div></div>
</div>
"""

p.add_tools(hover)

output_file("nj.html")

show(layout)
