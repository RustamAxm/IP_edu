from progress.colors import color
from rtlsdr import RtlSdr
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter1d
from scipy.signal import find_peaks


def main():
    sdr = RtlSdr()
    sdr.center_freq = 100.5e6  # Hz
    sdr.freq_correction = 60  # PPM
    sdr.gain = 'auto'
    sdr.sample_rate = 2.4e6 # Hz

    fft_size = 512
    num_rows = 1000
    x = sdr.read_samples(fft_size*num_rows) # get all the samples we need for the spectrogram
    spectrogram = np.zeros((num_rows, fft_size))
    for i in range(num_rows):
        spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x[i*fft_size:(i+1)*fft_size])))**2)
    extent = [(sdr.center_freq + sdr.sample_rate/-2)/1e6,
                (sdr.center_freq + sdr.sample_rate/2)/1e6,
                len(x)/sdr.sample_rate, 0]

    filtered = uniform_filter1d(spectrogram[200, :], size=30)
    peaks, _ = find_peaks(filtered, height=20, distance=50)

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(spectrogram, aspect='auto', extent=extent)
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Time [s]")
    plt.subplot(1, 2, 2)
    x_for_plot = np.linspace(
            (sdr.center_freq + sdr.sample_rate/-2)/1e6,
            (sdr.center_freq + sdr.sample_rate/2)/1e6, fft_size)
    plt.plot(
        x_for_plot,
        spectrogram[200, :],
        x_for_plot,
        filtered)
    plt.plot(
        x_for_plot[peaks],
        filtered[peaks], "x", color="r")
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("intensity")
    plt.show()


if __name__ == '__main__':
    main()
