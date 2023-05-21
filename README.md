# DRF CMS Project

This repository contains a Django CMS project built with Django Rest Framework (DRF). It provides a backend API for managing blog posts, comments, users, tags, and categories.

## Features

- User management: Create, update, and delete users. Only superusers have access to user details.
- Blog post management: Create, update, delete, and view blog posts. Posts can be categorized and tagged.
- Comment system: Users can add comments to blog posts and reply to existing comments.
- Authentication and authorization: Token-based authentication is used to secure the API endpoints. Only authenticated users can perform certain actions.
- API endpoints: The project provides a set of API endpoints for performing CRUD operations on users, posts, comments, tags, and categories.

## Requirements

- Python 3.x
- Django 4.2.1
- Django Rest Framework (DRF)
- SQLite (default database)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/drf-cms-project.git
   ```

2. Navigate to the project directory:

   ```shell
   cd drf-cms-project
   ```

3. Create a virtual environment (optional):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Run database migrations:

   ```shell
   python manage.py migrate
   ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. The API will be accessible at `http://localhost:8000`.

## API Endpoints

The following API endpoints are available:

- `GET /users/`: Get a list of all users (superuser only).
- `POST /users/`: Create a new user (superuser only).
- `GET /users/{username}/`: Get details of a specific user (superuser only).
- `PUT /users/{username}/`: Update details of a specific user (superuser only).
- `DELETE /users/{username}/`: Delete a specific user (superuser only).

- `GET /posts/`: Get a list of all blog posts.
- `POST /posts/`: Create a new blog post.
- `GET /posts/{slug}/`: Get details of a specific blog post.
- `PUT /posts/{slug}/`: Update details of a specific blog post.
- `DELETE /posts/{slug}/`: Delete a specific blog post.

- `GET /posts/{slug}/comments/`: Get a list of comments for a specific blog post.
- `POST /posts/{slug}/comments/`: Add a new comment to a specific blog post.
- `GET /posts/{slug}/comments/{pk}/`: Get details of a specific comment.
- `PUT /posts/{slug}/comments/{pk}/`: Update details of a specific comment (superuser only).
- `DELETE /posts/{slug}/comments/{pk}/`: Delete a specific comment (superuser only).

For authentication and registration endpoints, please refer to the [dj-rest-auth documentation](https://dj-rest-auth.readthedocs.io/).


## Contributing

Contributions are welcome! If you find any issues or want to add new features, please submit a pull request or open an issue.

## Credits

This project was developed by [Mobin Zamanzadeh](https://github.com/mobinzamanzadeh).

## Contact

If you have any questions or suggestions, feel free to
