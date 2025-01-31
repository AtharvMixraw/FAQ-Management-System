"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Home route
def home_view(request):
    from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse

def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FAQ API Documentation</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .container {
                max-width: 800px;
                margin: 2rem auto;
                padding: 2rem;
                background: white;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 2rem;
            }
            .endpoint-list {
                background: #f8f9fa;
                padding: 1.5rem;
                border-radius: 5px;
                margin-bottom: 1.5rem;
            }
            .endpoint {
                margin-bottom: 1rem;
                padding-bottom: 1rem;
                border-bottom: 1px solid #e9ecef;
            }
            .endpoint:last-child {
                border-bottom: none;
                margin-bottom: 0;
                padding-bottom: 0;
            }
            .method {
                display: inline-block;
                padding: 0.25rem 0.5rem;
                background: #4CAF50;
                color: white;
                border-radius: 3px;
                font-size: 0.9rem;
                margin-right: 0.5rem;
            }
            .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 2rem 0;
        color: #6c757d;
        border-top: 1px solid #e9ecef;
    }
    .social-links {
        margin-top: 1rem;
        display: flex;
        justify-content: center;
        gap: 1.5rem;
    }
    .social-links a {
        color: #6c757d;
        text-decoration: none;
        transition: color 0.3s ease;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .social-links a:hover {
        color: #2c3e50;
    }
    .creator-info {
        font-size: 1.1rem;
        color: #4a5568;
        margin-bottom: 1rem;
    }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📚 Welcome to the FAQ API</h1>
            
            <div class="endpoint-list">
                <h2>Available Endpoints</h2>
                <div class="endpoint">
                    <span class="method">GET</span>
                    <code>/api/faqs/</code>
                    <p>Retrieve all FAQ entries</p>
                </div>
                <div class="endpoint">
                    <span class="method">POST</span>
                    <code>/admin/</code>
                    <p>Create a new FAQ entry</p>
                </div>
                <!-- Add more endpoints as needed -->
            </div>

            <div class="footer">
    <p>API Version 1.0</p>
    <p>Built with Django Rest Framework</p>
    <p class="creator-info">Made by Atharv, for BharatFD task</p>
    <div class="social-links">
        <a href="https://github.com/AtharvMixraw" target="_blank" rel="noopener noreferrer">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            GitHub
        </a>
        <a href="https://www.linkedin.com/in/atharv-mishra-077b0a253/" target="_blank" rel="noopener noreferrer">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
            </svg>
            LinkedIn
        </a>
        <a href="https://x.com/AtharvMixraw" target="_blank" rel="noopener noreferrer">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
            </svg>
            X (Twitter)
        </a>
    </div>
</div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
urlpatterns = [
    path("", home_view, name="home"),  # Home route for "/"
    path("admin/", admin.site.urls),
    path("api/", include("faq_project.urls")),  # Include API URLs
]

