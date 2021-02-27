import tkinter as tk
import tkinter.font as tkFont
import psutil
import platform
from win32api import GetSystemMetrics
import time
import matplotlib.pyplot as plt
import numpy as np

def toggleFullScreen(self, status):
    self.fullScreenState = not self.fullScreenState
    self.attributes("-fullscreen", self.fullScreenState)


def quitFullScreen(self, status):
    self.fullScreenState = False
    self.attributes("-fullscreen", self.fullScreenState)


if __name__ == '__main__':

    # MODULO DE DATOS DEL PC EXTRAIDO DE:
    # https: // github.com / rahulph / chk - pc - status / blob / master / cpu.py

    # inicilizo el uname para datos del pc
    uname = platform.uname()

    # VENTANA PRINCIPAL
    root = tk.Tk()
    root.minsize(GetSystemMetrics(0), GetSystemMetrics(1))
    root.maxsize(GetSystemMetrics(0), GetSystemMetrics(1))
    root.wm_attributes("-topmost", False)  # siempre al top
    root.wm_attributes("-transparentcolor", "#abcdef")
    root.attributes('-fullscreen', True)
    root.config(bg="#abcdef")  # color transparent ->>>> #abcdef

    # SUBVENTANA
    subroot = tk.Frame(root)
    subroot.config(bg="#abcdef", width=200, height=500)
    subroot.pack(side=tk.RIGHT)

    # FUENTE CUSTOM
    print(list(tkFont.families()))
    fontExample = tkFont.Font(family="Oswald", size=12, weight="normal", slant="roman")

    # LABELS FIJOS
    # SO
    so_label = tk.Label(subroot, text=f"System: {uname.system}", anchor="w")
    so_label.config(bg="#abcdef", fg="#fff", font=fontExample)
    so_label.grid(row=0, column=0, sticky="E")
    # VERSION SO
    version_label = tk.Label(subroot, text=f"Release: {uname.release}", anchor="w")
    version_label.config(bg="#abcdef", fg="#fff", font=fontExample)
    version_label.grid(row=1, column=0, sticky="E")
    # machine
    machine_label = tk.Label(subroot, text=f"Machine: {uname.machine}", anchor="w")
    machine_label.config(bg="#abcdef", fg="#fff", font=fontExample)
    machine_label.grid(row=2, column=0, sticky="E")
    # processor
    processor_label = tk.Label(subroot, text=f"Processor: {uname.processor}", anchor="w")
    processor_label.config(bg="#abcdef", fg="#fff", highlightcolor="white", font=fontExample)
    processor_label.grid(row=3, column=0, sticky="E")

    # estado del sistema
    # cores
    cores_label = tk.Label(subroot, text=f"Physical Cores: {psutil.cpu_count(logical=False)}", anchor="w")
    cores_label.config(bg="#abcdef", fg="#fff", highlightcolor="white", font=fontExample)
    cores_label.grid(row=4, column=0, sticky="E")

    # LABELES DINAMICOS
    cpuCurrentUsageArray = []


    # funcion para update de texto de cada label, para evitar crear uno cada vez que haya una actualizacion del valor
    # cambio directamente el contenido de texto de cada label guardado en cpuCurrentUsageArray
    def updateCpuUsage(label):
        label.config(text=f"Core {x + 1}:   {percentage}%")

    # GRAPH CPU USAGE (MATPLOTLIB)















    #EN TESTEO ESTO (IDEA: METER GRAPHS DINAMICOS PARA VER LA CPU)














    #for para crear elementos en sus arrays para post manipulacion por medio dde su indice
    height = []
    bars = []
    for x, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        height.append(percentage)
        bars.append(x)
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    def animate():
        ax1.clear()
        for x, percentage in enumerate(psutil.cpu_percent(percpu=True)):
            height[x] = percentage
        print(height)
        y_pos = np.arange(len(bars))
        ax1.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))
        # Custom Axis title
        plt.show()
        return
        # FIN GRAPHS TEST


    for x, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        currentCpuUsage_label = tk.Label(subroot, text=f"Core {x + 1}: {percentage}%", anchor="w")
        currentCpuUsage_label.config(bg="#abcdef", fg="#fff", highlightcolor="white", font=fontExample)
        currentCpuUsage_label.grid(row=x + 5, column=0, sticky="E")
        cpuCurrentUsageArray.append(currentCpuUsage_label)

    # UPDATER
    while 1:
        for x, percentage in enumerate(psutil.cpu_percent(percpu=True)):
            updateCpuUsage(cpuCurrentUsageArray[x])
        print(len(cpuCurrentUsageArray))
        animate()
        root.update()
        time.sleep(1)
