from davinci import output as davinci_output
from linkedin_api import output as linkedin_output

prompt = ("A LinkedIn post on one interesting python hack to make your life easier. Include hash tags.")
print(davinci_output(prompt))


linkedin_output(davinci_output(prompt))
# linkedin_output("hello world", "https://abhijith14.github.io/Portfolio-v2/media/buddyai.png")
