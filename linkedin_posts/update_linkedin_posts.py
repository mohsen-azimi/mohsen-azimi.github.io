import os
import json
import yaml


cfg = yaml.load(open('config.yaml', 'r'), Loader=yaml.FullLoader)


#
def embed_linkedin_post(url, h, w,frameborder=0, allowfullscreen=True):
    return f"""
    <iframe src="{url}" width="{w}" height="{h}" frameborder="{frameborder}" allowfullscreen="{allowfullscreen}"></iframe>
    """



def generate_html(cfg):

    html = f"""
    
    <!DOCTYPE HTML>
    
    <html>
        <head>
            <title>LinkedIn Posts</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
            <link rel="stylesheet" href="../assets/css/main.css" />
            <link rel="stylesheet" href="../assets/css/main_yaksoy.css" />
            <link rel="stylesheet" href="../assets/css/academicons.min.css"/>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
        <!-- Bootstrap -->
        <link href="../assets/css/bootstrap-4.4.1.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> 
    
        <meta charset="utf-8">
            <meta name="description" content="LinkedIn Posts">
    
    
            <!-- Webmaster Tools verfication -->
            <!-- <meta name="google-site-verification" content="googleb0479c04a25255c3">
     -->
    
    
    
            <!-- Webfonts -->
            <script src="//use.edgefonts.net/source-sans-pro:n2,i2,n3,i3,n4,i4,n6,i6,n7,i7,n9,i9;source-code-pro:n4,n7;volkhov.js"></script>
    
            <meta http-equiv="cleartype" content="on">
    
    
    
    
        </head>
        <body class="is-preload">
    
            <!-- Wrapper -->
                <div id="wrapper">
    
                    <!-- Main -->
                        <div id="main">
                            <div class="inner">
    
                                <!-- Header -->
                                    <header id="header">
                                        <a href="https://mohsen-azimi.github.io/publications/" class="logo"><strong>Publications</strong></a>
                                        <ul class="icons">
                                            <li><a href="https://mohsen-azimi.github.io" class="icon brands fa-home"><span class="label">Home</span></a></li>
                                            <li><a href="https://www.linkedin.com/in/mohsenazimi/" class="icon brands fa-linkedin"><span class="label">LinkedIn</span></a></li>
                                            <li><a href="https://www.researchgate.net/profile/Mohsen_Azimi" class="icon brands fa-researchgate"><span class="label">ResearchGate</span></a></li>
                                            <li><a href="https://github.com/mohsen-azimi" class="icon brands fa-github"><span class="label">GitHub</span></a></li>
                                        </ul>
                                    </header>
    
    
    
    
    <h2><a href="https://mohsen-azimi.github.io/"><i class="fas fa-arrow-left"></i> Back</a></h2>


                                <!-- Banner -->
                                <hr />
                                    <section id="container">
    
    
        
    """

    for url in cfg['linkedin_posts']:
        print(url)
        html += embed_linkedin_post(url, cfg["height"], cfg["width"], cfg["frameborder"], cfg["allowfullscreen"])

    html += """
   
                                  <br>	
                                                                              
                            </div>
                        </div>
    
                    <!-- Sidebar -->
    
    
                </div>
    
            <!-- Scripts -->
                <script src="assets/js/jquery.min.js"></script>
                <script src="assets/js/browser.min.js"></script>
                <script src="assets/js/breakpoints.min.js"></script>
                <script src="assets/js/util.js"></script>
                <script src="assets/js/main.js"></script>
    

    
    
        </body>
    </html>
    """




    return html


posts_list_html = generate_html(cfg)

with open("./index.html", "w",encoding='utf-8') as output_file:

        output_file.write(posts_list_html)