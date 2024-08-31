from setuptools import setup
setup(name="Playlist_downloader",
      version="0.0.4",
      description="Playlist Downloader simplifies the process of downloading YouTube playlists by providing a straightforward API to fetch and save videos from a given playlist URL.",
      long_description=open('README.md').read(), 
      long_description_content_type='text/markdown',
      author="Deepanshu antil",
      maintainer="Deepanshu antil",
      packages=['Playlist_downloader'],
      author_email="deepanshuantil4113@gmail.com",
      url="https://github.com/deepanshu414/playlist_downloader",
      license="MIT", 
      install_requires=['pytube'])
