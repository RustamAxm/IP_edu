from astropy.units.quantity_helper.function_helpers import piecewise
from rtlsdr import RtlSdr
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter1d
from scipy.signal import find_peaks

def main():
    sdr = RtlSdr()

    sdr.freq_correction = 60  # PPM
    sdr.gain = 'auto'
    sdr.sample_rate = 2.4e6 # Hz

    fft_size = 512
    spectrogram = np.array([])
    x_plots = np.array([])
    center_freqs = np.arange(90e6, 200e6, sdr.sample_rate)
    sdr.center_freq = center_freqs[0]
    for _ in range(5): # dummy wait
        x = sdr.read_samples(fft_size)

    for center in center_freqs:
        sdr.center_freq = center  # Hz
        x = sdr.read_samples(fft_size) # get all the samples we need for the spectrogram
        x_plots_ = np.linspace((sdr.center_freq + sdr.sample_rate / -2) / 1e6,
                              (sdr.center_freq + sdr.sample_rate / 2) / 1e6, fft_size)
        spectrogram_ = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x[0*fft_size:(0+1)*fft_size])))**2)
        spectrogram = np.concatenate((spectrogram, spectrogram_), axis=None)
        x_plots = np.concatenate((x_plots, x_plots_), axis=None)

    filtered = uniform_filter1d(spectrogram, size=30)
    peaks, _ = find_peaks(filtered, height=20, distance=50)

    print(f'{x_plots[peaks]=}')
    plt.figure()
    plt.plot(x_plots, spectrogram)
    plt.plot(x_plots, filtered)
    plt.plot(
        x_plots[peaks],
        filtered[peaks], "x", color="r")
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("intensity")
    plt.show()


if __name__ == '__main__':
    main()
