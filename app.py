from flask import Flask, render_template_string
import base64
import os

app = Flask(__name__)

def get_profile_image():
    """Load profile image and convert to base64"""
    try:
        # Try to find the image file (png or jpg)
        image_files = ['profile.png', 'profile.jpg', 'profile.jpeg']
        for img_file in image_files:
            if os.path.exists(img_file):
                with open(img_file, 'rb') as f:
                    encoded = base64.b64encode(f.read()).decode('utf-8')
                    # Determine the correct MIME type
                    if img_file.endswith('.png'):
                        return f"data:image/png;base64,{encoded}"
                    else:
                        return f"data:image/jpeg;base64,{encoded}"
        # If no image found, return empty string
        return ""
    except Exception as e:
        print(f"Error loading image: {e}")
        return ""
def get_icon_image():
    """Load profile image and convert to base64"""
    try:
        # Try to find the image file (png or jpg)
        image_files = ['icon.png', 'profile.jpg', 'profile.jpeg']
        for img_file in image_files:
            if os.path.exists(img_file):
                with open(img_file, 'rb') as f:
                    encoded = base64.b64encode(f.read()).decode('utf-8')
                    # Determine the correct MIME type
                    if img_file.endswith('.png'):
                        return f"data:image/png;base64,{encoded}"
                    else:
                        return f"data:image/jpeg;base64,{encoded}"
        # If no image found, return empty string
        return ""
    except Exception as e:
        print(f"Error loading image: {e}")
        return ""

