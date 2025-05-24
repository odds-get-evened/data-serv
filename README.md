# Data Server

A lightweight Python package that implements a simple TCP streaming service and corresponding client to demonstrate streaming random data over a socket.

## Features

* **DataServer**: Listens on a configurable host and port. Accepts client connections and responds to commands. ([github.com](https://github.com/odds-get-evened/data-serv/raw/main/src/data_server/server.py))
* **Streaming**: Upon receiving the `data` command, streams random float values at one-second intervals. ([github.com](https://github.com/odds-get-evened/data-serv/raw/main/src/data_server/server.py))
* **Client**: Interactive command-line client to send commands (`data`) and receive streamed values or status messages. ([github.com](https://github.com/odds-get-evened/data-serv/raw/main/src/data_server/client.py))
* **Zero dependencies**: Built using Python standard library only (no external packages). ([github.com](https://github.com/odds-get-evened/data-serv/raw/main/setup.py))

## Requirements

* Python 3.12 or later.

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/odds-get-evened/data-serv.git
cd data-serv
pip install .
```

## Usage

### Running the server

```bash
python -m data_server.server [HOST] [PORT]
```

* **HOST**: IP address to bind (default: `127.0.0.1`)
* **PORT**: TCP port to listen on (default: `8080`)

Example:

```bash
python -m data_server.server 0.0.0.0 9000
```

### Running the client

```bash
python -m data_server.client [HOST] [PORT]
```

* **HOST** and **PORT** should match the server settings.

Once connected, at the prompt, enter:

* `data` to start streaming random values.
* Any other input will prompt usage instructions.

## Project Structure

```
data-serv/
├── src/
│   └── data_server/
│       ├── server.py        # DataServer implementation
│       └── client.py        # Interactive client
├── setup.py                 # Packaging information ([github.com](https://github.com/odds-get-evened/data-serv/raw/main/setup.py))
└── requirements.txt         # Minimal dependencies ([github.com](https://github.com/odds-get-evened/data-serv/raw/main/requirements.txt))
```

## License

This project is licensed under the GNU General Public License v3.0 or later. ([github.com](https://github.com/odds-get-evened/data-serv/raw/main/setup.py))

## Author

* Chris Walsh ([chris.is.rad@pm.me](mailto:chris.is.rad@pm.me))
