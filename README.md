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
  <a href="https://github.com/github_username/repo_name">
    <img src="static/krea.gif" alt="Logo" width="auto" height="200">
  </a>

<h3 align="center">the prompt repository</h3>

  <p align="center">
    an open knowledge base of prompts powered by krea.ai
    <br />
    <a href="https://krea.ai"><strong>explore prompts</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name/issues">newsletter</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">community</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<!-- <details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details> -->



<!-- ABOUT THE PROJECT -->
## ✨ about

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

with the right spark, we humans are infinite sources of creativity.

*the prompt repository* democratizes a wide variety of creative knowledge to serve as an inspiration when using text-to-image AI models.

this is an open knowledge base made by the AI Art community and powered by krea.ai.

you can <a hred=#contribute>contribute</a> with your own prompts, they will be accessible for anyone and for free [here](https://krea.ai).


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## 🧑‍🎨 getting started

### prompts and AI
AI is extending the creative possibilities of language to the realm of visual arts.

today, a few words is all we need to express our ideas visually through an image.

models like DALL-E, Stable Diffusion, or Midjourney, are capable of creating almost any image we can imagine if we are able to find the right combination of words for them to understand our purpose.

the art of optimizing the inputs we feed into an AI model to generate content that is in alignment with our purpose is known as *prompting* or *prompt engineering*.

a good *prompter* will be able to guide a text-to-image AI model with prompts that produce images that accurately represent their visual ideas.

### the needs of a *prompter*
#### sparks of inspiration
since language is something that most of us master since a young age, being good at the emerging skill of *prompting* is very related on how creative and original we can get at imagining a text prompt.

creativity is inherently related with the combination of dispar ideas in ways that we never imagined before.

indeed, half of the work in creative jobs consists of searching for ideas to merge together and create something new.

that is why open Discords like Midjourney's have worked so well with text-to-image AI models, people get a lot of value and ideas from other's generations.

#### visual domain knowledge
there are many ways to express an idea through text, and there are words that can convey ideas extremelly well.

that's why a good vocabulary is something helpful for expressing ourselves to text and the reason why dictionaries are so handy.

something similar happens with *prompting*.

a simple word can convey an insane amount of information about how our final image should look like, from specific kinds of lighting to artistic mediums or composition.

for example, the word "Dali" will serve us to describe an image that looks like a surrealist painting with abstract shapes and bizarre elements.

hence, a good visual domain knowledge is key for *prompt engineering*, knowing about different artistic styles, 3D renderers, or photography, enables us to have a wider vocabulary that we can use to communicate our ideas more effectively with the AI.

### the prompt repository
with this project we provide *prompters* with a source of inspiration and of visual domain knowledge.

on the one side, the prompts from our knowledge are continuously updated by a community of AI enthusiasts that <a href=#contribute>contribute</a> with their creative ideas, so there are always new ideas to check out.

plus, at [krea.ai](https://krea.ai), it is possible to visualize all this prompts, giving extra room for inspiration and surprises.

on the other hand, the knowledge is organized in a way that makes it easy to browse and learn about different artists and concepts while exploring prompts.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

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
contributions are at the core of this project.

we made it really simple to contribute:
1. open
2. something
3. add txt
4. close
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
## 📞 contact

vicc - [@viccpoes](https://twitter.com/viccpoes) - v@krea.ai

diego - [@asciidiego](https://twitter.com/asciidiego) - d@krea.ai


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



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