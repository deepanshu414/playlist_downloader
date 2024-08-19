# Playlist Downloader

[![PyPI version](https://badge.fury.io/py/Playlist.svg)](https://badge.fury.io/py/Playlist)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Playlist Downloader is a robust Python library that simplifies the process of downloading entire YouTube playlists. It leverages the powerful pytube library to fetch and download videos at their highest available resolution.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Advanced Usage](#advanced-usage)
- [Configuration](#configuration)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)
- [Changelog](#changelog)
- [Roadmap](#roadmap)

## Features

- Effortless downloading of complete YouTube playlists
- Automatic selection of the highest available video resolution
- Customizable download path for organizing your media
- Progress tracking and error handling
- Support for both public and private playlists (with proper authentication)
- Multithreaded downloads for improved performance
- Resumable downloads in case of interruptions

## Installation

1. Install Playlist Downloader using pip:

```sh
pip install Playlist
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

## Usage
Here's a comprehensive example of how to use Playlist Downloader:
```python
from Playlist import download, set_config

# Configure download settings
set_config(
    max_resolution='720p',
    audio_only=False,
    download_captions=True,
    language='en'
)

# Download the playlist
playlist_id = 'PLxxxxxxxxxxxxxxxx'
download_path = '/path/to/download/folder'
download(playlist_id, download_path)
```
## Advanced Usage
### Handling Private Playlists
To download private playlists, you'll need to authenticate:
```python
from Playlist import authenticate, download

credentials = authenticate('path/to/credentials.json')
download('PLxxxxxxxxxxxxxxxx', '/download/path', credentials=credentials)
```
### Filtering Videos
You can apply filters to download only specific videos from a playlist:
```python
from Playlist import download, Filter

filter = Filter()
filter.add_date_range(start_date='2022-01-01', end_date='2022-12-31')
filter.add_duration_range(min_duration=300, max_duration=1200)  # 5-20 minutes

download('PLxxxxxxxxxxxxxxxx', '/download/path', filter=filter)
```
## Configuration
Customize the behavior of Playlist Downloader using the `set_config` function:
```python
from Playlist import set_config

set_config(
    max_threads=4,
    retry_attempts=3,
    timeout=30,
    proxy='http://proxy.example.com:8080'
)
```
## Requirements

- Python 3.7+
- pytube
- requests
- tqdm
## Contributing
We welcome contributions to Playlist Downloader! Here's how you can help:

1. Fork the repository
2. Create a new branch (git checkout -b feature/amazing-feature)
3. Make your changes
4. Run the tests (pytest)
5. Commit your changes (git commit -am 'Add some amazing feature')
6. Push to the branch (git push origin feature/amazing-feature)
7. Open a Pull Request

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Author
Deepanshu Antil - GitHub Profile
## Contact
For support or inquiries, please open an issue on the GitHub repository.
## Acknowledgments

- Thanks to the creators and maintainers of pytube for their excellent YouTube download library
- Inspired by the need for a simple, yet powerful playlist downloader
- Special thanks to all contributors who have helped improve this project
## Changelog
See CHANGELOG.md for a detailed history of changes to Playlist Downloader.
## Roadmap
Our plans for future development include:

- Support for other video platforms (e.g., Vimeo, Dailymotion)
- GUI interface for easier use by non-technical users
- Integration with media players for direct playback of downloaded content
- Advanced metadata extraction and organization features
