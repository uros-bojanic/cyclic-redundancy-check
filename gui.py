# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Uros Bojanic
# Created Date: 2022/03/14
# ---------------------------------------------------------------------------

# Python program to create a simple GUI using Tkinter
from crc_otr import crc_decode, crc_encode
from tkinter import *
import logging


# Function to decode information sequence using CRC
def keyboard_function_decode(label, sequence, generator):
    try:
        # Extract text from labels (textboxes)
        sequence_text = sequence.get()
        generator_text = generator.get()
        # Check for errors
        for text in [sequence_text, generator_text]:
            if len(text) <= 0:
                raise ValueError('Textbox empty.')
            if not all(character in "01" for character in text):
                raise ValueError('Textbox can only contain binary digits (0 or 1).')
        # Convert text to binary number
        seq = int("0b" + sequence_text, 2)
        gen = int("0b" + generator_text, 2)
        # Decode using cyclic redundancy check
        decoded = crc_decode(seq, gen)
        label.set("DECODED!\n" + str(decoded))
    except Exception as e:
        label.set("ERROR!\nInvalid input.")
        # logging.exception(e)


# Function to encode information sequence using CRC
def keyboard_function_encode(label, sequence, generator):
    try:
        # Extract text from labels (textboxes)
        sequence_text = sequence.get()
        generator_text = generator.get()
        # Check for errors
        for text in [sequence_text, generator_text]:
            if len(text) <= 0:
                raise ValueError('Textbox empty.')
            if not all(character in "01" for character in text):
                raise ValueError('Textbox can only contain binary digits (0 or 1).')
        # Convert text to binary number
        seq = int("0b" + sequence_text, 2)
        gen = int("0b" + generator_text, 2)
        # Encode using cyclic redundancy check
        encoded = crc_encode(seq, gen)
        label.set("ENCODED!\n" + str(bin(encoded)))
    except Exception as e:
        label.set("ERROR!\nInvalid input.")
        # logging.exception(e)


# Function to update expression in the text entry box
def keyboard_function_press(textbox, num):
    try:
        textbox.set(textbox.get() + str(num))
    except Exception as e:
        textbox.set("ERROR!\nInvalid input.")
        # logging.exception(e)


# Function to clear the contents of text entry box
def keyboard_function_delete(textbox):
    try:
        textbox.set(textbox.get()[:-1])
    except Exception as e:
        textbox.set("ERROR!\nInvalid input.")
        # logging.exception(e)


# Function to clear the contents of text entry box
def keyboard_function_clear(textbox):
    try:
        textbox.set("")
    except Exception as e:
        textbox.set("ERROR!\nInvalid input.")
        # logging.exception(e)


