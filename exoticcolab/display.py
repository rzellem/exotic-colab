from IPython.display import display, HTML, Javascript
import random
import time
import progressbar
import urllib.request

######################################################

# Grabs a stylesheet, call this before any html output in cell
def importCustomStyles():
  custom_stylesheet_url = 'https://exoplanets.nasa.gov/system/exotic/colab.css?i=' + str(random.random())
  display(HTML('<link rel="stylesheet" href="' + custom_stylesheet_url + '">'))

def importCustomJS():
  custom_js_url = 'https://exoplanets.nasa.gov/system/exotic/colab.js?i=' + str(random.random())
  display(HTML('<script type="text/javascript" src="' + custom_js_url + '">'))

def importCustomJSasHTML():
  # open a connection to a URL using urllib
  custom_html_url = 'https://exoplanets.nasa.gov/system/exotic/colab.html?i=' + str(random.random())
  webUrl  = urllib.request.urlopen(custom_html_url)

  # read the data from the URL and print it
  exotic_html = webUrl.read().decode('utf-8')
  display(HTML(exotic_html))

def setupDisplay():
  importCustomStyles()
  importCustomJSasHTML()

######################################################

def testImplementation(): 
  display(HTML('<p>CODE IMPLEMENTED SUCCESSFULLY</p>'))

######################################################

def displayStep(message):
  js_code = '''\
                var container = document.querySelector("#output-body ul.step_container");\
                container.innerHTML += '<li class="step1">{m}</li>';
                '''.format(m=message)
  display(Javascript(js_code))

def makeContainer(container_class):
  display(HTML('<div class="' + container_class + '"></div>'))

def appendToContainer(container_selector, html_chunk):
  js_code = '''\
                var container = document.querySelector("#output-body {c}");\
                container.innerHTML += '{m}';
                '''.format(c=container_selector, m=html_chunk)
  display(Javascript(js_code))

######################################################
  
def expandableSection(content):
  html_content = '''\
    <div class="expandable" onclick="show_or_hide(this)">
      <div class="expand_text">+ MORE</div>
      <div class="hidden">
        {expand_content}
      </div>
    </div>
    '''.format(expand_content=content)
  display(HTML(html_content))

def hideWarning():
  js_code = '''\
                document.querySelector('#output-body .step1').parentElement.parentElement.nextElementSibling.style.display = "none"
                '''
  display(Javascript(js_code))

def downloadButton(text,download_target,filename):
  display(HTML('<a class="big_button" href="' + download_target + '" href="' + filename + '">' + text + '</a>'))

# Creates a progress bar that just runs for `seconds` number of seconds
def showProgress(seconds):
  with progressbar.ProgressBar(max_value=100) as bar:
    for idx, val in enumerate(range(100)):
      time.sleep(seconds/100)
      bar.update(idx)

######################################################

# Avoids scroll-in-the-scroll in the entire Notebook
def resize_colab_cell():
  display(Javascript('google.colab.output.setIframeHeight(0, true, {maxHeight: 5000})'))
