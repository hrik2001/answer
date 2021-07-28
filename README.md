# !answer
!answer is a discord bot that leverages state of the art artifical intelligence to serve your users in your
discord guild. You can give the bot context paragraphs, from which the bot will reply to any questions of users.
Best used to answer a user's doubt about FAQs or rules or venue.  
!answer also plans to release moderation tools and a real time dashboard for the ease of discord admins and moderators  


## Installation
If you want to use it locally or host this yourself, then here is what you have to do.   
*Note: For local users its recommended to use virtualenv or any other such environment*
```bash
git clone --recurse-submodules https://github.com/hrik2001/answer.git   #if you want to install via https
git clone --recurse-submodules git@github.com:hrik2001/answer.git       #if you want to install via ssh
```
*Note: you can also -jN parameter, right after `--recurse-submodules` parameter where N being number of process that helps in recursively cloning submodules, though not needed*
<br>
Now one has to install pytorch. Get it from [here](https://pytorch.org/get-started/locally/)  
Now we have to install `transformers` from huggingface. For that  
```bash
pip install -U transformers
```
Then proceed to install nltk and punkt
```bash
pip install nltk && python -m nltk.downloader punkt
```
*Note: pip may point to pip2 for you, either type pip3 or make sure that pip doesnt point to pip2*  
Then do the following (in the repo)  
```bash
pip install -r requirements.txt
```
First run would make you download the pre-trained model. After that, there won't be any need.

## Contributing
Fork this repo and follow the above steps (for your own repo, not the upstream aka this repo)  
After that go to your freshly downloaded repo and add the following  
```bash
git remote add upstream https://github.com/hrik2001/answer.git   #if you want http remote
git remote add upstream git@github.com:hrik2001/answer.git       #if you want ssh remote
```
Now, you can pull from upstream to make updates to the `master` branch of your fork and also locally  
That's all folks!

