from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from datetime import date

# Create your views here.
posts_data = [
    {
        "slug": "project-development-1",
        "image": "some_picture.png",
        "author": "Anna Szyszkowska, Msc",
        "author_image": "hero__image.png",
        "date": date(2021, 1, 1),
        "title": "BLog post 1",
        "excerpt": "some text 1",
        "content": "Cumque ut harum reprehenderit libero? Quo ratione perferendis ipsum necessitatibus! Explicabo cupiditate illo vero esse quaerat similique itaque nemo laudantium harum atque. Ex reprehenderit facilis ea laborum sint eum ad provident perspiciatis, impedit delectus animi. Explicabo, error? Voluptatum delectus sapiente cumque neque unde ea impedit optio repellendus, sit quisquam aliquam ratione deleniti. Doloribus eveniet, unde recusandae aspernatur voluptatum modi eaque facere eos soluta labore dolorem suscipit maiores nihil natus neque totam non iure, ab molestiae adipisci! Commodi numquam facilis eveniet velit iste! Ex commodi praesentium quibusdam fuga delectus odio quam tenetur, officia blanditiis quod ad, odit obcaecati et pariatur. Delectus dicta veniam culpa repudiandae modi consectetur voluptatibus eveniet, non, at eaque molestiae. Tenetur error laboriosam alias quo sapiente fugiat placeat repellendus ducimus iusto dolore ullam ex, commodi aspernatur. Vero unde, voluptatibus amet facere sed ipsa ad cupiditate expedita eligendi animi eveniet repudiandae. Necessitatibus minus, voluptate iusto expedita neque cumque recusandae in deserunt ad veritatis. Impedit maiores necessitatibus odit laborum facere quam modi, repellat esse sint ratione fuga, non saepe perferendis fugiat iste? Excepturi magnam odio eum eius harum corporis! Quae similique corporis optio, modi eum nemo veniam esse quo omnis ad exercitationem, ut iusto quasi vel magni accusamus adipisci saepe voluptates ipsam! Nemo, architecto, obcaecati explicabo molestias quaerat reprehenderit corporis nisi illum repellendus facilis harum voluptatum, tempora ex sint nobis illo exercitationem eum? Animi, error a non delectus ad aperiam laudantium nam! Eveniet alias enim quo quidem, in similique ab! Velit minima delectus ducimus sapiente reprehenderit esse nobis reiciendis maiores, non suscipit ratione. Quisquam reiciendis unde quos dolorem fac",
    },
    {
        "slug": "project-development-2",
        "image": "some_picture.png",
        "author": "Anna Szyszkowska, Msc",
        "author_image": "hero__image.png",
        "date": date(2021, 2, 1),
        "title": "Blog post 2",
        "excerpt": "some text 2",
        "content": "Quo ratione perferendis ipsum necessitatibus! Explicabo cupiditate illo vero esse quaerat similique itaque nemo laudantium harum atque. Ex reprehenderit facilis ea laborum sint eum ad provident perspiciatis, impedit delectus animi. Explicabo, error? Voluptatum delectus sapiente cumque neque unde ea impedit optio repellendus, sit quisquam aliquam ratione deleniti. Doloribus eveniet, unde recusandae aspernatur voluptatum modi eaque facere eos soluta labore dolorem suscipit maiores nihil natus neque totam non iure, ab molestiae adipisci! Commodi numquam facilis eveniet velit iste! Ex commodi praesentium quibusdam fuga delectus odio quam tenetur, officia blanditiis quod ad, odit obcaecati et pariatur. Delectus dicta veniam culpa repudiandae modi consectetur voluptatibus eveniet, non, at eaque molestiae. Tenetur error laboriosam alias quo sapiente fugiat placeat repellendus ducimus iusto dolore ullam ex, commodi aspernatur. Vero unde, voluptatibus amet facere sed ipsa ad cupiditate expedita eligendi animi eveniet repudiandae. Necessitatibus minus, voluptate iusto expedita neque cumque recusandae in deserunt ad veritatis. Impedit maiores necessitatibus odit laborum facere quam modi, repellat esse sint ratione fuga, non saepe perferendis fugiat iste? Excepturi magnam odio eum eius harum corporis! Quae similique corporis optio, modi eum nemo veniam esse quo omnis ad exercitationem, ut iusto quasi vel magni accusamus adipisci saepe voluptates ipsam! Nemo, architecto, obcaecati explicabo molestias quaerat reprehenderit corporis nisi illum repellendus facilis harum voluptatum, tempora ex sint nobis illo exercitationem eum? Animi, error a non delectus ad aperiam laudantium nam! Eveniet alias enim quo quidem, in similique ab! Velit minima delectus ducimus sapiente reprehenderit esse nobis reiciendis maiores, non suscipit ratione. Quisquam reiciendis unde quos dolorem fac",
    },
    {
        "slug": "project-development-3",
        "image": "some_picture.png",
        "author": "Anna Szyszkowska, Msc",
        "author_image": "hero__image.png",
        "date": date(2021, 3, 1),
        "title": "Blog post 3",
        "excerpt": "some text 3",
        "content": "Quisquam reiciendis unde quos dolorem fac",
    },
    {
        "slug": "project-development-4",
        "image": "some_picture.png",
        "author": "Anna Szyszkowska, Msc",
        "author_image": "hero__image.png",
        "date": date(2021, 4, 1),
        "title": "Blog post 4",
        "excerpt": "some text 4",
        "content": "Lorem ipsum dolor sit amet consectetadipisicing elit. Cumque ut harum reprehenderit libero? Quo ratione perferendis ipsum necessitatibus! Explicabo cupiditate illo vero esse quaerat similique itaque nemo laudantium harum atque. Ex reprehenderit facilis ea laborum sint eum ad provident perspiciatis, impedit delectus animi. Explicabo, error? Voluptatum delectus sapiente cumque neque unde ea impedit optio repellendus, sit quisquam aliquam ratione deleniti. Doloribus eveniet, unde recusandae aspernatur voluptatum modi eaque facere eos soluta labore dolorem suscipit maiores nihil natus neque totam non iure, ab molestiae adipisci! Commodi numquam facilis eveniet velit iste! Ex commodi praesentium quibusdam fuga delectus odio quam tenetur, officia blanditiis quod ad, odit obcaecati et pariatur. Delectus dicta veniam culpa repudiandae modi consectetur voluptatibus eveniet, non, at eaque molestiae. Tenetur error laboriosam alias quo sapiente fugiat placeat repellendus ducimus iusto dolore ullam ex, commodi aspernatur. Vero unde, voluptatibus amet facere sed ipsa ad cupiditate expedita eligendi animi eveniet repudiandae. Necessitatibus minus, voluptate iusto expedita neque cumque recusandae in deserunt ad veritatis. Impedit maiores necessitatibus odit laborum facere quam modi, repellat esse sint ratione fuga, non saepe perferendis fugiat iste? Excepturi magnam odio eum eius harum corporis! Quae similique corporis optio, modi eum nemo veniam esse quo omnis ad exercitationem, ut iusto quasi vel magni accusamus adipisci saepe voluptates ipsam! Nemo, architecto, obcaecati explicabo molestias quaerat reprehenderit corporis nisi illum repellendus facilis harum voluptatum, tempora ex sint nobis illo exercitationem eum? Animi, error a non delectus ad aperiam laudantium nam! Eveniet alias enim quo quidem, in similique ab! Velit minima delectus ducimus sapiente reprehenderit esse nobis reiciendis maiores, non suscipit ratione. Quisquam reiciendis unde quos dolorem fac",
    },
]


def get_date(post: dict[str, date]) -> date:
    return post.get("date")


def index(request: HttpRequest) -> HttpResponse:
    """Entrypoint for index page."""
    sorted_posts = sorted(posts_data, key=get_date, reverse=True)
    latest_posts = sorted_posts[:3]
    return render(request, "blog/index.html", {"latest_posts": latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    """Entrypoint for all posts page."""
    return render(request, "blog/posts.html", {"posts": posts_data})


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    """Entrypoint for detail post page page."""
    current_post = next(filter(lambda post: post.get("slug") == slug, posts_data))
    return render(request, "blog/post-detail.html", {"post": current_post})
