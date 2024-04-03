import wikipedia
import time
topics = wikipedia.search("generative artificial intelligence")

print("Topics related to 'generative artificial intelligence':")
for topic in topics:
    print(f"Title: {page_title}")
    print("References:")
    for reference in page_references:
        print(reference)
    print()

start_time = time.perf_counter()
myfunc1()
end_time = time.perf_counter()
lapsed1 = end_time - start_time

urls = ["https://en.wikipedia.org/wiki/Generative_artificial_intelligence",
        "https://en.wikipedia.org/wiki/Artificial_general_intelligence",
        "https://en.wikipedia.org/wiki/Music_and_artificial_intelligence"]

def multithread():
  
  def url_download(url):
    page = requests.get(url)
    html_content = page.text
    html_content.encode('utf-8')
    out_filename = url.split("wiki/")[1] + ".txt"
    print(f'output filename: {out_filename}')
    with open(out_filename, 'wt', encoding='utf-8') as fileobj:
      fileobj.write(html_content)

  # configure the TPE to loop through urls concurrently
  with ThreadPoolExecutor() as executor:
    executor.map(url_download, urls)

# use name == main idiom to execute the following when run directly (not imported)
if __name__ == "__main__":
  multithread()