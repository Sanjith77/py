import dash 
import dash_core__components as dcc
import dash_html_components as html


app=dash.DASH(__name__)


app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
                dcc.Graph(
                    id='My-Graph',
                    figure={
                        'Data':[
                            {'x':[1,2,3],'y':[4,1,2],'type' : 'bar', 'name':'bar chart'},
                            {'x':[1,2,3],'y':[2,4,5],'type' : 'line', 'name':'bar chart'},
                        ],
                        'layout' :{
                            'title': 'Graph title',
                            'xaxis': {'title':'x-axis'},
                            'yaxis': {'title':'y-axis'}
                           }
                        }
                )
    ]
)


if __name__=='__main__':
    app.run_server(debug=True)