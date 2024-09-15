# rtl test journal 
## fm part
play fm radio by cli 
```bash 
rustam@nb-ubuntu-02:~/IP_edu/rtl_journal$ rtl_fm -M wbfm -f 100.5M -r 48k  - | aplay -r 24000 -f S16_LE -t raw -c 2
Found 1 device(s):
Playing raw data 'stdin' : Signed 16 bit Little Endian, Rate 24000 Hz, Stereo
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
Tuner gain set to automatic.
Tuned to 100771000 Hz.
Oversampling input by: 6x.
Oversampling output by: 1x.
Buffer size: 8.03ms
Exact sample rate is: 1020000.026345 Hz
Sampling at 1020000 S/s.
Output at 170000 Hz.
underrun!!! (at least 126,737 ms long)
```
for mono play
```bash 
rustam@nb-ubuntu-02:~/IP_edu/rtl_journal$ rtl_fm -M wbfm -f 100.5M -r 48k  - | aplay -r 48000 -f S16_LE -t raw -c 1
Playing raw data 'stdin' : Signed 16 bit Little Endian, Rate 48000 Hz, Mono
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
Tuner gain set to automatic.
Tuned to 100771000 Hz.
Oversampling input by: 6x.
Oversampling output by: 1x.
Buffer size: 8.03ms
Exact sample rate is: 1020000.026345 Hz
Sampling at 1020000 S/s.
Output at 170000 Hz.
underrun!!! (at least 125,732 ms long)
```
save and play 
```bash 
rustam@nb-ubuntu-02:~/IP_edu/rtl_journal$ rtl_fm -M wbfm -f 100.5M -r 48k  out_fm.raw
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
Tuner gain set to automatic.
Tuned to 100771000 Hz.
Oversampling input by: 6x.
Oversampling output by: 1x.
Buffer size: 8.03ms
Exact sample rate is: 1020000.026345 Hz
Sampling at 1020000 S/s.
Output at 170000 Hz.
^CSignal caught, exiting!

User cancel, exiting...
rustam@nb-ubuntu-02:~/IP_edu/rtl_journal$ aplay -r 48000 -f S16_LE -t raw -c 1 out_fm.raw 
Playing raw data 'out_fm.raw' : Signed 16 bit Little Endian, Rate 48000 Hz, Mono
```
## raw sdr
```bash
rustam@nb-ubuntu-02:~/IP_edu/rtl_journal$ rtl_sdr -f 100.5M -n 10000  out_sdr.bin
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
[R82XX] PLL not locked!
Sampling at 2048000 S/s.
Tuned to 100500000 Hz.
Tuner gain set to automatic.
Reading samples in async mode...

User cancel, exiting...

```
## python sample
```bash
pip install poetry==1.2
poetry install
```
[simple script](fft_show.py) 
![](fftimg.png)