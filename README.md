# Playlist Downloader

[![PyPI version](https://badge.fury.io/py/Playlist.svg)](https://badge.fury.io/py/Playlist)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Playlist Downloader is a robust Python library that simplifies the process of downloading entire YouTube playlists. It leverages the powerful pytube library to fetch and download videos at their highest available resolution.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage/Example](#usageexample)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Contact](#contact)

## Features

- Effortless downloading of complete YouTube playlists
- Automatic selection of the highest available video resolution
- Customizable download path for organizing your media
- Progress tracking and error handling

## Installation

1. Install Playlist Downloader using pip:

```sh
pip install PlayList
```
2. For the latest development version, you can install directly from the GitHub repository:
```sh
pip install git+https://github.com/deepanshu414/playlist-downloader.git
```
3. Clone the repository:
```sh
git clone https://github.com/deepanshu414/playlist-downloader.git
```
4. Navigate to the project directory:
```sh
cd playlist-downloader
```

## Usage/Example
Here's a comprehensive example of how to use Playlist Downloader:
```python
from PlayList import download

def download_playlist():
    # Extract the playlist ID from the full URL
    # For example, from 'https://www.youtube.com/playlist?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0'
    # we extract 'PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0'
    playlist_id = 'PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0'

    # Specify the path where the playlist videos will be downloaded
    download_path = '/path/to/download/folder'

    # Call the download function with the playlist ID and download path
    download(playlist_id, download_path)

if __name__ == "__main__":
    # Execute the download_playlist function when the script is run directly
    download_playlist()
```

## Requirements

- Python 3.7+
- `pytube` library

## Contributing
We welcome contributions to Playlist Downloader! Here's how you can help:

1. Fork the repository
2. Create a new branch (git checkout -b feature/amazing-feature)
3. Make your changes
4. Run the tests (pytest)
5. Commit your changes (git commit -am 'Add some amazing feature')
6. Push to the branch (git push origin feature/amazing-feature)
7. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Author
Deepanshu Antil - [GitHub Profile](https://github.com/deepanshu414)
## Contact
For support or inquiries, please open an issue on the GitHub repository.
