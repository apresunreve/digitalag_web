#!/usr/bin/python3                                                                                                                                                                                                               

import cgi
import cgitb
import urllib.request
import google.oauth2.credentials
import google_auth_oauthlib.flow
import flask
from flask import request

cgitb.enable()
print(
'''Content-type: text/html

<!doctype html>
<html lang="en">

<head>
''')

auth_site = """
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="viewport"
    content="user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=320, height=device-height, target-densitydpi=medium-dpi" />
  <title>DAB website</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <link href='https://fonts.googleapis.com/css?family=Space Grotesk' rel='stylesheet'>
  <link rel="stylesheet" type="text/css" href="http://149.165.155.188:2298/css/style.css"> 
  <!--  <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}"> -->
  

</head>
<!-- https://user-images.githubusercontent.com/69735000/208339849-f5f07bf6-b743-4d54-953b-fc5cbec387be.png -->

<body>

  <!-- HOME PAGE STARTS HERE -->
  <div class="container-fluid">
    <div class="line"></div>
    <div class="container-fluid">
      <nav class="navbar navbar-expand-sm navbar-light">
        <div class="navbar-brand">
          <div class="container ms-sm-0 ms-md-5">
            <div class="row">
              <div class="col-12">
                <div class="logoContainerLrg">ICICLE Digital Agriculture</div>
              </div>

              <div class="col-12">
                <div class="logoContainerSml">Intelligent Cyberinfrastructure with Computational Learning<br> in the Environment: Digital Agriculture Transformation<br>
                    <a href="https://icicle.osu.edu/"><img src="https://reroutlab.org/images/iciclelogo.jpg" style="width: 11vw; min-width: 65px;" alt="Logo of the ICICLE AI Institute"></a></div>
              </div>
            </div>
          </div>
        </div>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#toggleMobileMenu"
          aria-controls="toggleMobileMenu" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="toggleMobileMenu">
          <ul class="navbar-nav ms-auto text-center">
            <li>
              <a class="nav-link me-2 active" href="#">Home</a>
            </li>
            <li>
              <a class="nav-link me-2" href="#testimonialOne">Mission</a>
            </li>
            <li>
              <a class="nav-link me-2" href="#product">OpenPASS</a>
            </li>
            <li>
              <a class="nav-link me-2" href="#about">About</a>
            </li>
            <li>
              <a class="nav-link me-2" href="#contact">Contact/Demo</a>
            </li>
             <li>
                <a class="nav-link me-2" href="#contact"><b>Welcome DABGoogleUserDAB</b></a>
     	      </li>
          </ul>
        </div>
      </nav>
    </div>

    <div class="container-fluid">
      <div id="parent" class="row ">
        <div id="sloganNInfo" class="col-md-6 col-sm-12 adjustPic">
          <div id="slogan" class="container-fluid adjustSlogan">

            <div class="bigSlogan"><i><u>AI for All </i></u></div>
            <!-- to advanced digital agriculture infrastracture -->
            <div class="smallSlogan ">We are democratizing<br> next-gen cyberinfrastructure
            <br> to bring cutting-edge AI<br> to realize the digital agriculture revolution<br></div>
            <!-- fully autonomouse crop scouting for farmers -->
            <button type="button" class="btn homeBtn adjustHomeBtn" onClick="document.getElementById('product').scrollIntoView();" >
              Learn More: openPASS
            </button>
          </div>

          <div id="infoBoxes" class="container-fluid adjustInfo" style="background-color: white;">
            <div class="row logos">
              <div class="col-4">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-3">
                      <img
                        src="https://user-images.githubusercontent.com/69735000/210031679-917d2b37-678c-47b6-96de-3e286895a04d.png"
                        class="float-start smlInfoLogo">
                      </img>
                    </div>
                    <div class="col-9">
                      <div class="infoContainer">
                        Map fields autonomously<br> and continiously
                        <!--  map fields autonomously and continiously-->
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-4">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-3">
                      <img
                        src="https://user-images.githubusercontent.com/69735000/210151898-4cf6620b-a775-4c71-9cb5-d68191adad62.png"
                        class="float-start smlInfoLogo">
                      </img>
                    </div>
                    <div class="col-9">
                      <div class="infoContainer">
                        Make better crop<br>management decisions
                        <!-- make better crop management decisions -->
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-4">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-3">
                      <img
                        src="https://user-images.githubusercontent.com/69735000/210152313-40227037-3f44-4953-8848-78d0c43a234b.png"
                        class="float-start smlInfoLogo">
                      </img>
                    </div>
                    <div class="col-9">
                      <div class="infoContainer">
                        State of the art <br>edge computing
                        <!-- state of the art edge computing -->
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="pic" class="col-md-6 adjustSloganNInfo">
          <img
            src="https://user-images.githubusercontent.com/69735000/210019352-a3d5a913-d351-40d0-bb96-14f1ccb9da0b.png"
            class="float-start adjustImg float-left">
        </div>
      </div>
    </div>
  </div>

  <!-- HOME PAGE END HERE & TESTIMONIALS STARTS -->
  <div id="testimonialOne" class="container-fluid testimonialContainer">
    <div class="container-fluid testimonialStyleContainer">
    </div>
    <div class="container-fluid">
      <div class="row row-cols-auto">
        <div class="col-4 testimonialSentenceLg">
	 What is<br><b>Digital Agriculture?</b>
        </div>
        <div class="col-4 testimonialSentenceSm">
          9 million children suffer from food insecurity.
          Migrant workers in food production die, on average,
          38 years sooner than well-off Americans. <br>
          <b>Digital Agriculture</b> uses AI, IoT sensors,
          edge computing, and agricultural engineering to 
          transform crop and farm management, increasing yield,
          improving working conditions, and remedying crop
          health problems quickly and precisely.<br>
          <b> What is cyberinfrastructure (CI)?</b>
           CI includes the software and hardware needed to 
           realize digital agriculture. Unfortunately, 
           CI needed for advanced AI systems could be 
           more cost-effective, limiting its impact.  We design,
           prototype, and deploy accessible and affordable
           CI for digital agriculture, <b><u>AI for ALL</u></b>.
        </div>
      </div>
    </div>
  </div>


  <!-- TESTIMONIALONE PAGE END HERE & PRODUCT STARTS -->
  <div id="product" class="container-fluid productContainer">
    <div class="container-fluid productInfo">
      <div class="row">
        <div class="col-1" style="background-color:white;">
        </div>
        <div class="col-10">
          <div class="productInfoTitle">
          <b>openPASS:</b>Open-Source, Plug-and-Play,<br> Aerial Crop Scouting for Soybean Fields
          </div>
          <div class="productInfoDescription">
OpenPASS is an open-source web and mobile application that allows farmers, 
in-field operations consultants, agronomy researchers and hobbyists to automatically deploy software-piloted small unmanned aerial systems for rapid aerial scouting of soybean crop health. Our first major CI product, OpenPASS builds upon our recent innovative deep-learning software for characterizing the severity of soybean defoliation in crop fields and represents
joint development with ICICLE and the Ohio Soybean Council.  Our deep-learning software can accurately characterize severe defoliation from aerial photos and, combined with novel AI software, we can map defoliation levels across a whole field, with high confidence, <b>in minutes to hours</b>.
          </div>
        </div>
        <div class="col-1" style="background-color:white;">
        </div>
      </div>
    </div>
    <div class="container-fluid productsContainer">
      <div class="row">
        <div class="col-1">
        </div>
        <div class="col-10">
          <div class="container-fluid">
            <div class="row row-cols-auto">
              <div class="col-3">
                <div class="container text-center">
                  <div class="productImgContainer mx-auto">
                    <img
                      src="https://cdn.thewirecutter.com/wp-content/media/2022/10/drones-2048px-0706-2x1-1.jpg?auto=webp&quality=75&crop=2:1&width=1024&dpr=2"
                      alt="image" class="img-fluid productImg ">
                  </div>
                  <div class="productTitleContainer">
                    <a>Unmanned Aerial System</a>
                  </div>
                  <div class="productContentContainer">
                    Step 1: You will ship our drones and infrastructure to you.
                    You simply unpack the box, link your smartphone, and start missions.
                  </div>
                </div>
              </div>
              <div class="col-3">
                <div class="container text-center">
                  <div class="productImgContainer mx-auto">
                    <img src="https://reroutlab.org/images/fieldmap.jpg" alt="image"
                      class="img-fluid productImg ">
                  </div>
                  <div class="productTitleContainer">
                    Map Fields Autonomously
                  </div>
                  <div class="productContentContainer">
                    Step 2: Set GPS boundaries and a crop 
                    condition of interest, our system will
                    fly autonomously and produce
                    a field map in real time.
                  </div>
                </div>
              </div>
              <div class="col-3">
                <div class="container text-center">
                  <div class="productImgContainer mx-auto">
                    <img
                      src="https://reroutlab.org/images/soybeanfield.jpg"
                      alt="image" class="img-fluid productImg ">
                  </div>
                  <div class="productTitleContainer">
                    Use Data to Manage your Field
                  </div>
                  <div class="productContentContainer">
                    Step 3: Use the map to inform pesticide and fertilizer applications.
                    Upload our maps to compatible sprayers.
                  </div>
                </div>
              </div>
              <div class="col-3">
                <div class="container text-center">
                  <div class="productImgContainer mx-auto">
                    <img src="https://miro.medium.com/max/1400/1*e-f-6BRq4-Bv4jW6CSjiTg.webp" alt="image"
                      class="img-fluid productImg ">
                  </div>
                  <div class="productTitleContainer">
                    State of the Art Computing
                  </div>
                  <div class="productContentContainer">
                    Step 4: Optionally, send data back to ICICLE.
                    This helps us create more products
                    using access to efficient, high performance computing.
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-1">
        </div>
      </div>
    </div>
  </div>

  <!-- DEMO PAGE END HERE & ABOUT STARTS -->
  DABprivate_ms.htmlDAB
  <!-- ABOUT PAGE END HERE & CONTACT STARTS -->
  <div id="contact" class="container-fluid contactContainer">
    <div class="container contact__container">
      <div class="contact__left">
        <h2>Contact</h2>
        <p>
          Interested in using OpenPASS?  Please reach out to us using the form below.
          
        </p>
      </div>
      <iframe width="480px" height="250px" src="https://forms.office.com/r/2nViF5mUNi" frameborder="0" marginwidth="0"
        marginheight="0" allowfullscreen webkitallowfullscreen mozallowfullscreen msallowfullscreen></iframe>
    </div>


  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous">
    </script>
  <script src="http://149.165.155.188:2298/js/main.js">
  <!-- <script src="{% static 'js/main.js' %}"></script> -->
  <!-- <link rel="stylesheet" type="text/css" href="{% static 'js/main.js' %}"> -->
  </script>
</body>

</html>

"""