@app.route('/')
def index():
    profile_image = get_profile_image()
    icon = get_icon_image()
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Abdullah Kabir - DevOps Consultant & Data Scientist</title>
        <link rel="icon" type="image/x-icon" href="{{ icon }}">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
        <style>
            :root {
                --primary-color: #0066cc;
                --secondary-color: #004c99;
                --accent-color: #3399ff;
                --text-dark: #1a1a1a;
                --text-light: #666666;
                --bg-light: #f8f9fa;
                --bg-white: #ffffff;
                --border-color: #e0e0e0;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                overflow-x: hidden;
                color: var(--text-dark);
            }
            
            /* Smooth scroll */
            html {
                scroll-behavior: smooth;
            }
            
            /* Fade in animation */
            .fade-in {
                animation: fadeIn 0.8s ease-in;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            /* Slide in from left */
            .slide-in-left {
                animation: slideInLeft 0.8s ease-out;
            }
            
            @keyframes slideInLeft {
                from { opacity: 0; transform: translateX(-50px); }
                to { opacity: 1; transform: translateX(0); }
            }
            
            /* Slide in from right */
            .slide-in-right {
                animation: slideInRight 0.8s ease-out;
            }
            
            @keyframes slideInRight {
                from { opacity: 0; transform: translateX(50px); }
                to { opacity: 1; transform: translateX(0); }
            }
            
            /* Card hover effect */
            .card-hover {
                transition: all 0.3s ease;
                border: 1px solid var(--border-color);
            }
            
            .card-hover:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 20px rgba(0, 102, 204, 0.1) !important;
                border-color: var(--primary-color);
            }
            
            /* Profile image animation */
            .profile-img {
                transition: all 0.4s ease;
                border: 5px solid white;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            
            .profile-img:hover {
                transform: scale(1.05);
                box-shadow: 0 15px 40px rgba(0, 102, 204, 0.2);
            }
            
            /* Navbar enhancement */
            .navbar {
                background-color: white !important;
            }
            
            .navbar-brand {
                font-size: 1.5rem;
                font-weight: 700;
                color: var(--primary-color) !important;
            }
            
            .nav-link {
                color: var(--text-dark) !important;
                font-weight: 500;
                transition: color 0.3s ease;
            }
            
            .nav-link:hover {
                color: var(--primary-color) !important;
            }
            
            /* Button animations */
            .btn {
                transition: all 0.3s ease;
                font-weight: 500;
            }
            
            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0, 102, 204, 0.3);
            }
            
            .btn-primary {
                background-color: var(--primary-color);
                border-color: var(--primary-color);
            }
            
            .btn-primary:hover {
                background-color: var(--secondary-color);
                border-color: var(--secondary-color);
            }
            
            .btn-outline-primary {
                color: var(--primary-color);
                border-color: var(--primary-color);
            }
            
            .btn-outline-primary:hover {
                background-color: var(--primary-color);
                border-color: var(--primary-color);
            }
            
            /* Skill badge animation */
            .badge {
                transition: all 0.3s ease;
                cursor: default;
                font-weight: 500;
                padding: 0.5rem 1rem;
            }
            
            .badge:hover {
                transform: scale(1.05);
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            }
            
            /* Section title underline animation */
            .section-title {
                position: relative;
                display: inline-block;
                padding-bottom: 15px;
                color: var(--text-dark);
            }
            
            .section-title::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 0;
                height: 3px;
                background: var(--primary-color);
                transition: width 0.6s ease;
                border-radius: 2px;
            }
            
            .section-title.animate::after {
                width: 60px;
            }
            
            /* Stats counter animation */
            .stat-number {
                font-size: 2rem;
                font-weight: 700;
                color: var(--primary-color);
            }
            
            /* Icon pulse animation */
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.1); }
            }
            
            .icon-pulse:hover {
                animation: pulse 0.8s ease-in-out;
            }
            
            /* Scroll reveal */
            .scroll-reveal {
                opacity: 0;
                transform: translateY(30px);
                transition: all 0.6s ease;
            }
            
            .scroll-reveal.active {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* Custom badge colors */
            .badge-blue {
                background-color: #0066cc;
                color: white;
            }
            
            .badge-green {
                background-color: #28a745;
                color: white;
            }
            
            .badge-purple {
                background-color: #6f42c1;
                color: white;
            }
            
            .badge-orange {
                background-color: #fd7e14;
                color: white;
            }
            
            .badge-teal {
                background-color: #20c997;
                color: white;
            }
            
            .badge-gray {
                background-color: #6c757d;
                color: white;
            }
            
            /* Hero section styling */
            .hero-section {
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            }
            
            /* Contact section */
            .contact-section {
                background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            }
            
            .contact-icon {
                transition: transform 0.3s ease;
            }
            
            .contact-icon:hover {
                transform: translateY(-5px);
            }
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-light sticky-top">
            <div class="container">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="#experience">Experience</a></li>
                        <li class="nav-item"><a class="nav-link" href="#skills">Skills</a></li>
                        <li class="nav-item"><a class="nav-link" href="#education">Education</a></li>
                        <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="py-5">
            <div class="container">
                <div class="row align-items-center py-5">
                    <div class="col-lg-4 text-center mb-4 mb-lg-0 slide-in-left">
                        {% if profile_image %}
                        <img src="{{ profile_image }}" alt="Abdullah Kabir" class="mb-3" style="max-width: 280px; width: 100%;">
                        {% else %}
                        <div class="rounded-circle bg-secondary d-flex align-items-center justify-content-center mx-auto shadow-lg mb-3" style="width: 280px; height: 280px;">
                            <i class="bi bi-person-circle text-white" style="font-size: 150px;"></i>
                        </div>
                        {% endif %}
                    </div>
                    <div class="col-lg-8 slide-in-right">
                        <h1 class="display-4 fw-bold mb-3 text-dark">Abdullah Kabir</h1>
                        <h3 class="text-primary mb-3">DevOps Consultant</h3>
                        <h5 class="text-muted mb-4">Bechtle GmbH | Darmstadt, Germany</h5>
                        <p class="lead text-secondary mb-4">M.Sc. in Web and Data Science | B.Sc. in Computer Science & Engineering</p>
                        <p class="lead text-secondary mb-4">Enterprise Automation Specialist | Machine Learning & AI Researcher</p>
                        <div class="d-flex gap-3 flex-wrap">
                            <a href="https://www.linkedin.com/in/abdullahkabir" class="btn btn-primary btn-lg" target="_blank">
                                <i class="bi bi-linkedin me-2"></i>LinkedIn
                            </a>
                            <a href="mailto:abdullah.kabir12@gmail.com" class="btn btn-outline-primary btn-lg">
                                <i class="bi bi-envelope me-2"></i>Contact Me
                            </a>
                            <a href="tel:+4915750709337" class="btn btn-outline-secondary btn-lg">
                                <i class="bi bi-telephone me-2"></i>Call
                            </a>
                        </div>
                    </div>
                    
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section id="about" class="py-5 bg-white">
            <div class="container">
                <h2 class="display-6 fw-bold mb-4 text-center section-title">Professional Summary</h2>
                <div class="row justify-content-center scroll-reveal">
                    <div class="col-lg-10">
                        <div class="card border-0 shadow-sm card-hover">
                            <div class="card-body p-5">
                                <p class="fs-5 text-dark mb-4">DevOps Consultant with expertise in enterprise automation and network security. Completed Master's degree in Web and Data Science from Universität Koblenz, Germany, with demonstrated experience in Python-based automation solutions and strong background in Machine Learning and Data Mining research.</p>
                                <p class="fs-5 text-dark mb-4">Former Research and Teaching Assistant specializing in Machine Learning and Data Mining modules. Proven track record in full-stack development with proficiency in Java (Android), ReactJS, and Laravel frameworks.</p>
                                <div class="row mt-4">
                                    <div class="col-md-4 mb-3">
                                        <div class="d-flex align-items-center">
                                            <i class="bi bi-briefcase fs-3 text-primary me-3 icon-pulse"></i>
                                            <div>
                                                <h6 class="mb-0 fw-bold stat-number">3+</h6>
                                                <small class="text-muted">Years DevOps Experience</small>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-4 mb-3">
                                        <div class="d-flex align-items-center">
                                            <i class="bi bi-code-square fs-3 text-primary me-3 icon-pulse"></i>
                                            <div>
                                                <h6 class="mb-0 fw-bold stat-number">6+</h6>
                                                <small class="text-muted">Years Development</small>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-4 mb-3">
                                        <div class="d-flex align-items-center">
                                            <i class="bi bi-mortarboard fs-3 text-primary me-3 icon-pulse"></i>
                                            <div>
                                                <h6 class="mb-0 fw-bold stat-number">M.Sc.</h6>
                                                <small class="text-muted">Web & Data Science</small>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Experience Section -->
        <section id="experience" class="py-5 bg-light">
            <div class="container">
                <h2 class="display-6 fw-bold mb-5 text-center section-title">Professional Experience</h2>
                
                <div class="row mb-4 scroll-reveal">
                    <div class="col-md-12">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <div class="row">
                                    <div class="col-md-9">
                                        <h4 class="card-title mb-2 fw-bold">DevOps Consultant</h4>
                                        <h5 class="text-primary mb-2">Bechtle GmbH</h5>
                                        <p class="text-muted mb-3"><i class="bi bi-geo-alt me-2"></i>Darmstadt, Hesse, Germany</p>
                                    </div>
                                    <div class="col-md-3 text-md-end">
                                        <span class="badge bg-success px-3 py-2">July 2024 - Present</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row mb-4 scroll-reveal">
                    <div class="col-md-12">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <div class="row">
                                    <div class="col-md-9">
                                        <h4 class="card-title mb-2 fw-bold">Werkstudent in DevOps</h4>
                                        <h5 class="text-primary mb-2">Bechtle GmbH</h5>
                                        <p class="text-muted mb-2"><i class="bi bi-geo-alt me-2"></i>Darmstadt, Hesse, Germany</p>
                                        <p class="card-text mt-3">Specialized in Network and Security Department with focus on enterprise automation solutions using Python. Contributed to critical infrastructure projects and security implementations.</p>
                                    </div>
                                    <div class="col-md-3 text-md-end">
                                        <span class="badge bg-primary px-3 py-2">Jan 2023 - July 2024</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row mb-4">
                    <div class="col-md-12">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <div class="row">
                                    <div class="col-md-9">
                                        <h4 class="card-title mb-2 fw-bold">Research Assistant - Machine Learning & Data Mining</h4>
                                        <h5 class="text-primary mb-2">Universität Koblenz</h5>
                                        <p class="text-muted mb-2"><i class="bi bi-geo-alt me-2"></i>Koblenz, Rhineland-Palatinate, Germany</p>
                                        <p class="card-text mt-3">Research and teaching assistant for Machine Learning and Data Mining module during Winter semester 2022/23. Conducted research in AI applications and supported academic instruction.</p>
                                    </div>
                                    <div class="col-md-3 text-md-end">
                                        <span class="badge bg-primary px-3 py-2">Oct 2022 - May 2023</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row mb-4">
                    <div class="col-md-12">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <div class="row">
                                    <div class="col-md-9">
                                        <h4 class="card-title mb-2 fw-bold">Software Developer</h4>
                                        <h5 class="text-primary mb-2">AppHouseBD</h5>
                                        <p class="text-muted mb-2"><i class="bi bi-geo-alt me-2"></i>Bangladesh</p>
                                        <p class="card-text mt-3">Full-stack software development including Android application development using Java, and web application development utilizing ReactJS and Laravel frameworks. Delivered multiple client projects successfully.</p>
                                    </div>
                                    <div class="col-md-3 text-md-end">
                                        <span class="badge bg-primary px-3 py-2">Apr 2018 - Jan 2022</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row scroll-reveal">
                    <div class="col-md-12">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <div class="row">
                                    <div class="col-md-9">
                                        <h4 class="card-title mb-2 fw-bold">Web Developer</h4>
                                        <h5 class="text-primary mb-2">Russell IT & Engineering</h5>
                                        <p class="text-muted mb-2"><i class="bi bi-geo-alt me-2"></i>Dhaka, Bangladesh</p>
                                    </div>
                                    <div class="col-md-3 text-md-end">
                                        <span class="badge bg-secondary px-3 py-2">Apr 2016 - Oct 2016</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Skills Section -->
        <section id="skills" class="py-5">
            <div class="container">
                <h2 class="display-6 fw-bold mb-5 text-center section-title">Skills & Technologies</h2>
                
                <div class="row g-4">
                    <div class="col-md-4 scroll-reveal">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <h5 class="card-title mb-3"><i class="bi bi-code-slash text-primary me-2"></i>Programming Languages</h5>
                                <div class="d-flex flex-wrap gap-2">
                                    <span class="badge badge-blue">Python</span>
                                    <span class="badge badge-blue">Java</span>
                                    <span class="badge badge-blue">JavaScript</span>
                                    <span class="badge badge-blue">Prolog</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4 scroll-reveal">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <h5 class="card-title mb-3"><i class="bi bi-gear text-primary me-2"></i>DevOps & Tools</h5>
                                <div class="d-flex flex-wrap gap-2">
                                    <span class="badge bg-success">Enterprise Automation</span>
                                    <span class="badge bg-success">Network Security</span>
                                    <span class="badge bg-success">Dagster</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <h5 class="card-title mb-3"><i class="bi bi-cpu text-primary me-2"></i>AI & Data Science</h5>
                                <div class="d-flex flex-wrap gap-2">
                                    <span class="badge bg-info">Machine Learning</span>
                                    <span class="badge bg-info">Data Mining</span>
                                    <span class="badge bg-info">Large Language Models</span>
                                    <span class="badge bg-info">OpenAI Products</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4"> 
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <h5 class="card-title mb-3"><i class="bi bi-window text-primary me-2"></i>Web Development</h5>
                                <div class="d-flex flex-wrap gap-2">
                                    <span class="badge bg-warning text-dark">ReactJS</span>
                                    <span class="badge bg-warning text-dark">Laravel</span>
                                    <span class="badge bg-warning text-dark">Flask</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <h5 class="card-title mb-3"><i class="bi bi-phone text-primary me-2"></i>Mobile Development</h5>
                                <div class="d-flex flex-wrap gap-2">
                                    <span class="badge bg-danger">Android Development</span>
                                    <span class="badge bg-danger">Java</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-4">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <h5 class="card-title mb-3"><i class="bi bi-cloud text-primary me-2"></i>Cloud & Services</h5>
                                <div class="d-flex flex-wrap gap-2">
                                    <span class="badge bg-secondary">SaaS</span>
                                    <span class="badge bg-secondary">Distributed Computing</span>
                                    <span class="badge bg-secondary">IoT Systems</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Education Section -->
        <section id="education" class="py-5 bg-light">
            <div class="container">
                <h2 class="display-6 fw-bold mb-5 text-center section-title">Education</h2>
                
                <div class="row g-4">
                    <div class="col-md-6 scroll-reveal">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <div class="d-flex justify-content-between align-items-start mb-3">
                                    <div>
                                        <h4 class="card-title mb-1">Master of Science</h4>
                                        <h5 class="text-primary mb-2">Universität Koblenz</h5>
                                    </div>
                                    <span class="badge bg-success px-3 py-2">Completed 2025</span>
                                </div>
                                <p class="card-text fw-semibold">Web and Data Science</p>
                                <p class="text-muted mb-0"><i class="bi bi-geo-alt me-2"></i>Koblenz, Germany</p>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-6 scroll-reveal">
                        <div class="card border-0 shadow-sm h-100 card-hover">
                            <div class="card-body p-4">
                                <div class="d-flex justify-content-between align-items-start mb-3">
                                    <div>
                                        <h4 class="card-title mb-1">Bachelor of Science</h4>
                                        <h5 class="text-primary mb-2">North South University</h5>
                                    </div>
                                    <span class="badge bg-secondary">2015 - 2019</span>
                                </div>
                                <p class="card-text fw-semibold">Computer Science and Engineering</p>
                                <p class="text-muted mb-0"><i class="bi bi-geo-alt me-2"></i>Dhaka, Bangladesh</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="mt-5">
                    <h4 class="mb-4 text-center">Certifications & Achievements</h4>
                    <div class="row g-3">
                        <div class="col-md-6 scroll-reveal">
                            <div class="d-flex align-items-center p-3 bg-white rounded shadow-sm card-hover">
                                <i class="bi bi-award text-success fs-3 me-3"></i>
                                <div>
                                    <h6 class="mb-0">1st Runner up - Innovation Challenge Season 7</h6>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 scroll-reveal">
                            <div class="d-flex align-items-center p-3 bg-white rounded shadow-sm card-hover">
                                <i class="bi bi-patch-check text-primary fs-3 me-3"></i>
                                <div>
                                    <h6 class="mb-0">Dagster Essentials</h6>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="d-flex align-items-center p-3 bg-white rounded shadow-sm card-hover">
                                <i class="bi bi-patch-check text-primary fs-3 me-3"></i>
                                <div>
                                    <h6 class="mb-0">Distributed Computing</h6>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="d-flex align-items-center p-3 bg-white rounded shadow-sm card-hover">
                                <i class="bi bi-patch-check text-primary fs-3 me-3"></i>
                                <div>
                                    <h6 class="mb-0">AI JAM: Hands on with LLM</h6>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Publications Section -->
        <section class="py-5 bg-light">
            <div class="container">
                <h2 class="display-6 fw-bold mb-4 text-center">Research & Publications</h2>
                <div class="row justify-content-center">
                    <div class="col-lg-10">
                        <div class="card border-0 shadow-sm card-hover">
                            <div class="card-body p-4">
                                <div class="d-flex align-items-start">
                                    <i class="bi bi-file-earmark-text text-primary fs-2 me-3 mt-1"></i>
                                    <div>
                                        <h5 class="card-title fw-bold">Aquatic Iguana: A Floating Waste Collecting Robot with IoT Based Water Monitoring System</h5>
                                        <p class="text-muted mb-2">Research Publication</p>
                                        <p class="card-text">Innovative research focused on environmental technology, combining robotics and IoT systems for sustainable water management and waste collection solutions.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="py-5 bg-dark text-white">
            <div class="container">
                <div class="row justify-content-center text-center">
                    <div class="col-lg-8">
                        <h2 class="display-6 fw-bold mb-4">Let's Connect</h2>
                        <p class="lead mb-4">Interested in collaboration, research opportunities, or just want to chat about tech? Feel free to reach out!</p>
                        
                        <div class="d-flex justify-content-center gap-4 mb-4">
                            <a href="mailto:abdullah.kabir12@gmail.com" class="text-white text-decoration-none">
                                <i class="bi bi-envelope fs-1"></i>
                                <p class="small mt-2 mb-0">Email</p>
                            </a>
                            <a href="https://www.linkedin.com/in/abdullahkabir" target="_blank" class="text-white text-decoration-none">
                                <i class="bi bi-linkedin fs-1"></i>
                                <p class="small mt-2 mb-0">LinkedIn</p>
                            </a>
                            <a href="tel:+4915750709337" class="text-white text-decoration-none">
                                <i class="bi bi-telephone fs-1"></i>
                                <p class="small mt-2 mb-0">Phone</p>
                            </a>
                        </div>

                        <div class="mt-4">
                            <p class="mb-1"><i class="bi bi-geo-alt me-2"></i>Koblenz, Rhineland-Palatinate, Germany</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="bg-black text-white py-4">
            <div class="container text-center">
                <p class="mb-0">&copy; 2026 Abdullah Kabir. All rights reserved.</p>
                <a href="https://www.freepik.com/icon/personal-profile_2194267">Icon by Freepik</a>
            </div>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script>
            // Smooth scrolling for navigation links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }
                });
            });
            
            // Animate section titles on load
            window.addEventListener('load', function() {
                document.querySelectorAll('.section-title').forEach(title => {
                    setTimeout(() => {
                        title.classList.add('animate');
                    }, 100);
                });
            });
            
            // Scroll reveal animation
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };
            
            const observer = new IntersectionObserver(function(entries) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);
            
            document.querySelectorAll('.scroll-reveal').forEach(el => {
                observer.observe(el);
            });
            
            // Navbar background change on scroll
            window.addEventListener('scroll', function() {
                const navbar = document.querySelector('.navbar');
                if (window.scrollY > 50) {
                    navbar.style.backgroundColor = 'rgba(17, 24, 39, 1)';
                } else {
                    navbar.style.backgroundColor = 'rgba(17, 24, 39, 0.95)';
                }
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html, profile_image=profile_image, icon=icon)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
