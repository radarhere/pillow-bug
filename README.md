# Pillow bug demo

Small VM demonstrating [Pillow#3066](https://github.com/python-pillow/Pillow/issues/3066).

## Installation

To run the VM, clone the repo and run

```
vagrant up
```

## Triggering the bug

Ssh into the machine:

```
vagrant ssh
```

Then:

```
cd /vagrant/files/
python3 test.py
```

it should read:

```
True
6.1.0
things work until...
Traceback (most recent call last):
  File "test.py", line 13, in <module>
    res = fnt.getmask("༄༅། །སྒྲུབ།", features=['ccmp', 'abvs', 'blws', 'calt', 'liga', 'kern', 'abvm', 'blwm', 'mkmk'])
  File "/usr/local/lib/python3.7/dist-packages/PIL/ImageFont.py", line 334, in getmask
    text, mode, direction=direction, features=features, language=language
  File "/usr/local/lib/python3.7/dist-packages/PIL/ImageFont.py", line 395, in getmask2
    size, offset = self.font.getsize(text, direction, features, language)
OSError: invalid face handle
Segmentation fault
```