# Relating Diagrams to the API

- The `/users` endpoint is implemented in the `UserViewSet` view, which interacts with the `User` model.
- The `/posts` endpoint is handled by the `PostViewSet`, which connects the `Post` model to the `User` model via a foreign key.
