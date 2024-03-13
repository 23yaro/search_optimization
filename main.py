import time
import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Notebook
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from Gradient import make_data_lab_1, funct_consider


def main():
    window = Tk()

    window.iconbitmap(r'image/image.ico')

    width = 1450
    height = 800

    window.geometry("%dx%d" % (width, height))

    window.title("Optimization")

    fig = plt.figure(figsize=(10, 10))
    fig.add_subplot(projection='3d')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, )

    tab_control = Notebook(window)

    def draw_lab_1():
        fig.clf()

        x, y, z = make_data_lab_1()

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=4, cstride=4, alpha=0.5, cmap="jet")
        canvas.draw()

        res_x = txt_1_tab_1.get()
        res_y = txt_2_tab_1.get()
        res_step = txt_3_tab_1.get()
        res_iterations = txt_4_tab_1.get()

        x_cs, y_cs, z_cs = funct_consider(float(res_x), float(res_y), float(res_step), int(res_iterations))

        for i in range(len(x_cs)):
            if i < (len(x_cs) - 1):
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s")
            else:
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")

            canvas.draw()
            txt_tab_1.insert(INSERT, f"{i}) f({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {z_cs[i]}\n")

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            window.update()
            delay = txt_5_tab_1.get()
            time.sleep(float(delay))

    def delete_lab_1():
        txt_tab_1.delete(1.0, END)

    tab_1 = Frame(tab_control)
    tab_control.add(tab_1, text="LR1")

    main_f_tab_1 = LabelFrame(tab_1, text="Parameters")
    left_f_tab_1 = Frame(main_f_tab_1)
    right_f_tab_1 = Frame(main_f_tab_1)
    txt_f_tab_1 = LabelFrame(tab_1, text="Выполнение и результаты")

    lbl_1_tab_1 = Label(left_f_tab_1, text="X")
    lbl_2_tab_1 = Label(left_f_tab_1, text="Y")
    lbl_3_tab_1 = Label(left_f_tab_1, text="Initial step")
    lbl_4_tab_1 = Label(left_f_tab_1, text="Number of iterations")
    lbl_5_tab_1 = Label(tab_1, text="Function x^2 + y^2")
    lbl_6_tab_1 = Label(left_f_tab_1, text="Delay")

    txt_1_tab_1 = Entry(right_f_tab_1)
    txt_1_tab_1.insert(0, "-1")

    txt_2_tab_1 = Entry(right_f_tab_1)
    txt_2_tab_1.insert(0, "-1")

    txt_3_tab_1 = Entry(right_f_tab_1)
    txt_3_tab_1.insert(0, "0.1")

    txt_4_tab_1 = Entry(right_f_tab_1)
    txt_4_tab_1.insert(0, "100")

    txt_5_tab_1 = Entry(right_f_tab_1)
    txt_5_tab_1.insert(0, "0.1")

    txt_tab_1 = scrolledtext.ScrolledText(txt_f_tab_1)
    btn_tab_1 = Button(tab_1, text="Start", foreground="black", command=draw_lab_1)
    txt_f_tab_1.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    lbl_5_tab_1.pack()
    main_f_tab_1.pack()
    left_f_tab_1.pack(side=LEFT)
    right_f_tab_1.pack(side=RIGHT)

    lbl_1_tab_1.pack()
    lbl_2_tab_1.pack()
    lbl_3_tab_1.pack()
    lbl_4_tab_1.pack()
    lbl_6_tab_1.pack()

    txt_1_tab_1.pack()
    txt_2_tab_1.pack()
    txt_3_tab_1.pack()
    txt_4_tab_1.pack()
    txt_5_tab_1.pack()

    txt_tab_1.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_1.pack()

    tab_control.pack()
    window.mainloop()


if __name__ == '__main__':
    main()
