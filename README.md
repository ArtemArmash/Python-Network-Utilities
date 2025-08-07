# Python Cybersecurity and Network Scanning Toolkit

This repository contains a collection of powerful, standalone Python scripts designed for network scanning and web technology analysis. The toolkit leverages popular libraries like **Scapy**, **Requests**, and **BeautifulSoup** to perform a variety of tasks, from discovering hosts on a local network to identifying the technologies running on a web server.

## About The Project

This project is a practical demonstration of how Python can be used to build effective cybersecurity and network reconnaissance tools. It's an excellent portfolio piece for developers interested in ethical hacking, network administration, and automation. The scripts are designed to be modular, functional, and easy to understand.

## Toolkit Components

The repository includes several distinct tools, each with a specific purpose:

---

### 1. ARP Network Scanner (`my_arp_scanner.py`)

*   **Functionality**: Discovers active hosts on the local network using ARP "who-has" requests. It broadcasts a request to a specified IP range (e.g., `192.168.1.0/24`) and listens for replies.
*   **Output**: Prints a list of discovered devices with their corresponding IP and MAC addresses.
*   **Key Technology**: `Scapy` (for crafting and sending ARP packets).

---

### 2. TCP SYN Port Scanners

This toolkit includes three variations of a TCP SYN port scanner, a stealthy technique for checking if ports are open without completing a full TCP connection.

#### a. Single-Port SYN Scanner (`my_syn_scanner.py`)
*   **Functionality**: Scans a single, hardcoded port on a target IP or hostname. It sends a SYN packet and analyzes the flags of the response (SYN/ACK or RST/ACK) to determine the port's state. It also correctly sends a RST packet to close the half-open connection.
*   **Key Technology**: `Scapy`.

#### b. Multithreaded SYN Scanner (`multithread_syn_scanner.py`)
*   **Functionality**: An enhanced version of the SYN scanner that scans a list of ports in parallel using multithreading. This significantly speeds up the scanning process. It also includes basic error handling for non-integer port values.
*   **Key Technology**: `Scapy`, `threading`.

#### c. JSON-Driven SYN Scanner (`json_scanner.py`)
*   **Functionality**: A powerful, data-driven scanner that reads a list of targets and ports from a `targets.json` file. It scans each target and writes the results (open, closed, or unknown) back to a `results.json` file.
*   **Key Technology**: `Scapy`, `json`.

---

### 3. Web Technology Analyzer (`tech_analyzer/tech_analyzer.py`)

*   **Functionality**: Performs reconnaissance on a target website to identify the technologies it uses. It analyzes HTTP headers, meta tags, script and link tags, HTML comments, and page content to find signatures of common technologies like WordPress, Django, and Cloudflare.
*   **Output**: Prints a detailed report of its findings to the console.
*   **Key Technology**: `requests` (for making HTTP requests), `BeautifulSoup` (for parsing HTML).

## Setup and Installation

To use these tools, you need Python 3 and several external libraries.

### 1. Prerequisites
*   **Python 3**: Make sure you have Python 3 installed.
*   **Root/Administrator Privileges**: The SYN and ARP scanners require raw socket access to craft and send packets. You must run these scripts with `sudo` on Linux/macOS or as an Administrator on Windows.

### 2. Install Required Libraries
Open your terminal and run the following command to install all the necessary Python packages:
```sh
pip install scapy requests beautifulsoup4 lxml
```

### 3. Directory Structure
Ensure your project is organized as follows for the JSON-driven scanner and the tech analyzer to work correctly:
```
.
├── my_arp_scanner.py
├── my_syn_scanner.py
├── multithread_syn_scanner.py
├── json_scanner.py
├── json_files/
│   ├── targets.json
│   └── results.json
└── tech_analyzer/
    └── tech_analyzer.py
```

## How to Run the Scripts

Navigate to the project's root directory in your terminal and run the scripts as follows.

*   **ARP Scanner**:
    ```sh
    sudo python my_arp_scanner.py
    ```

*   **Single-Port SYN Scanner**:
    ```sh
    sudo python my_syn_scanner.py
    ```

*   **Multithreaded SYN Scanner**:
    ```sh
    sudo python multithread_syn_scanner.py
    ```

*   **JSON-Driven SYN Scanner**:
    *   First, edit `json_files/targets.json` to define your targets.
    *   Then, run the scanner:
        ```sh
        sudo python json_scanner.py
        ```
    *   Check `json_files/results.json` for the output.

*   **Web Technology Analyzer**:
    *   Navigate into the `tech_analyzer` directory:
        ```sh
        cd tech_analyzer
        ```
    *   Run the script:
        ```sh
        python tech_analyzer.py
        ```

---

**Disclaimer**: These tools are intended for educational purposes and for use on networks and systems where you have explicit permission to conduct scanning. Unauthorized scanning of networks is illegal and unethical.
```
