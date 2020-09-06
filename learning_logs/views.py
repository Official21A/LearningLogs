from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

import datetime
import pytz

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
	# this function sets the home page of the site
	return render(request, 'learning_logs/index.html')

@login_required 
# this function sets a limit for the users to 
# access the links only when they are logged in.
def topics(request):
	# this function sets the topics view page
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')	
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	# show a single topic and all its entries
	topic = Topic.objects.get(id=topic_id)
	check_topic_owner(request, topic)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic' : topic, 'entries': entries}	
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	# this fucntion opens a page for users to input a new topic
	if request.method != 'POST':
		# no data submitted
		form = TopicForm()
	else:
		# process the data
		form = TopicForm(data=request.POST)	
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('learning_logs:topics')
	# display a blank page
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)		

@login_required
def new_entry(request, topic_id):
	# this function opens a page for getting a new entry from user
	topic = Topic.objects.get(id=topic_id)	
	check_topic_owner(request, topic)
	if request.method != 'POST':
		# no data submitted
		form = EntryForm()
	else:
		# process the data
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)	
			new_entry.topic = topic
			new_entry.save()
			return redirect('learning_logs:topic', topic_id=topic_id)
	# display a blank page
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)		

@login_required
def edit_entry(request, entry_id):
	# this function opens a page for editing an entry
	entry = Entry.objects.get(id=entry_id)
	entry.date_added = datetime.datetime.now(pytz.utc)
	topic = entry.topic
	check_topic_owner(request, topic)
	if request.method != 'POST':
		# no data submitted
		form = EntryForm(instance=entry)
	else:
		# process the data
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topic', topic_id=topic.id)	
	# display a blank page		
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(request, topic):
	# owner validation for getting the topics
	if topic.owner != request.user:
		raise Http404