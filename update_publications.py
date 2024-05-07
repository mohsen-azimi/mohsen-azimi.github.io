import os
import json


def generate_publication_page(publication_info):
    # Start building the HTML content
    html_content = f"""
    <!DOCTYPE HTML>
    <html>
        <head>
		<title>{publication_info["name"]}</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="../../assets/css/main.css" />
		<link rel="stylesheet" href="../../assets/css/academicons.min.css"/>
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
	    <!-- Bootstrap -->
	    <link href="../../assets/css/bootstrap-4.4.1.css" rel="stylesheet">
	    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> 
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
                                        <li><a href="https://mohsen-azimi.github.io" class="icon"><i class="fa fa-home fa-lg" aria-hidden="true"></i><span class="label">Home</span></a></li>
                                        <li><a href="https://www.linkedin.com/in/mohsenazimi/" class="icon brands fa-linkedin"><span class="label">LinkedIn</span></a></li>
                                        <li><a href="https://www.researchgate.net/profile/Mohsen_Azimi" class="icon brands fa-researchgate"><span class="label">ResearchGate</span></a></li>
                                        <li><a href="https://github.com/mohsen-azimi" class="icon brands fa-github"><span class="label">GitHub</span></a></li>
                                    </ul>
								</header>
    """

    # Add the closing tags
    html_content += f"""
							<!-- Banner -->
								<section id="container">

									<div class="jumbotron text-center mt-0">
								      <div class="container">
								        <div class="row">
								          <div class="col-12">

								            <h2>{publication_info["title"]}</h2>
								            <h4 style="color:#5a6268;">{publication_info["journal"]}</h4>
								            <hr>
								            <h6> 
					"""

    for author, details in publication_info["authors"].items():
        html_content += f'<a href="{details["website"]}" target="_blank">{author}</a><sup>{details["affiliation"]+1}</sup>'
        if author != list(publication_info["authors"].keys())[-1]:
            html_content += ", "




    html_content += """
                                        </h6>"""




    for i, affiliation in enumerate(publication_info["affiliations"]):
        html_content += f"""
								            <p><sup>{i+1}</sup>{affiliation} &nbsp;&nbsp; 
        """

    html_content += f"""
								                
								            <div class="row justify-content-center">
								            
								              <div class="column">
								                  <p class="mb-5"><a class="btn btn-large btn-light" href="{publication_info["url"]}" role="button"  target="_blank">
								                    <i class="fa fa-file"></i> Paper</a> </p>
								              </div>
								              
								              <div class="column">
								                <p class="mb-5"><a class="btn btn-large btn-light" href="{publication_info["code_url"]}" role="button">
								                  <i class="fa fa-github-alt"></i> Code</a> </p>
								              </div>
								              
								              <div class="column">
								                  <p class="mb-5"><a class="btn btn-large btn-light" href="{publication_info["supplementary_url"]}" role="button">
								                    <i class="fa fa-file"></i> Supplementary </a> </p>
								              </div>
								              
								            </div>

								          </div>
								        </div>
								      </div>
								    </div>


								</section>

							<!-- abstract -->
							  <section>
							    <div class="container">
							      <div class="row">
							        <div class="col-12 text-center">
							          <h3>Abstract</h3>
							            <hr style="margin-top:0px">
							          <p class="text-left"> {publication_info["abstract"]} </p>
							        </div>
							      </div>
							    </div>


							    <div class="container">
							      <div class="row">
							        <div class="col-12 text-center">
							            <hr style="margin-top:0px">
							            	
							            	<iframe 
							            	src="./{publication_info["name"]}.pdf" width="100%" height="1100px"> 
							            	</iframe>

							            	
							            	


							        </div>
							      </div>
							    </div>
							  </section>






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

    return html_content
#
def publication_preview(publication_info):

    preview = f"""
    <!-- -------------------------------- {publication_info["name"]} -------------------------------- -->
    <table>
    <tr>
    <td class="pub-photocol" >
    <a href="./{publication_info["name"]}/index.html" target="_blank"><img src="./{publication_info["name"]}/icon.jpg" class="pub-photo" /></a>
    </td>
    """

    preview += f"""

    <td>
    <div class="pub-title">
        <a href="./{publication_info["name"]}/index.html" target="_blank">{publication_info["name"]}. {publication_info["title"]}  <i class="fa fa-external-link"></i></a>
    </div>
    
    """


    preview += f"""
    <div class="pub-authors">
    """
    for author, details in publication_info["authors"].items():
        preview += f'<a href="{details["website"]}" target="_blank">{author}</a><sup>{details["affiliation"]+1}</sup>'
        if author != list(publication_info["authors"].keys())[-1]:
            preview += ", "
    preview += f"""
    </div>
    """


    preview += f"""
    <div class="pub-venue">
    """
    for i, affiliation in enumerate(publication_info["affiliations"]):
        preview += f"""
        <a><sup>{i+1}</sup>{affiliation}</a> <br />
        """
    preview += f"""
        {publication_info["journal"]}, {publication_info["year"]}
    </div>
    
    
    <p>   	</p>

    <div class="accordion">
      <input id="{publication_info["name"]}-item1" name="accordion1" type="checkbox" />
      <label for="{publication_info["name"]}-item1">Abstract</label>
      
      <div class="pub-abstract">
       {publication_info["abstract"]}
      </div>
    
      <input id="{publication_info["name"]}-item3" name="accordion1" type="checkbox" />
      <label for="{publication_info["name"]}-item3">BibTeX</label>
      <div class="pub-bibtex">
    
    

    {publication_info["bibtex"]}
    
    
      </div>
    </div>
    </td>
    </tr>

    </td>

    </table>
    <!-- -------------------------------------------------------------------- -->

    """


    return preview

def update_pulications_list(publication_previews):

    publications_list_html = f"""
    
    <!DOCTYPE HTML>
    
    <html>
        <head>
            <title>Publications</title>
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
            <meta name="description" content="Publications">
    
    
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

    for publication_preview in publication_previews:
        publications_list_html += publication_preview

    publications_list_html += """
   
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




    return publications_list_html

list_of_publications = ["j11", "j10", "j09", "j08", "j07", "j06", "j05","j04","j03","j02", "j01"]# , "j01"] # "j01 - Copy"]

previews = []
for publication in list_of_publications:
    print(f"updating {publication}...")
    publication_dir = os.path.join("publications", publication)

    with open(os.path.join(publication_dir, "info.json"), 'r', encoding='utf-8') as f:
        info = json.load(f)

    info["publication_dir"] = publication_dir

    # read the bibtex file
    with open(os.path.join(publication_dir, "bibtex.bib")) as f:
        bibtex = f.readlines()

    info["bibtex"] = ""
    for line in bibtex:
        info["bibtex"] += line.rstrip() + "<br />\n"
    # info["bibtex"] = modified_bibtex


    publication_page = generate_publication_page(info)
    with open(os.path.join(publication_dir, "index.html"), "w", encoding='utf-8') as output_file:

        output_file.write(publication_page)



    previews.append(publication_preview(info))


publications_list_html = update_pulications_list(previews)

with open("./publications/index.html", "w",encoding='utf-8') as output_file:

        output_file.write(publications_list_html)