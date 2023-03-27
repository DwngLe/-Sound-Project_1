import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

class Signal:
    def __init__(self, samples, sample_rate):
        self.samples = samples
        self.sample_rate = sample_rate
        self.length = len(self.samples)

    def resample(self, new_sample_rate):
        if self.sample_rate != new_sample_rate:
            self.samples = librosa.resample(self.samples, self.sample_rate, new_sample_rate)
            self.sample_rate = new_sample_rate
    
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

       
# Đọc hai đoạn âm thanh từ file
x, sample_rate1 = librosa.load('../sample_audio/au_02.wav')
y, sample_rate2 = librosa.load('../sample_audio/au_01.wav')

# Gắn 2 đoạn âm thanh vào Object
sound1 = Signal(x, sample_rate1)
sound2 = Signal(y, sample_rate2)

def dong_nhat(sound1, sound2):
    print("Độ lớn và tần số lấy mẫu ban đầu:")
    # print("__________________________________")
    print(sound1.length)
    print(sound1.sample_rate)
    print(sound2.length)
    print(sound2.sample_rate)
    print("__________________________________")


    # Đồng nhất tần số lấy mẫu của hai tín hiệu âm thanh về cùng một giá trị
    if sound1.sample_rate != sound2.sample_rate:
        new_sample_rate = min(sound1.sample_rate, sound2.sample_rate)
        sound1.resample(new_sample_rate)
        sound2.resample(new_sample_rate)

    # Đồng nhất độ dài và gốc của 2 tín hiệu
    sound1.trim_signal(sound2)

    print("Độ lớn và tần số lấy mẫu sau khi đồng nhất:")
    # print("__________________________________")
    print(len(sound1.samples))
    print(sound1.sample_rate)
    print(len(sound2.samples))
    print(sound2.sample_rate)
    print("__________________________________")
        
