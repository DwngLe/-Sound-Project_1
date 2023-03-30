import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from signal_class import Signal
       
# Đọc hai đoạn âm thanh từ file
x, sample_rate1 = librosa.load('../sample_audio/au_02.wav')
y, sample_rate2 = librosa.load('../sample_audio/au_01.wav')

# Gắn 2 đoạn âm thanh vào Object
sound1 = Signal(x, sample_rate1)
sound2 = Signal(y, sample_rate2)

def dong_nhat(sound1, sound2):

    # Đồng nhất tần số lấy mẫu của hai tín hiệu âm thanh về cùng một giá trị
    if sound1.sample_rate != sound2.sample_rate:
        new_sample_rate = min(sound1.sample_rate,sound2.sample_rate)
        sound1.resample(new_sample_rate)
        sound2.resample(new_sample_rate)

    # Đồng nhất độ dài và gốc của 2 tín hiệu
    sound1.trim_signal(sound2)
    
    print("Đã đồng nhất")

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
    print("10. Nhân châp đoạn âm thanh 1 với đoạn âm thanh 2")
    print("11. Nhân tương quan đoạn âm thanh 1 với đoạn âm thanh 2")
    print("-------------------------------------------")
    print("Nhap lua chon:")

    lua_chon = int(input())

    print("-------------------------------------------")
    match lua_chon:
        case 0:
            break

        case 1:
            plt.figure(figsize=(8, 6))
            plt.subplot(2, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1 ban đầu")

            sound1.flipp_time()
            print("Đoạn âm thanh 1 đã được đảo")
            
            plt.subplot(2, 1, 2)
            sound1.plot_Signal("Đoạn âm thanh 1 sau khi đảo")
            plt.tight_layout()
            plt.show()

        case 2:
            print("Nhập thời gian cần dịch:")
            time = float(input())
            plt.figure(figsize=(8, 6))
            plt.subplot(2, 1, 1)
            
            sound1.plot_Signal("Đoạn âm thanh 1 ban đầu")
            shifted_signal = sound1.shift_left(time)
            print("Đoạn âm thanh 1 đã được dịch sang trái " + str(time) + 's')
            print("-----------------------")

            plt.subplot(2, 1, 2)
            shifted_signal.plot_Signal("Đoạn âm thanh 1 sau khi dịch trái")
            plt.tight_layout()
            plt.show()

        case 3:
            print("Nhập thời gian cần dịch:")
            time = float(input())
            plt.figure(figsize=(8,6))
            plt.subplot(2, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1 ban đầu")
          
            shifted_signal = sound1.shift_right(time)
            print("Đoạn âm thanh 1 đã được dịch sang phải " + str(time) + 's')

            plt.subplot(2, 1, 2)
            shifted_signal.plot_Signal("Đoạn âm thanh 1 sau khi dịch phải")
            plt.tight_layout()
            plt.show()

        case 4:
            dong_nhat(sound1, sound2)
            new_signal = sound1.add_w_sig(sound2)
            print("Đoạn âm thanh 1 cộng đoạn âm thanh 2!")
            print("__________________________________")
            
            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1")
        
            plt.subplot(3, 1, 2)
            sound2.plot_Signal("Đoạn âm thanh 2")

            plt.subplot(3, 1, 3)
            new_signal.plot_Signal("Đoạn âm thanh mới")

            plt.tight_layout()
            plt.show()

        case 5:
            dong_nhat(sound1, sound2)
            new_signal = sound1.sub_w_sig(sound2)
            print("Đoạn âm thanh 1 trừ đoạn âm thanh 2!")
            print("__________________________________")

            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1")
        
            plt.subplot(3, 1, 2)
            sound2.plot_Signal("Đoạn âm thanh 2")
           
            plt.subplot(3, 1, 3)
            new_signal.plot_Signal("Đoạn âm thanh mới")

            plt.tight_layout()
            plt.show()

        case 6:
            dong_nhat(sound1, sound2)
            new_signal = sound1.mul_w_sig(sound2)
            print("Đoạn âm thanh 1 nhân đoạn âm thanh 2!")
            print("__________________________________")

            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1")
        
            plt.subplot(3, 1, 2)
            sound2.plot_Signal("Đoạn âm thanh 2")

            plt.subplot(3, 1, 3)
            new_signal.plot_Signal("Đoạn âm thanh mới")

            plt.tight_layout()
            plt.show()

        case 7:
            print("Nhập hệ số")
            heso = int(input())
            new_signal = sound1.mul_w_num(heso)
        
            plt.figure(figsize=(8,6))
            plt.subplot(2, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1")

            plt.subplot(2, 1, 2)
            new_signal.plot_Signal("Đoạn âm thanh mới")

            plt.tight_layout()
            plt.show()

        case 8:
            dong_nhat(sound1, sound2)
            new_signal = sound1.divide_w_sig(sound2)
            print("Đoạn âm thanh 1 nhân đoạn âm thanh 2!")
            print("__________________________________")

            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1")
        
            plt.subplot(3, 1, 2)
            sound2.plot_Signal("Đoạn âm thanh 2")

            plt.subplot(3, 1, 3)
            new_signal.plot_Signal("Đoạn âm thanh mới")

            plt.tight_layout()
            plt.show()

        case 9:
            print("Nhập hệ số")
            heso = int(input())
            new_signal = sound1.divide_w_num(heso)
        
            plt.figure(figsize=(8,6))
            plt.subplot(2, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1")

            plt.subplot(2, 1, 2)
            new_signal.plot_Signal("Đoạn âm thanh mới")

            plt.tight_layout()
            plt.show()
            print("Done")

        case 20:
            print("Chọn đoạn âm thanh:")
            choose = int(input())
            if(choose == 1):
                sound1.plot_Signal("Đồ thị của đoạn âm thanh 1")
            else:
                sound2.plot_Signal("Đồ thị của đoạn âm thanh 2")
            plt.show()

        case 10:
            dong_nhat(sound1, sound2)
            new_signal = sound1.convolve_signal(sound2)
            print("Đoạn âm thanh 1 nhân đoạn âm thanh 2!")
            print("__________________________________")

            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1")
        
            plt.subplot(3, 1, 2)
            sound2.plot_Signal("Đoạn âm thanh 2")

            plt.subplot(3, 1, 3)
            new_signal.plot_Signal("Đoạn âm thanh mới")

            plt.tight_layout()
            plt.show()

        case 11:
            dong_nhat(sound1, sound2)
            new_signal = sound1.correlate_signal(sound2)
            print("Đoạn âm thanh 1 nhân đoạn âm thanh 2!")
            print("__________________________________")

            plt.figure(figsize=(8,6))
            plt.subplot(3, 1, 1)
            sound1.plot_Signal("Đoạn âm thanh 1")
        
            plt.subplot(3, 1, 2)
            sound2.plot_Signal("Đoạn âm thanh 2")

            plt.subplot(3, 1, 3)
            new_signal.plot_Signal("Đoạn âm thanh mới")

            plt.tight_layout()
            plt.show()


