<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/krea_ai/open-prompts">
    <img src="static/krea.gif" alt="Logo" width="auto" height="200">
  </a>

<h3 align="center">open prompts</h3>

  <p align="center">
    open knowledge base of prompts.
    <br />
    <a href="https://krea.ai"><strong>explore prompts</strong></a>
    <br />
    <br />
    <a href="https://theprompter.substack.com/">newsletter</a>
    ·
    <a href="https://discord.gg/3mkFbvPYut">community</a>
    ·
    <a href="#contributing">contribute</a>
  </p>
  <p align="center">
    <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/krea_ai">
  </p>
</div>

<!-- ABOUT THE PROJECT -->

# Open Prompts

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Open Prompts contains the data we use to build [krea.ai](krea.ai). You can get access to this data too.

You can either download a (large) CSV file with image links and meta-data of >10M generations, or access it through [our free API](https://devapi.krea.ai) (still in development).

Everyone is welcome to <a href=#contributing>contribute</a> with their own prompts, and [ideas](https://discord.gg/K8anVEWbQC).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

# About

AI models like Stable Diffusion, DALL-E, or Midjourney, are capable of creating stunning images from text descriptions. They provide us with freedom to produce an image of almost anything we can imagine.

Platforms like Lexica, OpenArt, and Krea.ai let us explore millions of AI generated images—as well as the prompts that produced them. They help you see what words work for generating certain styles and to assess how each AI model interprets different concepts.

We are just starting to explore the possibilities of text-to-image models, and we do not necessarily need to re-train them to dramatically improve their results; we can also learn how to prompt them effectively.

We hope this repository serves anyone who wants to analyze large datasets of prompts, create datasets to train new models, or build tools that help people create better prompts.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Data

There are three main data sources that you can use.

1. **Prompts API**. We released a (experimental) REST-based API that you can query to find and paginate through prompts—and its generations.

1. **CSV dataset**. This is a large CSV file that contains more than 10 million generations extracted from the Stability AI Discord during the beta testing of Stable Diffusion v1.3.

1. **This repository**. This repository contains a small but structured set of data that we created for the category section of [krea.ai](https://www.krea.ai). Anyone can <a href="#contributing">contribute</a>.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Prompts API

You can get query data from the dataset using our (experimental) [Prompts API](https://devapi.krea.ai).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## CSV file

To download the dataset click [this link]() or execute the following `wget` command:

```bash

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1c4WHxtlzvHYd0UY5WCMJNn2EO-Aiv2A0' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1c4WHxtlzvHYd0UY5WCMJNn2EO-Aiv2A0" -O openprompts.csv && rm /tmp/cookies.txt

# See: https://stackoverflow.com/a/39087286/10391569
```

### Structure of the dataset

The CSV file has a simple and raw structure. We may publish parsing scripts in the future, but we are focused on building more features for [krea.ai](https://www.krea.ai) for now. If you know Python, we would love to feature your parsing scripts here. To do so, simply [fork the repo and submit a PR](https://github.com/krea-ai/open-prompts/fork).

### How was the dataset made?

This dataset was created using a crawler and one-time use parsing scripts that mixed our own crawled generations with the [dataset](https://github.com/paperdave/stable-diffusion-sqlite) published by [paperdave](https://github.com/paperdave/) (thanks Dave!).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## In-repository dataset

This dataset started as a manual work that we conducted to create the modifiers in [krea.ai](https://www.krea.ai).

It is smaller than the previous dataset, but it is simpler as well. It is just plain-text files that
anyone can edit.

We want the best prompt engineers out there to grow it for the benefit of everyone else. For now the instructions for contributing can be found <a href="#contributing">here</a>, but in the future we will look for a cleaner way to upload prompts to this dataset—ideally including images too!

This dataset differentiates between two different kinds of elements: _modifiers_ and _presets_.

### Modifiers

Modifiers are those parts of a text prompt that contain the stylistic information of it. For example, if we want a prompt to look like a 3D render, we could use `octane render`, `unreal engine`, or `ray tracing` to enhance the style of our generations.

Modifiers can be very variate, from very precise colors and shapes to very abstract concepts and emotions—some people even find it useful to use emojis! The following is a tree representation of how we have organized the modifiers in this project:

```
├── README.md
├── modifiers
│   ├── modifier-category-1
│   │   ├── modifier-subcategory-1.txt
│   │   ├── modifier-subcategory-2.txt
│   │   ├── ...
│   ├── modifier-category-2
│   │   ├── ...
│   ├── ...
...
```

All the modifiers can be found within the folder `modifiers`, and they are organized within sub-categories that at its time belong to a parent category. Each of the subfolders within `modifiers` represents a different category—and the name of each subfolder specifies the name of each category. Sub-categories are represented within `txt` files where their name represent the name of the sub-category, and they contain a different modifier in each row.

The following is an example of how the subcategory `3D` from the category `digital art` could look like:

```
artstation
renderman
octane render
3d render
high quality 3d render
```

Note that each line represents a SINGLE modifier, and that there is nothing else in the file, just modifiers separated by lines.

### Presets

Presets are sets of modifiers that work well when used together and they normally share similarities. Organizing sets of modifiers within presets can come handy for speeding up the creation of prompts. For example, if we know that `greg rutkowski` creates amazing 3D art, we will probably find ourselves combining it all the time with modifiers such as `unreal engine`, `3D`, `artstation` and even with other similar artists like `wlop`.

The following is a tree representation of how we have organized the presets in this project:

```
├── README.md
├── presets
│   ├── preset-author
│   │   ├── preset-title-1.txt
│   │   ├── preset-title-2.txt
│   │   ├── ...
│   ├── preset-author-2
│   │   ├── ...
│   ├── ...
...
```

All the presets can be found within a folder within `presets`. Each of these folders will contain the name of the author that created each preset. Inside these folders, each preset is created in a different `txt` file. Each file contains a different modifier in each row.

The following is an example of how the subcategory `glossy tubes` from the category `krea` could look like:

```
glossy translucent glass with abstract tubular shapes
psychedelic texture
colors range between pastel blue and pastel pink
highly intricate
hyper detailed render
caspar david friedrich
ArtStation HD
```

We found that using all these modifiers combined works particularly well.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Contributing

for now, feel free to create a `txt` file containing modifiers or presets with the correct <a href="Modifiers">structure</a> and send it to `v@krea.ai`, we'll make sure to add it to the repository asap :)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Create your own CLIP Search Engine with _Open Prompts_

In our [https://github.com/krea-ai/clip-search](clip-search) repository you will find everything you need to create a semantic search engine with CLIP.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- CONTACT -->

# Get in Touch

- Follow and DM us on Twitter: [@krea_ai](https://twitter.com/krea_ai)
- Join [our Discord community](https://discord.gg/3mkFbvPYut)
- Email either `v` or `d` (`v` at `krea` dot `ai`; `d` at `krea` dot `ai` respectively)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Contributors

#### [@blademort](https://twitter.com/blademort)

**art**: `art movements`, `art styles`, and `descriptive terms`

**general**: `design tools and communities`, and `genres`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[twiter-shield]: https://img.shields.io/badge/-Twitter-black.svg?style=for-the-badge&logo=twitter&colorB=111
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: static/screenshot.png
[next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[next-url]: https://nextjs.org/
[react.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[react-url]: https://reactjs.org/
[vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[vue-url]: https://vuejs.org/
[angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[angular-url]: https://angular.io/
[svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[svelte-url]: https://svelte.dev/
[laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[laravel-url]: https://laravel.com
[bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[bootstrap-url]: https://getbootstrap.com
[jquery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[jquery-url]: https://jquery.com
