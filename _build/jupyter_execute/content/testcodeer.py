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

# <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg==" crossorigin="anonymous" />
# <script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"></script>
# 
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
# <button id="activateButton" style="width: 120px; height: 45px; font-size: 1.5em;">
#      Activate
# </button>
# <script>
#    var bootstrapThebe = function() {
#        thebe.bootstrap();
#    }
#    document.querySelector("#activateButton").addEventListener('click', bootstrapThebe)
# </script>
# 
# 
# 
#    <pre data-executable="true" data-language="python">
#    %matplotlib widget
#    import ipywidgets as widgets
#    import matplotlib.pyplot as plt
#    import numpy as np
# 
#    x = np.linspace(0,10)
# 
#    def sine_func(x, w, amp):
#        return amp*np.sin(w*x)
# 
#    @widgets.interact(w=(0, 4, 0.25), amp=(0, 4, .1))
#    def update(w = 1, amp = 1):
#        plt.clf()
#        plt.ylim(-4, 4)
#        plt.plot(x, sine_func(x, w, amp))
#    </pre>
# 

# 
