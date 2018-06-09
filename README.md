# CryptonoteEvo Easy Miner

The most easy, intuitive CPU miner for cryptonote-based cryptocurrencies like SUMOKOIN (SUMO), Monero (XMR), Aeon (AEON) etc.

![](http://www.sumokoin.org/images/easy-miner-features_1080x1100.png)

## USAGE

### Download

**Windows and Mac OS X**

Need Compile.

**Linux**
- Clone `git clone https://github.com/Nur1Labs/CryptonoteEvo-EasyMiner.git`.
- Clone `git clone https://github.com/Nur1Labs/CryptonoteEvo-Hash-Lib`.

### Install Dependencies
- `sudo apt-get install cmake gcc python-dev python-pip python-pyside`
-  `pip install psutil`

### Compile library and run
- `cd /path/to/CryptonoteEvo-Hash-Lib`
- `cmake .`

The last lines of the output should look something like this:
```
-- Configuring done
-- Generating done
-- Build files have been written to: /path/to/CryptonoteEvo-Hash-Lib
```
- `make`

The last lines of the output should look something like this:
```
[100%] Linking C shared library evo_hash.so
[100%] Built target evo_hash
```
- Copy just created `evo_hash.so` from `CryptonoteEvo-Hash-Lib` folder to `/path/to/evo/libs` folder.
```
- Run the miner with `python evominer.py`
- Start mining
```

## Donation Support

https://github.com/FndNur1Labs/CryptonoteEvo
