# Grayscale Applet

A lightweight system tray applet for Linux that toggles all connected displays between grayscale and normal color modes using [vibrant-cli](https://github.com/libvibrant/libvibrant).

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Troubleshooting](#troubleshooting)  
- [Tested Environment](#tested-environment)  
- [Author](#author)  
- [License](#license)  
- [References](#references)  

---

## Overview

The Grayscale Applet is a simple GTK3-based system tray application indicator that allows you to switch all connected monitors to grayscale mode or back to normal color mode easily. It relies on the external command-line tool `vibrant-cli` from the libvibrant project to perform the display color adjustments.

---

## Features

- System tray icon for quick access  
- Menu options to switch to grayscale or normal display modes  
- Supports multiple connected monitors automatically  
- About dialog with version and author info  
- Minimal dependencies and lightweight  

---

## Requirements

- Linux distribution running X11 (not Wayland)  
- Python 3  
- GTK 3 library (`gir1.2-gtk-3.0`)  
- AppIndicator3 library (`gir1.2-appindicator3-0.1`)  
- `xrandr` command-line tool for monitor detection  
- Build tools and dependencies for `vibrant-cli` (CMake, GCC, etc.)  

---

## Installation

Follow these steps to install and run the Grayscale Applet:

1. **Update your package lists:**

    ```bash
    sudo apt update
    ```

2. **Install required system dependencies:**

    ```bash
    sudo apt install -y \
      python3 python3-gi gir1.2-gtk-3.0 gir1.2-appindicator3-0.1 \
      x11-xserver-utils git build-essential cmake libgtk-3-dev libx11-dev libxrandr-dev
    ```

3. **Create a directory for applications if it doesn't exist:**

    ```bash
    mkdir -p $HOME/Applications
    ```

4. **Clone and build `libvibrant`:**

    ```bash
    cd $HOME/Applications
    git clone https://github.com/libvibrant/libvibrant.git
    cd libvibrant
    mkdir build && cd build
    cmake ..
    make
    ```

    After building, ensure the `vibrant-cli` binary is located at:  
    `$HOME/Applications/libvibrant/build/vibrant-cli/vibrant-cli`

5. **Clone this Grayscale Applet repository:**

    ```bash
    cd $HOME/Applications
    git clone https://github.com/yourusername/grayscale-applet.git
    cd grayscale-applet
    ```

6. **Make the applet script executable:**

    ```bash
    chmod +x grayscale_applet.py
    ```

7. **Run the applet:**

    ```bash
    ./grayscale_applet.py
    ```

---

## Usage

- After launching, a tray icon labeled "display" appears in your system tray.  
- Click or right-click the icon to open the menu.  
- Select **Grayscale mode** to convert all monitors to grayscale.  
- Select **Normal mode** to restore normal colors.  
- Select **About** for version and author info.  
- Select **Quit** to exit the applet.  

---

## Configuration

- The path to `vibrant-cli` is hardcoded to:

~/Applications/libvibrant/build/vibrant-cli/vibrant-cli

- If your `vibrant-cli` is installed elsewhere, edit the `run_vibrant_cli` method in `grayscale_applet.py` accordingly.

- Requires X11 display server and `xrandr` to detect connected monitors.

---

## Troubleshooting

- **Tray icon missing:**  
Ensure your desktop environment supports AppIndicator icons. Some require additional extensions or plugins.

- **`vibrant-cli` errors or not found:**  
Confirm the binary exists and has execute permissions. Verify the path is correct.

- **Display color doesn't change:**  
Verify `xrandr` outputs connected monitors correctly, and you have permission to change display settings.

- **Missing dependencies:**  
Check all required packages are installed.

---

## Tested Environment

- Linux Mint 21.1 Vera  
- Kernel 5.15.0-73-generic x86_64  
- Desktop Environment: Xfce 4.16.0  
- CPU: Intel Core i5-9400F  
- GPU: AMD Radeon RX 6600 XT (amdgpu driver)  
- OpenGL: 4.6 Mesa 22.2.5  
- RAM: 31.29 GiB  

---

## Author

**Thomas L.C. van Houten**  
- Created: 2023-05-07  
- Last Modified: 2023-06-13  
- Version: 0.0.6  

---

## License

Provided as-is, no warranty. Use, modify, and redistribute freely.

---

## References

- [libvibrant GitHub](https://github.com/libvibrant/libvibrant)  
- [GTK 3 Documentation](https://www.gtk.org/docs/)  
- [AppIndicator3 API Reference](https://developer.gnome.org/libappindicator/)  
- [`xrandr` man page](https://www.x.org/releases/X11R7.5/doc/man/man1/xrandr.1.html)  

---

## Contact

Open issues or pull requests in the GitHub repository for questions or suggestions.
