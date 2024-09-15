from rtlsdr import RtlSdr
import numpy as np
import matplotlib.pyplot as plt


def main():
    sdr = RtlSdr()

    sdr.freq_correction = 60  # PPM
    sdr.gain = 'auto'
    sdr.sample_rate = 2.4e6 # Hz

    fft_size = 4096
    spectrogram = np.array([])
    x_plots = np.array([])
    center_freqs = np.arange(80e6, 120e6, sdr.sample_rate)

    for center in center_freqs:
        sdr.center_freq = center  # Hz
        x = sdr.read_samples(fft_size) # get all the samples we need for the spectrogram
        x_plots_ = np.linspace((sdr.center_freq + sdr.sample_rate / -2) / 1e6,
                              (sdr.center_freq + sdr.sample_rate / 2) / 1e6, fft_size)
        spectrogram_ = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x[0*fft_size:(0+1)*fft_size])))**2)
        spectrogram = np.concatenate((spectrogram, spectrogram_), axis=None)
        x_plots = np.concatenate((x_plots, x_plots_), axis=None)

    plt.figure()
    plt.plot(x_plots, spectrogram)
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("intensity")
    plt.show()


if __name__ == '__main__':
    main()
