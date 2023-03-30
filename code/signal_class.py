import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

class Signal:
    def __init__(self, samples, sample_rate):
        self.samples = samples
        self.start_pos= 0
        self.sample_rate = sample_rate
        self.length = len(self.samples)

    def resample(self, new_sample_rate):
        if self.sample_rate != new_sample_rate:
            self.samples, self.sample_rate = librosa.resample(self.samples, self.sample_rate, new_sample_rate)
    
    def trim_signal(self, other_signal):
        if len(self.samples) > len(other_signal.samples):
            self.samples = self.samples[:len(other_signal.samples)]
        elif len(self.samples) < len(other_signal.samples):
            other_signal.samples = other_signal.samples[:len(self.samples)]
    
    def flipp_time(self):
        self.samples = np.flip(self.samples)

    def shift_left(self, shift_value):
        shift_samples = int(shift_value * self.sample_rate)
        shifted_audio = np.roll(self.samples, -shift_samples)
        return Signal(shifted_audio, self.sample_rate)
       
    def shift_right(self, shift_value):
        shift_samples = int(shift_value * self.sample_rate)
        shifted_audio = np.roll(self.samples, shift_samples)
        return Signal(shifted_audio, self.sample_rate)
    
    def add_w_sig(self, other_signal):
        new_samples = np.add(self.samples, other_signal.samples)
        new_samples_rate = self.sample_rate
        return Signal(new_samples, new_samples_rate)

    def sub_w_sig(self, other_signal):
        new_samples = np.subtract(self.samples, other_signal.samples)
        new_samples_rate = self.sample_rate
        return Signal(new_samples, new_samples_rate)

    def mul_w_num(self, heso):
        new_samples = np.multiply(self.samples, heso)
        new_samples_rate = self.sample_rate
        return Signal(new_samples, new_samples_rate)
    
    def divide_w_num(self, heso):
        new_samples = np.divide(self.samples, heso)
        new_samples_rate = self.sample_rate
        return Signal(new_samples, new_samples_rate)
    
    def mul_w_sig(self, other_signal):
        new_samples = np.multiply(self.samples, other_signal.samples)
        new_samples_rate = self.sample_rate
        return Signal(new_samples, new_samples_rate)
    
    def divide_w_sig(self, other_signal):
        new_samples = np.divide(self.samples, other_signal.samples)
        new_samples_rate = self.sample_rate
        return Signal(new_samples, new_samples_rate)
    
    # def trim_Signal(self):
    #     sound_trimmed, _ = librosa.effects.trim(self, top_db=20)
    #     return sound_trimmed

    def plot_Signal(self, title):
        duration = len(self.samples) /self.sample_rate
        time = np.linspace(0, duration, num=len(self.samples))
        plt.plot(time, self.samples)
        plt.title(title)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')

    def convolve_signal(self, other_signal):
        new_samples = np.convolve(self.samples, other_signal.samples, mode='full')
        new_samples_rate = self.sample_rate
        return Signal(new_samples, new_samples_rate)

    def correlate_signal(self, other_signal):
        new_samples = np.correlate(self.samples, other_signal.samples, mode='full')
        new_samples_rate = self.sample_rate
        return Signal(new_samples, new_samples_rate)