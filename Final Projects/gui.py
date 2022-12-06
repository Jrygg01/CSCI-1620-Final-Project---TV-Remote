from tkinter import *
from tkVideoPlayer import TkinterVideo
import time


class GUI:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    VID_ONE = 'Skeleton - 84705.mp4'
    VID_TWO = 'Energy Field - 74933.mp4'
    VID_THREE = 'istockphoto-940028270-640_adpp_is.mp4'
    VID_FOUR = 'istockphoto-1326362231-640_adpp_is.mp4'

    def __init__(self, window: Tk) -> None:
        '''
        This is the constructor, declares basic variables, configures GUI grid layout, configures videos,
        and other various GUI parts.
        :param window: class imported from Tkinter that sets things like window sizing
        '''
        self.__status = False
        self.__muted = False
        self.__volume = GUI.MIN_VOLUME
        self.__channel = GUI.MIN_CHANNEL

        self.window = window
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        self.window.columnconfigure(4, weight=1)
        self.window.columnconfigure(5, weight=1)
        self.window.columnconfigure(6, weight=1)

        # #Video
        self.videoplayer = TkinterVideo(master=window, scaled=True)
        self.videoplayer.load(GUI.VID_ONE)
        self.videoplayer.grid(row=0, column=3, pady=2)

        # Power
        self.button_power = Button(self.window, text='Power', command=self.power)
        self.button_power.grid(row=2, column=3, pady=2)

        # Mute
        self.button_mute = Button(self.window, text='Mute', command=self.mute)
        self.button_mute.grid(row=3, column=3, pady=2)

        # Channel
        self.button_channelUp = Button(self.window, text='Channel Up', command=self.channel_up)
        self.button_channelDown = Button(self.window, text='Channel Down', command=self.channel_down)
        self.label_channel = Label(self.window, text='Channel = 0')
        self.button_channelUp.grid(row=1, column=2, sticky=W, pady=2)
        self.button_channelDown.grid(row=2, column=2, sticky=W, pady=2)
        self.label_channel.grid(row=0, column=2, sticky=W, pady=2)

        # Volume
        self.button_volumeUp = Button(self.window, text='Volume +', command=self.volume_up)
        self.button_volumeDown = Button(self.window, text='Volume -', command=self.volume_down)
        self.label_volume = Label(self.window, text='Volume = 0')
        self.button_volumeUp.grid(row=1, column=4, sticky=E, pady=2)
        self.button_volumeDown.grid(row=2, column=4, sticky=E, pady=2)
        self.label_volume.grid(row=0, column=4, sticky=E, pady=2)

        # volume slider
        self.volume_slider = Scale(self.window, from_=GUI.MIN_VOLUME, to=GUI.MAX_VOLUME, orient=HORIZONTAL,
                                   showvalue=False, label='       Volume ',
                                   command=self.change_volume)
        self.volume_slider.grid(row=1, column=3, pady=2)

    # Change position of volume slider
    def change_volume(self, value: int) -> None:
        '''
        Function for changing volume, changes slider GUI and produces text showing volume :param value: It is a
        mystery value, that seems to affect the ability to use the slider in order to change volume. :return: None
        '''
        if self.__status:
            self.__volume = int(value)
            self.label_volume['text'] = f'Volume = {self.__volume}'
        else:
            self.volume_slider.set(GUI.MIN_VOLUME)

    # turn TV on/off
    def power(self) -> None:
        '''
        Function that allows the tv to turn on and turn off, also handles showing videos and removing them.
        :return: None
        '''
        if not self.__status:
            self.__status = True
            self.play()
        else:
            self.__status = False
            self.videoplayer.grid_forget()
            self.videoplayer.stop()

    # Mute TV
    def mute(self) -> None:
        '''
        Function mutes the tv and unmutes it. Adjusts slider aswell, and changes GUI labels to account for mute.
        :return: None
        '''
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.label_volume['text'] = f'Volume = Muted'
                #self.volume_slider.set(GUI.MIN_VOLUME)
            else:
                self.__muted = False
                self.label_volume['text'] = f'Volume = {self.__volume}'
                self.volume_slider.set(self.__volume)

    # Turn volume up
    def volume_up(self) -> None:
        '''
        Fucntion adjusts volume of TV, checks if on and if muted, changes self.__volume, and adjusts GUI labels and
        GUI slider.
        :return: None:
        '''
        if self.__status:
            if not self.__muted:
                if self.__volume == GUI.MAX_VOLUME:
                    pass
                else:
                    self.__volume += 1
                    self.label_volume['text'] = f'Volume: {self.__volume}'
                    self.volume_slider.set(self.__volume)

        else:
            pass

    # Turn volume down
    def volume_down(self) -> None:
        '''
        Fucntion adjusts volume of TV, checks if on and if muted, changes self.__volume, and adjusts GUI labels and
        GUI slider.
        :return: None:
        '''
        if self.__status:
            if not self.__muted:
                if self.__volume == GUI.MIN_VOLUME:
                    pass
                else:
                    self.__volume -= 1
                    self.label_volume['text'] = f'Volume: {self.__volume}'
                    self.volume_slider.set(self.__volume)

        else:
            pass

    # Increase channel
    def channel_up(self) -> None:
        '''
        Fucntion adjusts channel of TV, checks if on, changes self.__channel, and adjusts GUI labels and
        GUI slider. Also loads videos based on selected channel as well as stopping video in order to change them.
        :return: None:
        '''

        if self.__channel >= GUI.MAX_CHANNEL and self.__status:
            self.__channel = GUI.MIN_CHANNEL
            self.label_channel['text'] = f'Channel: {self.__channel}'

            if self.__channel == 0:
                self.videoplayer.load(GUI.VID_ONE)
            elif self.__channel == 1:
                self.videoplayer.load(GUI.VID_TWO)
            elif self.__channel == 2:
                self.videoplayer.load(GUI.VID_THREE)
            elif self.__channel == 3:
                self.videoplayer.load(GUI.VID_FOUR)

        elif self.__status:
            self.__channel += 1
            self.label_channel['text'] = f'Channel: {self.__channel}'

            if self.__channel == 0:
                self.videoplayer.load(GUI.VID_ONE)
            elif self.__channel == 1:
                self.videoplayer.load(GUI.VID_TWO)
            elif self.__channel == 2:
                self.videoplayer.load(GUI.VID_THREE)
            elif self.__channel == 3:
                self.videoplayer.load(GUI.VID_FOUR)

        self.stop()

    # Decrease channel
    def channel_down(self) -> None:
        '''
        Fucntion adjusts channel of TV, checks if on, changes self.__channel, and adjusts GUI labels and
        GUI slider. Also loads videos based on selected channel as well as stopping video in order to change them.
        :return: None:
        '''

        if self.__channel <= GUI.MIN_CHANNEL and self.__status:
            self.__channel = GUI.MAX_CHANNEL
            self.label_channel['text'] = f'Channel: {self.__channel}'

            if self.__channel == 0:
                self.videoplayer.load(GUI.VID_ONE)
            elif self.__channel == 1:
                self.videoplayer.load(GUI.VID_TWO)
            elif self.__channel == 2:
                self.videoplayer.load(GUI.VID_THREE)
            elif self.__channel == 3:
                self.videoplayer.load(GUI.VID_FOUR)

        elif self.__status:
            self.__channel -= 1
            self.label_channel['text'] = f'Channel: {self.__channel}'

            if self.__channel == 0:
                self.videoplayer.load(GUI.VID_ONE)
            elif self.__channel == 1:
                self.videoplayer.load(GUI.VID_TWO)
            elif self.__channel == 2:
                self.videoplayer.load(GUI.VID_THREE)
            elif self.__channel == 3:
                self.videoplayer.load(GUI.VID_FOUR)

        self.stop()

    # Play videos
    def play(self) -> None:
        '''
        Function to play videos, if tv powered on, also sets the video up in GUI grid.
        :return: None
        '''
        if self.__status:
            self.videoplayer.grid(row=0, column=3, pady=2)
            self.videoplayer.play()

    # Stop playing videos
    def stop(self) -> None:
        '''
        Function to stop videos, if tv powered on, also removes the video from the GUI grid.
        :return: None
        '''
        self.videoplayer.grid_forget()
        self.videoplayer.stop()
        time.sleep(.1)
        self.play()
