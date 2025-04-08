# Product Review Platform

A web application built with Django that allows users to submit and browse reviews for a wide variety of products. This platform was designed to be simple, modern, and responsive, with a focus on user experience and clean UI.

## 🚀 Features

- ✅ Product registration form with image upload
- ✅ Automatic image resizing and thumbnail generation
- ✅ Product list with detailed modal view
- ✅ Search functionality for filtering products
- ✅ Responsive dark-themed UI using Tailwind CSS
- ✅ Default placeholder image for products without images
- ✅ Modal popups for quick product info
- ✅ Footer with developer contact and GitHub link
- ✅ Future section with "About us", "What you can do", and "Upcoming improvements"

## 🛠️ Technologies Used

- **Python 3.13**
- **Django 5.1**
- **Tailwind CSS** (CDN)
- **Bootstrap 4**
- **HTML5**
- **JavaScript (Bootstrap Modal)**
- **Pillow** for image processing
- **django-widget-tweaks** for better form rendering
- **StdImageField** for image variations and processing

## 🖼️ Image Handling

Images uploaded by users are resized to standard dimensions (`150x150`) and optimized for better performance. The application also ensures that if no image is provided, a default placeholder is used.

## 📁 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