errorHTML = '''<head>\n
<meta http-equiv=\"refresh\" content=\"2; url=\'https://go.osu.edu/icicle-ag"  + "\'\" />

</head>
<body>
<p>You browser has accessed an invalid link: CAUSE. Redirecting to our homepage.</p>
</body>
</html>
'''

with open('/opt/bitnami/apache2/htdocs/private_ms.html', 'r') as file:
    private_msHTML = file.read()

#actualHost="149.165.155.188:2298"
#develEnv = "prod"
#with open('/root/environment', 'r') as file:
#    develEnv = file.readline().strip()
#if (develEnv == "devel"):
#    actualHost = 'localhost:30080'


form = cgi.FieldStorage()
code = str(form.getvalue("code"))
codeExists=0
if code:
    codeExists = 1
if (codeExists == 0):
    errorHTML = errorHTML.replace("CAUSE","No Code element")
    print(errorHTML)

state = str(form.getvalue("state"))
stateExists=0
if code:
    stateExists = 1
if (stateExists == 0):
    errorHTML =errorHTML.replace("CAUSE","No email element")    
    print(errorHTML)
state=state.replace("DAB","@")

auth_site=auth_site.replace("DABGoogleUserDAB", state)
auth_site=auth_site.replace("DABprivate_ms.htmlDAB", private_msHTML)
auth_site=auth_site.replace("/cgi-bin/callms.py?", "/cgi-bin/callms.py?state="+ state +"&code="+code + "&")

print(auth_site)
