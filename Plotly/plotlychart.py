import plotly.express as px
import os
import requests

config = {'displayModeBar': False}

class Plotly():
    __css_base = ".modebar {display: none;} \n.modebar-container {display: none;} "

    def __export(self, chart, filename, css=None):
        html_filename = f"{filename.split('.')[0]}.html"
        html_exist = os.path.exists(html_filename)
        chart.write_html(html_filename)
        selector = None
        html_map = None
        if css is None:
            css = self.__css_base
        else:
            css = css + self.__css_base
        with open(html_filename) as f:
            html_map = f.read()
            if html_map.find(" cartesianlayer") != -1:
                selector = ".cartesianlayer"
            result = html_map.replace(
                "</head>", f'<style id="naas_css">{css}</style></head>'
            )
        with open(html_filename, "w") as f:
            f.write(result)
            f.close()
        if filename.endswith(".png") or filename.endswith(".jpeg"):
            html_text = result
            extension = filename.split(".")[1]
            json = {
                "output": "screenshot",
                "html": html_text,
                "emulateScreenMedia": True,
                "ignoreHttpsErrors": True,
                "scrollPage": False,
                "screenshot": {"type": extension},
            }
            if selector:
                json["screenshot"]["selector"] = selector
            req = requests.post(
                url=f"{os.environ.get('SCREENSHOT_API', 'http://naas-screenshot:9000')}/api/render", # Sensitive
                json=json,
            )
            req.raise_for_status()
            open(filename, "wb").write(req.content)
            if not html_exist:
                os.remove(html_filename)
        elif not filename.endswith(".html"):
            print("Not supported for now")
            os.remove(html_filename)
            return
        print(f"Saved as {filename}")

    def export(self, chart, filenames, css=None):
        """ create html export and add css to it"""
        if isinstance(filenames, list):
            for filename in filenames:
                self.__export(chart, filename, css)
        else:
            self.__export(chart, filenames, css)
            
    def __update_layout(self,
                        fig,
                        title=None,
                        plot_bgcolor=None,
                        width=None,
                        height=None,
                        showlegend=None,
                        xaxis_title=None,
                        yaxis_title=None):
        fig.update_layout(title=title,
                          plot_bgcolor=plot_bgcolor,
                          width=width,
                          height=height,
                          showlegend=showlegend,
                          xaxis_title=xaxis_title,
                          yaxis_title=yaxis_title)
        return fig

    def linechart(self,
                  df,
                  x,
                  y,
                  title=None,
                  plot_bgcolor="#ffffff",
                  width=None,
                  height=600,
                  showlegend=False,
                  xaxis_title=None,
                  yaxis_title=None):
        fig = px.line(df, x, y)
        fig = self.__update_layout(fig, title, plot_bgcolor, width, height, showlegend, xaxis_title, yaxis_title)
        fig.show(config=config)
        return fig
        