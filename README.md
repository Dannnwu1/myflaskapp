This is a web app build with flask bootstrap 
myapp/
├── app.py
├── config.py
├── blueprints/
│   ├── __init__.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── blog/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── templates/
│   │       └── blog/
│   │           ├── index.html
│   │           └── post.html
│   └── admin/
│       ├── __init__.py
│       ├── routes.py
│       └── templates/
│           └── admin/
│               └── dashboard.html
├── static/
└── templates/
    └── base.html