# Driver code
if __name__ == "__main__":
    # Logging configuration
    logging.basicConfig(
        filename='gui.log',
        filemode='a',
        level=logging.DEBUG,
        format='%(asctime)s:(levelname)s:%(message)s'
    )

    # GUI configuration
    bg_color = "light blue"

    # Create a GUI window using Tkinter
    gui = Tk()
    gui.title("Cyclic Redundancy Check (CRC) - GUI Application")
    gui.configure(background=bg_color)
    gui.resizable(False, False)
    # gui.geometry("450x650")

    # Create title label
    Label(gui, text="Cyclic Redundancy Check", font=('Helvetica bold', 20),
          anchor="center", bg=bg_color).grid(row=0, column=0, columnspan=4, ipady=10)

    # Create textbox for information sequence input
    textbox_seq = StringVar()
    textbox_seq_label = Label(gui, text='Information sequence:', bg=bg_color, font=('Helvetica', 7))
    textbox_seq_label.grid(row=1, column=0, columnspan=1, sticky="nsew")
    textbox_seq_field = Entry(gui, textvariable=textbox_seq)
    textbox_seq_field.grid(row=1, column=1, columnspan=3, sticky="nsew")
    textbox_seq.set("11011011011")  # initial value

    # Create keyboard buttons (`1`, `0`, `Delete`, `Clear`)
    button_height = 2
    button_width = 14

    # Button to input a '1' into the first input text-field (textbox_seq)
    button1 = Button(gui, text=' 1 ', fg='black',
                     command=lambda: keyboard_function_press(textbox_seq, 1),
                     height=button_height, width=button_width)
    button1.grid(row=2, column=0)

    # Button to input a '0' into the first input text-field (textbox_seq)
    button2 = Button(gui, text=' 0 ', fg='black',
                     command=lambda: keyboard_function_press(textbox_seq, 0),
                     height=button_height, width=button_width)
    button2.grid(row=2, column=1)

    # Button to delete last character from first input text-field (textbox_seq)
    delete = Button(gui, text='Delete', fg='black',
                    command=lambda: keyboard_function_delete(textbox_seq),
                    height=button_height, width=button_width)
    delete.grid(row=2, column=2)

    # Button to clear first input text-field (textbox_seq)
    clear = Button(gui, text='Clear', fg='black',
                   command=lambda: keyboard_function_clear(textbox_seq),
                   height=button_height, width=button_width)
    clear.grid(row=2, column=3)

    # Create textbox for information sequence input
    textbox_gen = StringVar()
    textbox_gen_label = Label(gui, text='Generator polynomial:', bg=bg_color, font=('Helvetica', 7))
    textbox_gen_label.grid(row=3, column=0, columnspan=1, sticky="nsew")
    textbox_gen_field = Entry(gui, textvariable=textbox_gen)
    textbox_gen_field.grid(row=3, column=1, columnspan=3, sticky="nsew")
    textbox_gen.set("10101")  # initial value

    # Create keyboard buttons (`1`, `0`, `Delete`, `Clear`)
    button_height = 2
    button_width = 14

    # Button to input a '1' into the second input text-field (textbox_gen)
    button1 = Button(gui, text=' 1 ', fg='black',
                     command=lambda: keyboard_function_press(textbox_gen, 1),
                     height=button_height, width=button_width)
    button1.grid(row=4, column=0)

    # Button to input a '0' into the second input text-field (textbox_gen)
    button2 = Button(gui, text=' 0 ', fg='black',
                     command=lambda: keyboard_function_press(textbox_gen, 0),
                     height=button_height, width=button_width)
    button2.grid(row=4, column=1)

    # Button to delete last character from second input text-field (textbox_gen)
    delete = Button(gui, text='Delete', fg='black',
                    command=lambda: keyboard_function_delete(textbox_gen),
                    height=button_height, width=button_width)
    delete.grid(row=4, column=2)

    # Button to clear second input text-field (textbox_gen)
    clear = Button(gui, text='Clear', fg='black',
                   command=lambda: keyboard_function_clear(textbox_gen),
                   height=button_height, width=button_width)
    clear.grid(row=4, column=3)

    # Padding between input section and action buttons (decode/encode)
    Label(gui, textvariable="", bg=bg_color).grid(row=5, column=0, columnspan=4)

    # Button to decode given information sequence & generator polynomial
    button_decode = Button(gui, text='Decode', fg='black',
                           command=lambda: keyboard_function_decode(text_result, textbox_seq, textbox_gen),
                           height=button_height, width=button_width)
    button_decode.grid(row=6, column=0, columnspan=2)

    # Button to encode given information sequence & generator polynomial
    button_encode = Button(gui, text='Encode', fg='black',
                           command=lambda: keyboard_function_encode(text_result, textbox_seq, textbox_gen),
                           height=button_height, width=button_width)
    button_encode.grid(row=6, column=2, columnspan=2)

    # Create result label
    text_result = StringVar()
    label_result = Label(gui, textvariable=text_result, font=('Helvetica bold', 14),
                         anchor="center", bg=bg_color).grid(row=7, column=0, columnspan=4, ipady=10)
    text_result.set("WELCOME!\nPlease press Decode/Encode.")

    # Create instructions label
    text_instructions = StringVar()
    label_instructions = Label(gui, textvariable=text_instructions, font=('Helvetica bold', 8),
                               anchor="sw", bg=bg_color).grid(row=8, column=0, columnspan=4)
    text_instructions.set("To use the CRC program, please input the binary representation of your\n"
                          "information sequence and generator polynomial into labeled text-fields above,\n"
                          "and click a button to either Decode or Encode the data block.")

    # start the GUI
    gui.mainloop()