while(True):
    print("---------------------Menu-----------------")
    print("0. Thoát")
    print("1. Đảo ngược đoạn âm thanh 1")
    print("2. Dịch đoạn âm thanh 1 sang trái")
    print("3. Dịch đoạn âm thanh 1 sang phải")
    print("4. Cộng đoạn âm thanh 1 với đoạn âm thanh 2")
    print("5. Trừ đoạn âm thanh 1 với đoạn âm thanh 2")
    print("6. Nhân đoạn âm thanh 1 với đoạn âm thanh 2")
    print("7. Nhân đoạn âm thanh 1 với 1 số")
    print("8. Chia đoạn âm thanh 1 với đoạn âm thanh 2")
    print("9. Chia đoạn âm thanh 1 với 1 số")
    print("-------------------------------------------")
    print("Nhap lua chon:")

    lua_chon = int(input())

    print("-------------------------------------------")
    match lua_chon:
        case 0:
            break
        case 1:
            plt.figure(figsize=(8,6))
            plt.subplot(2, 1, 1)
            plt.plot(sound1.samples)
            print(sound1.samples)
            plt.title('Đoạn âm thanh 1 ban đầu')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            sound1.flipp_time()
            print("Đoạn âm thanh 1 đã được đảo")
        
            plt.subplot(2, 1, 2)
            plt.plot(sound1.samples)
            print(sound1.samples)
            plt.title('Đoạn âm thanh 1 sau khi đảo')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.tight_layout()
            plt.show()

        case 2:
            print("Nhập thời gian cần dịch:")
            time = float(input())
            plt.figure(figsize=(8,6))
            plt.subplot(2, 1, 1)
            plt.plot(sound1.samples)
        
            plt.title('Đoạn âm thanh 1 ban đầu')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            print("-----------------------")
            print("Samples của đoạn âm thanh 1:")
            print(sound1.samples)
            print("-----------------------")

            shifted_signal = sound1.shift_left(time)
            print("Đoạn âm thanh 1 đã được dịch sang trái " + str(time) + 's')
            print("-----------------------")
            print("Samples của đoạn âm thanh 1:")
            print(sound1.samples)
            print("-----------------------")

            plt.subplot(2, 1, 2)
            plt.plot(shifted_signal.samples)
        
            plt.title('Đoạn âm thanh 1 sau khi dịch')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.tight_layout()
            plt.show()

        case 3:
            print("Nhập thời gian cần dịch:")
            time = float(input())
            plt.figure(figsize=(8,6))
            plt.subplot(2, 1, 1)
            plt.plot(sound1.samples)
            plt.title('Đoạn âm thanh 1 ban đầu')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            print("-----------------------")
            print("Samples của đoạn âm thanh 1:")
            print(sound1.samples)
            print("-----------------------")

            shifted_signal = sound1.shift_right(time)
            print("Đoạn âm thanh 1 đã được dịch sang phải " + str(time) + 's')

            print("-----------------------")
            print("Samples của đoạn âm thanh 1:")
            print(sound1.samples)
            print("-----------------------")

            plt.subplot(2, 1, 2)
            plt.plot(shifted_signal.samples)
            plt.title('Đoạn âm thanh 1 sau khi dịch')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.tight_layout()
            plt.show()

        case 4:
            dong_nhat(sound1, sound2)
            new_signal = sound1.add_w_sig(sound2)

            print("Đoạn âm thanh 1 cộng đoạn âm thanh 2!")
            print("Độ lớn và tần số của mẫu âm thanh mới:")
            print(len(new_signal.samples))
            print(new_signal.sample_rate)
            print("__________________________________")
            
            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            plt.plot(sound1.samples)
            plt.title('Đoạn âm thanh 1')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')
        
            plt.subplot(3, 1, 2)
            plt.plot(sound2.samples)
            plt.title('Đoạn âm thanh 2')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.subplot(3, 1, 3)
            plt.plot(new_signal.samples)
            plt.title('Đoạn âm thanh mới')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.tight_layout()
            plt.show()

        case 5:
            dong_nhat(sound1, sound2)
            new_signal = sound1.sub_w_sig(sound2)

            print("Đoạn âm thanh 1 trừ đoạn âm thanh 2!")
            print("Độ lớn và tần số của mẫu âm thanh mới:")
            print(len(new_signal.samples))
            print(new_signal.sample_rate)
            print("__________________________________")

            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            plt.plot(sound1.samples)
            plt.title('Đoạn âm thanh 1')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')
        
            plt.subplot(3, 1, 2)
            plt.plot(sound2.samples)
            plt.title('Đoạn âm thanh 2')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.subplot(3, 1, 3)
            plt.plot(new_signal.samples)
            plt.title('Đoạn âm thanh mới')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.tight_layout()
            plt.show()

        case 6:
            dong_nhat(sound1, sound2)
            new_signal = sound1.mul_w_sig(sound2)

            print("Đoạn âm thanh 1 nhân đoạn âm thanh 2!")
            print("Độ lớn và tần số của mẫu âm thanh mới:")
            print(len(new_signal.samples))
            print(new_signal.sample_rate)
            print("__________________________________")

            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            plt.plot(sound1.samples)
            plt.title('Đoạn âm thanh 1')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')
        
            plt.subplot(3, 1, 2)
            plt.plot(sound2.samples)
            plt.title('Đoạn âm thanh 2')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.subplot(3, 1, 3)
            plt.plot(new_signal.samples)
            plt.title('Đoạn âm thanh mới')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.tight_layout()
            plt.show()

        case 7:
            print("Nhập hệ số")
            heso = int(input())
            new_signal = sound1.mul_w_num(heso)
        
            plt.figure(figsize=(8,6))
            plt.subplot(2, 1, 1)
            plt.plot(sound1.samples)
            plt.title('Đoạn âm thanh 1')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.subplot(2, 1, 2)
            plt.plot(new_signal.samples)
            plt.title('Đoạn âm thanh mới')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.tight_layout()
            plt.show()
            print("Done")

        case 8:
            dong_nhat(sound1, sound2)
            new_signal = sound1.divide_w_sig(sound2)

            print("Đoạn âm thanh 1 nhân đoạn âm thanh 2!")
            print("Độ lớn và tần số của mẫu âm thanh mới:")
            print(len(new_signal.samples))
            print(new_signal.sample_rate)
            print("__________________________________")

            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            plt.plot(sound1.samples)
            plt.title('Đoạn âm thanh 1')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')
        
            plt.subplot(3, 1, 2)
            plt.plot(sound2.samples)
            plt.title('Đoạn âm thanh 2')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.subplot(3, 1, 3)
            plt.plot(new_signal.samples)
            plt.title('Đoạn âm thanh mới')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.tight_layout()
            plt.show()

        case 9:
            print("Nhập hệ số")
            heso = int(input())
            new_signal = sound1.divide_w_num(heso)
        
            plt.figure(figsize=(8,6))
            plt.subplot(2, 1, 1)
            plt.plot(sound1.samples)
            plt.title('Đoạn âm thanh 1')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.subplot(2, 1, 2)
            plt.plot(new_signal.samples)
            plt.title('Đoạn âm thanh mới')
            plt.xlabel('Thời gian')
            plt.ylabel('Samples')

            plt.tight_layout()
            plt.show()
            print("Done")


