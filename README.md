# Terminology & trends in machine learning research
### Data-driven ANALYSIS OF NIPS and ICML CONTENT


Full blog post: https://nycdatascience.com/blog/student-works/can-i-use-data-science-techniques-to-speed-up-my-ml-learning-spoiler-a-bit/

- I used a web scraper to extract publicly available research content from two of the top machine learning techniques (NeurIPS and ICML) over the period 2007-19 to generate a rich dataset of ~12,000 texts
- Unsupervised topic modelling is used to explore clustering of terms across research areas; however, manual topic creation more clearly demonstrates trends over time
- I also experimented with recent transfer learning techniques to develop a language model to generate “fake abstracts” which might be quite hard to distinguish for non-experts
- Tools used: python, Google Colab, Scrapy, gensim, spaCy, regex, fast.ai libraries
