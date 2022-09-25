from IPython.display import display, HTML, Javascript
import urllib.request
import random
import time
import progressbar

# Grabs a stylesheet, call this before any html output in cell
def importCustomStyles():
  custom_stylesheet_url = 'https://exoplanets.nasa.gov/system/exotic/colab.css?i=' + str(random.random())
  display(HTML('<link rel="stylesheet" href="' + custom_stylesheet_url + '">'))

def setupDisplay():
  # open a connection to a URL using urllib
  custom_html_url = 'https://exoplanets.nasa.gov/system/exotic/colab.html?i=' + str(random.random())
  webUrl  = urllib.request.urlopen(custom_html_url)

  #get the result code and print it
  display("result code: " + str(webUrl.getcode()))

  # read the data from the URL and print it
  exotic_html = webUrl.read().decode('utf-8')
  display(HTML(exotic_html))

def testImplementation(): 
  display(HTML('<p>CODE IMPLEMENTED SUCCESSFULLY</p>'))

def displayStep(message):
  #display('in displayStep')
  js_code = '''\
                var container = document.querySelector("#output-body ul.step_container");\
                container.innerHTML += '<li class="step1">{m}</li>';
                '''.format(m=message)
  display(Javascript(js_code))

def makeContainer(container_class):
  display(HTML('<div class="' + container_class + '"></div>'))

def appendToContainer(container_class, html_chunk):
  #display(HTML('<p>appendingToContainer</p>'))
  js_code = '''\
                var container = document.querySelector("#output-body .{c}");\
                container.innerHTML += '{html_chunk}';
                '''.format(c=container_class, m=html_chunk)
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


# Creates a progress bar that just runs for `seconds` number of seconds
def showProgress(seconds):
  with progressbar.ProgressBar(max_value=100) as bar:
    for idx, val in enumerate(range(100)):
      time.sleep(seconds/100)
      bar.update(idx)

# Avoids scroll-in-the-scroll in the entire Notebook
def resize_colab_cell():
  display(Javascript('google.colab.output.setIframeHeight(0, true, {maxHeight: 5000})'))
