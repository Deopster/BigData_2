fig = go.Figure(px.bar(x=data.keys(), y=data.values(), color = data.keys(), text= data.values(), height=700, width=1700))
fig.update_traces(textfont_size=14, textangle=0, textposition="outside", marker=dict(line=dict(color="black", width=2)))
fig.update_layout(
    title = "Диаграмма СЫРА", title_font_size = 20,title_x=0.5,
    xaxis_title = "Страны экспортёры сыра", xaxis_title_font_size = 16, xaxis_tickfont_size = 14, yaxis_title = 'СКОЛЬКО СЫРА В КИЛО?', yaxis_title_font_size = 16, yaxis_tickfont_size = 14,
    margin=dict(l=0, r=0, t=30, b=0),autosize=True)
fig.update_xaxes(tickangle= 315)
fig. show()