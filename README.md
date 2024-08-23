<div align="center">
<img src="https://socialify.git.ci/deepanshu414/playlist_downloader/image?description=1&descriptionEditable=Playlist%20Downloader%20simplifies%20the%20process%20of%20downloading%20YouTube%20playlists%20by%20providing%20a%20straightforward%20API%20to%20fetch%20and%20save%20videos%20from%20a%20given%20playlist%20URL.&font=KoHo&forks=1&issues=1&language=1&name=1&pattern=Plus&pulls=1&stargazers=1&theme=Auto" alt="Playlist    " width="640" height="320" />
</div>

Playlist Downloader is a robust Python library that simplifies the process of downloading entire YouTube playlists. It leverages the powerful pytube library to fetch and download videos at their highest available resolution.

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Badges](#badges)
- [Installation](#installation)
- [Usage/Example](#usageexample)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Contact](#contact)

## Features

1. **Streamlined Playlist Acquisition**
   - Effortlessly download entire YouTube playlists with a single command

2. **Intelligent Quality Selection**
   - Automatic acquisition of the highest available video resolution

3. **Flexible File Management**
   - User-defined download directory for organized media storage
4. **Format Versatility**
   - Support for multiple output formats (MP4, MKV, etc.)

## Badges
![PyPI version](https://badge.fury.io/py/Playlist.svg)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

## Installation

1. Install Playlist Downloader using pip:

```sh
pip install Playlist_downloader
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
from Playlist_downloader import download

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
