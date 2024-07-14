# multicast data sender

```
rustam@nb-ubuntu-02:~/IP_edu/multicast-sender$ poetry run server
2024-07-14 15:31:45.884 | DEBUG    | multicast_sender.server:main:24 - len(tmp)=24, len(buffer)=24
2024-07-14 15:31:45.885 | INFO     | multicast_sender.server:main:29 - data_140724_15_31_45.bin saved!

```

```
rustam@nb-ubuntu-02:~/IP_edu/multicast-sender$ poetry run client -f README.md 
2024-07-14 15:31:45.884 | DEBUG    | multicast_sender.client:main:19 - len(tmp)=24
2024-07-14 15:31:45.884 | INFO     | multicast_sender.client:main:22 - README.md received

```
