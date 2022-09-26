from IPython.display import display, HTML, Javascript
import random
import time
import progressbar

# Grabs a stylesheet, call this before any html output in cell
def importCustomStyles():
  custom_stylesheet_url = 'https://exoplanets.nasa.gov/system/exotic/colab.css?i=' + str(random.random())
  display(HTML('<link rel="stylesheet" href="' + custom_stylesheet_url + '">'))

def importCustomJS():
  custom_js_url = 'https://exoplanets.nasa.gov/system/exotic/colab.js?i=' + str(random.random())
  display(HTML('<script type="text/javascript" src="' + custom_js_url + '">'))

def setupDisplay():
  importCustomStyles()
  importCustomJS()

def testImplementation(): 
  display(HTML('<p>CODE IMPLEMENTED SUCCESSFULLY</p>'))

def displayStep(message):
  js_code = '''\
                var container = document.querySelector("#output-body ul.step_container");\
                container.innerHTML += '<li class="step1">{m}</li>';
                '''.format(m=message)
  display(Javascript(js_code))

def makeContainer(container_class):
  display(HTML('<div class="' + container_class + '"></div>'))

def downloadButton(text,download_target,filename):
  display(HTML('<a class="big_button" href="' + download_target + '" href="' + filename + '">' + text + '</a>'))

def appendToContainer(container_selector, html_chunky):
  html_chunkles = html_chunky
  js_code = '''\
                var container = document.querySelector("#output-body {c}");\
                container.innerHTML += '{m}';
                '''.format(c=container_selector, m=html_chunkles)
  display(Javascript(js_code))
  
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


# Creates a progress bar that just runs for `seconds` number of seconds
def showProgress(seconds):
  with progressbar.ProgressBar(max_value=100) as bar:
    for idx, val in enumerate(range(100)):
      time.sleep(seconds/100)
      bar.update(idx)

# Avoids scroll-in-the-scroll in the entire Notebook
def resize_colab_cell():
  display(Javascript('google.colab.output.setIframeHeight(0, true, {maxHeight: 5000})'))
