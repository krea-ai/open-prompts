<a name="readme-top"></a>

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/krea_ai/open-prompts">
    <img src="static/krea.gif" alt="Logo" width="auto" height="200">
  </a>

<h3 align="center">open prompts</h3>

  <p align="center">
    data, utilities and APIs for prompting.
    <br />
    <a href="https://krea.ai"><strong>explore prompts</strong></a>
    <br />
    <br />
    <a href="https://theprompter.substack.com/">newsletter</a>
    ·
    <a href="https://discord.gg/3mkFbvPYut">community</a>
    ·
    <a href="#-contributing">contribute</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## ✨ About

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->


Open Prompts is currently a collection of the data, utilities, and APIs that we used to build [krea.ai](kre.ai). We hope this repository can useful to build tools that help people create better prompts. You are welcome to <a href=#-contributing>contribute</a> with your own prompts, implementations, and ideas.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## 📖 Background
AI models like Stable Diffusion, DALL-E, or Midjourney, are capable of creating stunning images from text descriptions. They provide creatives with freedom to produce an image of almost anything they can imagine.

Although some artists can get already get value from randomly throwing ideas to these models, creating a prompt can be a challenging creative exercise; visual domain knowledge is necessary to describe ideas accurately as well as a sense of how each model understands different concepts. A single word can convey lots of visual information about how an image should look like—from specific lightings to artistic styles, mediums or compositions—and each model will interpret it differently.

Platforms like Lexica, OpenArt, and Krea let creatives explore millions of prompts and the images they produced. They are helpful to see what words worked for generating certain styles and to assess how the AI model interprets different concepts.

We are just starting to explore the possibilities of text-to-image models. The interesting news is that we do not necessarily need to re-train them to produce better results. There is plenty of room for improvement by getting a better understanding about how they encode knowledge. 

We hope this repository serves to conduct studies, explorations, or to build tools that help people create better prompts.


## open prompts
with this project we provide *prompters* with a source of inspiration and of visual domain knowledge.

on the one side, the prompts from our knowledge base are continuously updated by a community of AI enthusiasts that <a href=#-contributing>contribute</a> with their creative ideas, so there are always new ideas to check out.

plus, at [krea.ai](https://krea.ai), it is possible to visualize all this prompts, giving extra room for inspiration and surprises.

on the other hand, the knowledge is organized in a way that makes it easy to browse and learn about different artists and concepts while exploring prompts.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 🏛️ structure of the repository
right now there exist two different kinds of elements that can be added to the repository: *modifiers* and *presets*.

### modifiers
modifiers are those parts of a text prompt that contain the stylistic information of it.

for example, if we want a prompt to look like a 3D render, we could use `octane render`, `unreal engine`, or `ray tracing` to enhance the style of our generations.

modifiers can be very variate, from very precise colors and shapes to very abstract concepts and emotions—some people even find it useful to use emojis!

the following is a tree representation of how we have organized the modifiers in this project:

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

all the modifiers can be found within the folder `modifiers`.

modifiers are organized within sub-categories that at its time belong to a parent category.

each of the subfolders within `modifiers` represents a different category of modifiers—and the name of each subfolder specifies the name of each category.

modifier subcategory files are plain `txt` that contain a different modifier in each row. 

the following is an example of how the subcategory `3D` from the category `digital art` could look like:
```
artstation
renderman
octane render
3d render
high quality 3d render
```

### presets
presets are sets of modifiers that work well when used together and they normally share similarities.

organizing sets of modifiers within presets is very handy for speeding up the creation of prompts. 

if we know that `greg rutkowski` creates amazing 3D art, we will probably find ourselves combining it all the time with modifiers such as `unreal engine`, `3D`, `artstation` and even with other similar artists like `wlop`.

the following is a tree representation of how we have organized the presets in this project:

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

all the presets can be found within the folder `presets`.

modifiers are organized within depending on their author. 

this author can be a single person or a group of people working together. 

each author folder contains all the presets that it has created.

each preset file is a plain `txt` that contain a different modifier in each row. 

the following is an example of how the subcategory `glossy tubes` from the category `krea` could look like:
```
glossy translucent glass with abstract tubular shapes
psychedelic texture
colors range between pastel blue and pastel pink
highly intricate
hyper detailed render
caspar david friedrich
ArtStation HD
```

<!-- ROADMAP -->
<!-- ## Roadmap -->

<!-- - [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
## 📝 contributing

for now, feel free to create a `txt` file containing modifiers or presets with the correct <a href="#%EF%B8%8F-structure-of-the-repository">structure</a> and send it to `v@krea.ai`, we'll make sure to add it to the repository asap :)


<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

### contributors
#### [@blademort](https://twitter.com/blademort)
**art**: `art movements`, `art styles`, and `descriptive terms`

**general**: `design tools and communities`, and `genres`


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## 📞 contact

[@krea_ai](https://twitter.com/krea_ai) - `v@krea.ai` - <a href="https://discord.gg/3mkFbvPYut">krea discord</a>



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
[twiter-shield]: https://img.shields.io/badge/-Twitter-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: static/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 