#!/usr/bin/env python
# coding: utf-8

# # Testing the code for run 

# <script type="text/x-thebe-config">
#   {
#     requestKernel: true,
#     binderOptions: {
#       repo: "matplotlib/ipympl",
#       ref: "0.6.1",
#       repoProvider: "github",
#     },
#   }
# </script>
# <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>
# 

# <script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"></script>
# 
# <script type="text/x-thebe-config">
#   {
#     requestKernel: true,
#     binderOptions: {
#       repo: "plotly/plotly.py",
#       ref: "doc-prod",
#       binderUrl: "https://mybinder.org",
#       repoProvider: "github",
#     },
#   }
# </script>
# <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>
# 
# <button id="activateButton" style="width: 120px; height: 40px; font-size: 1.5em;">
#   Activate
# </button>
# <script>
# var bootstrapThebe = function() {
#     thebe.bootstrap();
# }
# document.querySelector("#activateButton").addEventListener('click', bootstrapThebe)
# </script>
# 
# <pre data-executable="true" data-language="python">
# import plotly.express as px
# df = px.data.tips()
# fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug",
#                    hover_data=df.columns)
# fig.show()
# </pre>

# 
