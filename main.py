import time
import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Notebook, Combobox
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from Gradient import make_data_lab_1, funct_consider
from Rosenbrock_function import make_data_lab_3, rosenbrock_2
from SLSQP import make_data_lab_2, kp
from genetic_algorithm_l3 import GeneticAlgorithmL3


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
            txt_tab_1.insert(INSERT, f"f({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {z_cs[i]}\n")

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
    txt_f_tab_1 = LabelFrame(tab_1, text="Result")

    lbl_1_tab_1 = Label(left_f_tab_1, text="X")
    lbl_2_tab_1 = Label(left_f_tab_1, text="Y")
    lbl_3_tab_1 = Label(left_f_tab_1, text="Initial step")
    lbl_4_tab_1 = Label(left_f_tab_1, text="Number of iterations")
    lbl_5_tab_1 = Label(tab_1, text="Function x^2 + y^2")
    lbl_6_tab_1 = Label(left_f_tab_1, text="Delay")

    # initial value

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
    btn_del_tab_1 = Button(tab_1, text="Clear", command=delete_lab_1)
    btn_tab_1 = Button(tab_1, text="Start", foreground="black", command=draw_lab_1)

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

    btn_tab_1.pack()
    txt_tab_1.pack()
    txt_f_tab_1.pack()
    btn_del_tab_1.pack()

    def draw_lab_2():
        fig.clf()

        x, y, z = make_data_lab_2()

        res_x = txt_1_tab_2.get()
        res_y = txt_2_tab_2.get()

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=4, cstride=4, alpha=0.5, cmap="jet")
        canvas.draw()

        x_cs = []
        y_cs = []
        z_cs = []

        for i, point in kp(res_x, res_y):
            x_cs.append(point[0])
            y_cs.append(point[1])
            z_cs.append(point[2])

        for i in range(len(x_cs)):
            if i < (len(x_cs) - 1):
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s")
            else:
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")

            txt_tab_2.insert(INSERT, f"{i}) ({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {round(z_cs[i], 4)}\n")
            canvas.draw()
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            window.update()
            delay = txt_3_tab_2.get()
            time.sleep(float(delay))

    def delete_lab_2():
        txt_tab_2.delete(1.0, END)

    tab_2 = Frame(tab_control)
    tab_control.add(tab_2, text="LR2")

    main_f_tab_2 = LabelFrame(tab_2, text="Parameters")
    left_f_tab_2 = Frame(main_f_tab_2)
    right_f_tab_2 = Frame(main_f_tab_2)
    txt_f_tab_2 = LabelFrame(tab_2, text="Results")

    lbl_1_tab_2 = Label(tab_2, text="Function :\n2 * x₁² + 3 * x₂² + 4 * x₁ * x₂ - 6 * x₁ - 3 * x₂")
    lbl_2_tab_2 = Label(left_f_tab_2, text="X")
    lbl_3_tab_2 = Label(left_f_tab_2, text="Y")
    lbl_4_tab_2 = Label(left_f_tab_2, text="Delay")

    # initial value

    txt_1_tab_2 = Entry(right_f_tab_2)
    txt_1_tab_2.insert(0, "10")

    txt_2_tab_2 = Entry(right_f_tab_2)
    txt_2_tab_2.insert(0, "10")

    txt_3_tab_2 = Entry(right_f_tab_2)
    txt_3_tab_2.insert(0, "0.1")

    txt_tab_2 = scrolledtext.ScrolledText(txt_f_tab_2)
    btn_del_tab_2 = Button(tab_2, text="Clear", command=delete_lab_2)
    btn_tab_2 = Button(tab_2, text="Start", command=draw_lab_2)

    lbl_1_tab_2.pack()
    main_f_tab_2.pack()
    left_f_tab_2.pack(side=LEFT)
    right_f_tab_2.pack(side=RIGHT)

    lbl_2_tab_2.pack()
    lbl_3_tab_2.pack()
    lbl_4_tab_2.pack()

    txt_1_tab_2.pack()
    txt_2_tab_2.pack()
    txt_3_tab_2.pack()

    txt_tab_2.pack()

    btn_tab_2.pack()
    txt_f_tab_2.pack()
    btn_del_tab_2.pack()

    def draw_lab_3():
        fig.clf()

        x, y, z = make_data_lab_3()

        pop_number = int(txt_1_tab_3.get())
        iter_number = int(txt_2_tab_3.get())
        survive = float(txt_3_tab_3.get())
        mutation = float(txt_4_tab_3.get())
        delay = txt_5_tab_3.get()

        if combo_tab_3.get() == "Min":
            min_max = True
        else:
            min_max = False

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=4, cstride=4, alpha=0.5, cmap="jet")
        canvas.draw()

        genetic = GeneticAlgorithmL3(rosenbrock_2, iter_number, min_max, mutation, survive, pop_number)
        genetic.generate_start_population(5, 5)

        for j in range(pop_number):
            ax.scatter(genetic.population[j][0], genetic.population[j][1], genetic.population[j][2], c="black", s=1,
                       marker="s")
        if min_max:
            gen_stat = list(genetic.statistic()[1])
        else:
            gen_stat = list(genetic.statistic()[0])

        ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")
        canvas.draw()
        window.update()

        # Эти 4 строки ниже это считай удалить точку/точки
        fig.clf()
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=4, cstride=4, alpha=0.5, cmap="jet")
        canvas.draw()

        for i in range(50):
            for j in range(pop_number):
                ax.scatter(genetic.population[j][0], genetic.population[j][1], genetic.population[j][2], c="black", s=1,
                           marker="s")

            genetic.select()
            genetic.mutation(i)

            if min_max:
                gen_stat = list(genetic.statistic()[1])
            else:
                gen_stat = list(genetic.statistic()[0])

            ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")

            txt_tab_3.insert(INSERT,
                             f"{i}) ({round(gen_stat[1][0], 4)}) ({round(gen_stat[1][1], 4)}) = "
                             f" ({round(gen_stat[1][2], 4)})\n")

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection='3d')
            ax.plot_surface(x, y, z, rstride=4, cstride=4, alpha=0.5, cmap="jet")
            canvas.draw()

        for j in range(pop_number):
            ax.scatter(genetic.population[j][0], genetic.population[j][1], genetic.population[j][2], c="black", s=1,
                       marker="s")
        if min_max:
            gen_stat = list(genetic.statistic()[1])
        else:
            gen_stat = list(genetic.statistic()[0])

        ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")

        canvas.draw()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        window.update()

    def delete_lab_3():
        txt_tab_3.delete(1.0, END)

    tab_3 = Frame(tab_control)
    tab_control.add(tab_3, text="LR3")

    main_f_tab_3 = LabelFrame(tab_3, text="Parameters")
    left_f_tab_3 = Frame(main_f_tab_3)
    right_f_tab_3 = Frame(main_f_tab_3)
    txt_f_tab_3 = LabelFrame(tab_3, text="Results")

    # initial parameters

    lbl_1_tab_3 = Label(left_f_tab_3, text="Population size")
    lbl_2_tab_3 = Label(left_f_tab_3, text="Iterations number")
    lbl_3_tab_3 = Label(left_f_tab_3, text="Survivability")
    lbl_7_tab_3 = Label(left_f_tab_3, text="Mutation chance")
    lbl_4_tab_3 = Label(left_f_tab_3, text="Search point")
    lbl_5_tab_3 = Label(left_f_tab_3, text="Delay")
    lbl_6_tab_3 = Label(tab_3, text="Rosenbrock function")

    txt_1_tab_3 = Entry(right_f_tab_3)
    txt_1_tab_3.insert(0, "20")
    txt_2_tab_3 = Entry(right_f_tab_3)
    txt_2_tab_3.insert(0, "50")
    txt_3_tab_3 = Entry(right_f_tab_3)
    txt_3_tab_3.insert(0, "0.8")
    txt_4_tab_3 = Entry(right_f_tab_3)
    txt_4_tab_3.insert(0, "0.8")
    txt_5_tab_3 = Entry(right_f_tab_3)
    txt_5_tab_3.insert(0, "0.01")

    combo_tab_3 = Combobox(right_f_tab_3)
    combo_tab_3['values'] = ("Min", "Max")
    combo_tab_3.set("Min")

    txt_tab_3 = scrolledtext.ScrolledText(txt_f_tab_3)
    btn_del_tab_3 = Button(tab_3, text="Clear", command=delete_lab_3)
    btn_tab_3 = Button(tab_3, text="Start", command=draw_lab_3)

    lbl_6_tab_3.pack()
    main_f_tab_3.pack(expand=True)
    left_f_tab_3.pack(side=LEFT)
    right_f_tab_3.pack(side=RIGHT)

    lbl_1_tab_3.pack()
    lbl_2_tab_3.pack()
    lbl_3_tab_3.pack()
    lbl_7_tab_3.pack()
    lbl_5_tab_3.pack()
    # lbl_4_tab_3.pack()

    txt_1_tab_3.pack()
    txt_2_tab_3.pack()
    txt_3_tab_3.pack()
    txt_4_tab_3.pack()  # задержка в секундах
    txt_5_tab_3.pack()  # шанс мутации
    # combo_tab_3.pack()

    txt_tab_3.pack()

    btn_tab_3.pack()
    txt_f_tab_3.pack()
    btn_del_tab_3.pack()

    tab_control.pack()
    window.mainloop()


if __name__ == '__main__':
    main()
