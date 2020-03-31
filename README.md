# Steam gaming analysis challenge

by Sebastian Wolf

## Content
The repo is organized in three folders:
- `code`: holds all notebooks, utility .py files, and notebooks saved as htmls for easy viewing
- `docker` : a dockerfile to re-create the environment I used. Clone the repository, cd into it's root, then run `docker-compose up` and open the jupyter notebooks.
- `html_maps` : a map output showing gamers geographical distribution

To re-un the analysis, copy the [steam data](https://storage.googleapis.com/datatonic-steam-gaming-challenge/steam_gaming_large.zip) into a `data` foder in the root of the repository.

## Solution
My solution to the challenge is split in three notebooks:
- [data_engineering.ipynb](./code/data_engineering.ipynb) / [data_engineering.html](./code/data_engineering.html) - (Exercise 1)
- [analytics.ipynb](./code/analytics.ipynb) / [analytics.html](./code/analytics.html) / [analytics.slides.html](./code/analytics.slides.html) - (Exercise 2)
- [advanced.ipynb](./code/advanced.ipynb) / [advanced.html](./code/advanced.html) - (Exercise 3)

***Note***: For the **analytics** challenge (Exercise 2), I created a slide set [analytics.slides.html](./code/analytics.slides.html), please read that instead of the notebook.
